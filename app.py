from flask import Flask, render_template, request, jsonify
from config import RESPONSES

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json() or {}
    message = data.get("message", "").strip().lower()

    if not message:
        return jsonify({"reply": "Please type a question."})

    reply = RESPONSES["default"]
    for keyword, answer in RESPONSES.items():
        if keyword != "default" and keyword in message:
            reply = answer
            break

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
