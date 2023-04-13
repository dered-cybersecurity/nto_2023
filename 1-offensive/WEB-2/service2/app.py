from flask import Flask, request
import os

app = Flask(__name__)
FLAG = os.environ.get("FLAG", "flag{flag}")

@app.route("/")
def main():
    flag = request.cookies.get("flag")
    username = request.cookies.get("username")
    if FLAG == flag:
        return f"Hello, {username}"
    else:
        return f"I don't trust you!"
