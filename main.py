from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Replace these with your actual Chatbase values
CHATBASE_API_KEY = "your_chatbase_api_key"
CHATBOT_ID = "your_chatbot_id"

@app.route("/")
def index():
    return "✅ Chatbase cataloging backend is running."

@app.route("/ask-chatbase", methods=["POST"])
def ask_chatbase():
    data = request.get_json()
    user_text = data.get("text", "")

    if not user_text:
        return jsonify({"error": "No text provided"}), 400

    payload = {
        "chatbot_id": CHATBOT_ID,
        "messages": [
            { "role": "user", "content": user_text }
        ]
    }

    headers = {
        "Authorization": f"Bearer {CHATBASE_API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post("https://www.chatbase.co/api/v1/chat", headers=headers, json=payload)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
