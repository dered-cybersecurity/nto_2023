const hbs = require('express-hbs');
const express = require('express');
const bodyParser = require('body-parser');
const morgan = require('morgan');
const libxmljs = require("libxmljs");
const crypto = require('./crypto');
const calculator = require('./calculator');
const ws = require('ws');
const http = require('http');
const app = express();

const PORT = process.env.PORT || 8080;
const BIND_ADDR = process.env.BIND_ADDR || '0.0.0.0';

app.use(morgan('dev'));
app.engine('hbs', hbs.express4({}));
app.use(bodyParser.json());
app.set('views', './public');
app.set('view engine', 'hbs');
app.use("/static", express.static(__dirname + "/public/static"));

function decrypted(body) {
  let { data } = body;
  if (!data)
    return data;
  return JSON.parse(crypto.decrypt(data));
}

function encrypted(body) {
  return {'data': crypto.encrypt(JSON.stringify(body))};
}

app.get('/', function(req, res, next){
  res.redirect('/calculate');
});

app.get('/calculate', function(req, res, next){
  const currentYear = new Date().getFullYear();
  const countries = calculator.countries;
  res.render("calculate.hbs", { currentYear, countries });
});

function unpack_xml(data) {
  let doc = libxmljs.parseXml(data, {noent: true});
  let unpacked = Object();
  let args;
  try {
    args = doc.get('//data');
    args.text();
  } catch (e) {
    console.log(e);
    throw new Error('Cannot find <data> tag');
  }
  try {
    unpacked.countries = args.get('//countries').text().split(',');
  } catch (e) {
    console.log(e);
    throw new Error('Cannot find <countries> tag');
  }
  try {
    unpacked.startdate = args.get('//startdate').text();
  } catch (e) {
    console.log(e);
    throw new Error('Cannot find <startdate> tag');
  }
  try {
    unpacked.enddate = args.get('//enddate').text();
  } catch (e) {
    console.log(e);
    throw new Error('Cannot find <enddate> tag');
  }
  try {
    unpacked.resttype = parseInt(args.get('//resttype').text());
  } catch (e) {
    console.log(e);
    throw new Error('Cannot find <resttype> tag');
  }
  return unpacked;
}

function pack_xml(xml, price) {
  let doc = libxmljs.parseXml(xml, {noent: true});
  let allXml = doc.root();
  let args = doc.get('//data').node('price', `${price}`);
  return doc.toString();
}

function get_price(body) {
  if (!body) return undefined;
  let { format, data } = body;
  let data_;
  switch (format) {
    case 'xml':
      data_ = unpack_xml(data)
      break
    default:
      data_ = data
      break
  }
  let { countries, startdate, enddate, resttype } = data_;
  startdate = new Date(startdate);
  enddate = new Date(enddate);
  let price = calculator.calculate(countries, startdate, enddate, resttype);
  let output = Object();
  switch (format) {
    case 'xml':
      output.format = 'xml'
      output.data = pack_xml(data, price)
      break
    default:
      output.format = 'json'
      output.data = {countries: countries, startdate: startdate, enddate: enddate, resttype: resttype, price: price}
      break
  }
  return output;
}

const server = http.createServer(app);
const wss = new ws.Server({ server });

wss.on('connection', (ws) => {
    ws.on('message', (message) => {
        console.log('[WS] received: %s', message);
        if (message == "connected") return;
        try {
          let body = decrypted(JSON.parse(message));
          let output = get_price(body);
          ws.send(JSON.stringify(encrypted(output)));
        } catch (e) {
          console.log(e.stack);
          ws.send(JSON.stringify({'error':e.stack}));
        }
    });

    ws.send('connected');
});

server.listen(PORT, BIND_ADDR, () => {
	console.log('Running on ' + BIND_ADDR + ':' + PORT)
});
