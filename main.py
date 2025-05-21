from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

API_KEY = "bc07e328-2243-4774-9b0c-431df865af7e"
BOT_ID = "rSb7GdUSjw1kxi8igKkib"

@app.route('/send', methods=['POST'])
def send_to_chatbase():
    data = request.json
    message = data.get("message", "")

    if not message:
        return jsonify({"error": "No message provided"}), 400

    payload = {
        "chatbot_id": BOT_ID,
        "messages": [
            { "role": "user", "content": message }
        ]
    }

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post("https://www.chatbase.co/api/v1/chat", headers=headers, json=payload)
    return jsonify(response.json()), response.status_code

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
