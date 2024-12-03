from flask import Flask, request, jsonify
from client import chat, printd
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("API_KEY")

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def handle_chat():
    # check for auth bearer token
    if not request.headers.get("Authorization"):
        return jsonify({"error": "missing Authorization header"}), 401
    if request.headers.get("Authorization") != f"Bearer {API_KEY}":
        return jsonify({"error": "invalid Authorization header"}), 401

    # req_json = request.json
    printd(request.json)
    messages = request.json.get("messages")
    model = request.json.get("model")
    printd(type(messages))
    try:
        result = chat(messages, model)
        printd(result)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5001)
