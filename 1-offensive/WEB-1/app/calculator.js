const { parse } = require("csv-parse/sync");
const fs = require('fs');

let countries_, eu_, countries, eu;

try {
  countries_ = fs.readFileSync('public/static/data/countries.csv', 'utf8');
  eu_ = fs.readFileSync('public/static/data/eu.csv', 'utf8');
} catch (err) {
  console.log(`Error while reading a file: ${err}`);
}

countries = parse(countries_, {columns: true, skip_empty_lines: true});
eu = parse(eu_, {columns: true, skip_empty_lines: true});

function is_eu(code) {
  for (let el of eu) {
    if (el.Code == code) {
      return true;
    }
  }
  return false;
}

function calculate(countries, start_date, end_date, rest_type) {
  let price = 2000
  for (let code of countries) {
    if (is_eu(code)) {
      price = 5000;
      break;
    }
  }
  price *= parseInt(countries.length / 3);
  delta_days = parseInt((end_date - start_date) / 86400000);
  delta_weeks = parseInt(delta_days / 7);
  weeks_price = delta_weeks * 500;
  price += weeks_price;
  price *= rest_type;
  return price;
}


module.exports = {
  calculate,
  countries
}
