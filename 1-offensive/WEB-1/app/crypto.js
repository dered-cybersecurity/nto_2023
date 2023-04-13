const CryptoJS = require("crypto-js");

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

module.exports = {
  encrypt,
  decrypt
}
