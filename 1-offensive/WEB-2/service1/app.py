from flask import Flask, redirect, url_for, request, render_template
import os
import socket
import time
from flask_login import LoginManager, current_user, login_user, logout_user

from user import User

app = Flask(__name__)

app.config["SECRET_KEY"] = os.getrandom(64)
FLAG = os.environ.get("FLAG", "flag{flag}")


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "main"

@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(user_id)


@app.route("/login", methods=["GET", "POST"])
def login():
    if hasattr(current_user, "username"):
        return redirect(url_for("main"))
    if request.method == "GET":
        return render_template("login.html")
    username = request.form.get("username", "")
    password = request.form.get("password", "")

    if not (username or password):
        return "Empty"

    user = User.auth(username, password)
    
    if not user:
        return redirect(url_for("login"))

    login_user(user)
    return redirect(url_for("main"))

@app.route("/register", methods=["GET", "POST"])
def register():
    if hasattr(current_user, "username"):
        return redirect(url_for("main"))
    if request.method == "GET":
        return render_template("register.html")
    username = request.form.get("username", "")
    password = request.form.get("password", "")

    if not (username or password):
        return redirect(url_for("register"))

    user = User.register(username, password)
    
    if not user:
        return redirect(url_for("register"))

    login_user(user)
    return redirect(url_for("main"))

@app.route("/logout", methods=["GET"])
def logout():
    logout_user()
    return redirect("/login")

def make_request(username):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("service2", 3001))
    sock.settimeout(1)
    
    payload = f"""GET / HTTP/1.1\r\nHost: 0.0.0.0:3001\r\nCookie: username={username};flag={FLAG}\r\n\r\n"""
    sock.send(payload.encode())
    time.sleep(.3)
    try:
        data = sock.recv(4096)
        body = data.split(b"\r\n\r\n", 1)[1].decode()
    except (IndexError, TimeoutError) as e:
        print(e)
        body = str(e)
    return body
    

@app.route("/")
def main():
    if not hasattr(current_user, "username"):
        return redirect(url_for("login"))
    res = make_request(current_user.username)
    return render_template("index.html", contents=res, username=current_user.username)
