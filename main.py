from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

openai.api_key = "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"

@app.route('/')
def index():
    return "✅ OpenAI GPT PDF backend is running."

@app.route('/ask-gpt', methods=['POST'])
def ask_gpt():
    data = request.get_json()
    user_text = data.get('text', '')

    if not user_text:
        return jsonify({'error': 'No text provided'}), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant who catalogs and analyzes book metadata from extracted PDF text."},
                {"role": "user", "content": user_text}
            ]
        )
        answer = response.choices[0].message["content"]
        return jsonify({'response': answer})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
