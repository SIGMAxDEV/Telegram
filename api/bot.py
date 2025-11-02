import os
import requests
from flask import Flask, request

app = Flask(name)

TOKEN = os.environ.get("7200494679:AAH-W84VIBRVKnoZoSNHPIXkgNawCsjubxo")
URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

@app.route("/api/bot", methods=["POST", "GET"])
def bot():
    if request.method == "POST":
        data = request.get_json()
        if "message" in data:
            chat_id = data["message"]["chat"]["id"]
            text = data["message"].get("text", "")

            reply = "I’m alive on Vercel 🚀"
            if text == "/start":
                reply = "Hello Ayu! This bot is running on Vercel 🚀"

            requests.post(URL, json={"chat_id": chat_id, "text": reply})

        return "OK", 200
    else:
        return {"status": "Bot running fine!"}, 200
