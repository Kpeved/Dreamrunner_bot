from flask import Flask, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
TOKEN = os.getenv("TELEGRAM_TOKEN")
URL = f"https://api.telegram.org/bot{TOKEN}/"

def send_message(chat_id, text):
    url = URL + "sendMessage"
    data = {"chat_id": chat_id, "text": text}
    requests.post(url, data=data)

@app.route('/<token>', methods=['POST'])
def respond(token):
    if token != TOKEN:
        return "Unauthorized", 403

    update = request.get_json()
    chat_id = update["message"]["chat"]["id"]
    text = "Hello Bot"
    
    send_message(chat_id, text)
    
    return "Success", 200

if __name__ == '__main__':
    app.run(threaded=True)
