from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route("/api/doncay", methods=["GET"])
def get_doncay():
    with open("doncay.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == "__main__":
    app.run(port=5000)
