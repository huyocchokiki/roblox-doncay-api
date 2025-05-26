from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

@app.route("/api/doncay", methods=["GET"])
def get_doncay():
    with open("doncay.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render sẽ cung cấp PORT qua biến môi trường
    app.run(host="0.0.0.0", port=port)

