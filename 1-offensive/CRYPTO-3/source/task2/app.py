from flask import Flask, render_template
from flag import flag
from Crypto.Util.number import *

flag = bytes_to_long(flag)
assert flag.bit_length() <= 180

app = Flask(__name__)

@app.route('/')
def source():
    return render_template('intro.html')

@app.route('/shared_flag')
def share():
    data = dict()
    data['alghorithm'] = "generate g, generate p, return pow(g,flag,p)"
    data['g'] = 2
    data['p'] = getPrime(1024)
    data['shared_flag'] = pow(data['g'], flag, data['p'])
    return data

def main():
    app.run(host='0.0.0.0', port=1176)

if __name__ == "__main__":
    main()
