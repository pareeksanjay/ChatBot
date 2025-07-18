from flask import Flask, request, jsonify,send_from_directory
import requests

app = Flask(__name__)

PERPLEXITY_API_KEY = "<>"
PERPLEXITY_API_URL = "https://api.perplexity.ai/chat/completions"
@app.route('/')
def index():
    return send_from_directory('static', 'index.html')
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    payload = {
        "model": "sonar-pro",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message}
        ]
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": f"Bearer {PERPLEXITY_API_KEY}"
    }
    api_response = requests.post(PERPLEXITY_API_URL, headers=headers, json=payload)
    bot_reply = api_response.json()['choices'][0]['message']['content']
    return jsonify({'reply': bot_reply})

if __name__ == '__main__':
    app.run(debug=True)
