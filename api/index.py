from flask import Flask, render_template, redirect, url_for, session, request, send_file
import os
import requests
from random import SystemRandom

CLID = "1163179429640544267"
re_uri = "https%3A%2F%2Fchronicbot.xyz%2Fcallback"
base = "https://discord.com/api"
BSEC = os.environ.get("BOT_TOKEN")

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("FLASK_SECRET_KEY")
app.config["TESTING"] = True

@app.route("/")
def index():
    return render_template("main.html")

@app.route("/login")
def login():
    if "token" in session:
        return redirect(url_for("dash"))
    state = generate_token()
    url = f"https://discord.com/oauth2/authorize?response_type=code&client_id={CLID}&scope=identify%20guilds%20guilds.members.read&state={state}&redirect_uri={re_uri}&prompt=consent"
    return redirect(url)

@app.route("/callback")
def callback():
    session["code"] = request.args.get("code")
    session["token"] = r["access_token"]
    session.pop("code")
    return f"Your code is {session["code"]}"
