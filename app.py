from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return "DevOps Project Running"

@app.route("/health")
def health():
    return jsonify({
        "status": "UP",
        "application": "devops-project",
        "timestamp": str(datetime.now())
    })

@app.route("/version")
def version():
    return jsonify({
        "version": "1.0.0",
        "environment": "local"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
