import os
import requests
from flask import Flask, request, jsonify

app = Flask(name)

TOKEN = os.environ.get("BOT_TOKEN")
if not TOKEN:
    raise ValueError("BOT_TOKEN not found in environment variables!")

URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"


@app.route("/api/bot", methods=["GET"])
def home():
    return jsonify({"status": "Bot running successfully 🚀"}), 200


@app.route("/api/bot", methods=["POST"])
def webhook():
    data = request.get_json()
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        if text == "/start":
            reply = "Hello Ayu! This bot is running on Vercel 🚀"
        else:
            reply = "I’m alive on Vercel ⚡"

        requests.post(URL, json={"chat_id": chat_id, "text": reply})

    return "OK", 200
