from flask import Flask
import requests
import os
from dotenv import load_dotenv
app = Flask(__name__)

TOKEN = os.getenv("TELEGRAM_TOKEN")
URL = f"https://api.telegram.org/bot{TOKEN}/"

@app.route('/')
def hello_world():
    return 'Hello from Koyeb'

@app.route('/webhook', methods=['POST'])
def receive_update():
    # Telegram sends updates using POST
    update = request.get_json()
    chat_id = update['message']['chat']['id']
    text = update['message']['text']
    
    # Logic to respond to the message
    send_message(chat_id, "Received your message: " + text)
    return 'OK', 200

def send_message(chat_id, text):
    url = f"{TELEGRAM_API_URL}/sendMessage"
    data = {'chat_id': chat_id, 'text': text}
    requests.post(url, data=data)

if __name__ == "__main__":
    app.run()
