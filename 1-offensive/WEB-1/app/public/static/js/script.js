const socket = new WebSocket(`ws://${location.host}`);

socket.addEventListener('open', (event) => {
  socket.send('connected');
});

const MASTER_PASSWORD = 'InsureYourTravel'

function encrypt(data) {
  var G = CryptoJS.lib.WordArray.random(16);
  key = CryptoJS.PBKDF2(MASTER_PASSWORD, G, {
    keySize: 8,
    iterations: 100
  });
  var iv = CryptoJS.lib.WordArray.random(16);
  var I = CryptoJS.AES.encrypt(data, key, {
    iv: iv,
    padding: CryptoJS.pad.Pkcs7,
    mode: CryptoJS.mode.CBC
  });

  return CryptoJS.enc.Base64.stringify(G.concat(iv).concat(I.ciphertext))
}

function toBase64String(words){
  return CryptoJS.enc.Base64.stringify(words);
}

function decrypt(data) {
  data = CryptoJS.enc.Base64.parse(data)
  var G = CryptoJS.lib.WordArray.create(data.words.slice(0, 4))
  var iv = CryptoJS.lib.WordArray.create(data.words.slice(4, 8))
  var ciphertext = CryptoJS.lib.WordArray.create(data.words.slice(8))
  key = CryptoJS.PBKDF2(MASTER_PASSWORD, G, {
    keySize: 8,
    iterations: 100
  });
  ciphertext = toBase64String(ciphertext);

  var D = CryptoJS.AES.decrypt(ciphertext, key, {
    iv: iv
  }).toString(CryptoJS.enc.Utf8)
  return D
}

function getSelectValues(select) {
  var result = [];
  var options = select && select.options;
  var opt;

  for (var i=0, iLen=options.length; i<iLen; i++) {
    opt = options[i];

    if (opt.selected) {
      result.push(opt.value || opt.text);
    }
  }
  return result;
}

function decrypted(body) {
  let { data } = body;
  if (!data)
    return data;
  return JSON.parse(decrypt(data));
}

function encrypted(body) {
  return {'data': encrypt(JSON.stringify(body))};
}

socket.addEventListener('message', (event) => {
  if (event.data == 'connected') return;
  let data = JSON.parse(decrypt(JSON.parse(event.data).data)).data;
  document.querySelector("#finalPrice").value = data.price;
});

function calculate() {
  let countries = getSelectValues(document.querySelector("#countries"));
  let startDate = document.querySelector("#startDate").value;
  let endDate = document.querySelector("#endDate").value;
  let restType = parseInt(document.querySelector("#restType").value);
  let data = JSON.stringify(encrypted({format: 'json', data: {countries: countries, startdate: startDate, enddate: endDate, resttype: restType}}));
  socket.send(data);
}
