from flask import Flask, render_template, request
from flag import flag
from Crypto.Util.number import *
from random import randint

assert flag.endswith(b'}')
flag = bytes_to_long(flag)

flag = bin(flag)[2:]
assert flag[-2] == '0'

n = getPrime(512) * getPrime(512)


app = Flask(__name__)

@app.route('/')
def intro():
    return render_template('intro.html', n = n)

@app.route('/guess_bit', methods=['GET'])
def guess_bit():
    args = request.args
    if 'bit' not in args.keys():
        return {"error": "Bit needed to be guessed"}
    index = abs(int(args['bit']))

    if index >= len(flag):
        return {"error": "Index overflow"}
    bit = flag[index]

    if bit == '1':
        return {"guess": pow(7, getPrime(300), n)}
    else:
        return {"guess": randint(n//2, n)}

def main():
    app.run(host='0.0.0.0', port=1177)

if __name__ == "__main__":
    main()