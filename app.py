from flask import Flask, jsonify, Response
from datetime import datetime
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUEST_COUNT = Counter(
    "app_requests_total",
    "Total number of requests"
)

@app.route("/")
def home():
    REQUEST_COUNT.inc()
    return "DevOps Project Running"

@app.route("/health")
def health():
    REQUEST_COUNT.inc()
    return jsonify({
        "status": "UP",
        "application": "devops-project",
        "timestamp": str(datetime.now())
    })

@app.route("/version")
def version():
    REQUEST_COUNT.inc()
    return jsonify({
        "version": "1.1.0",
        "environment": "production"
    })

@app.route("/metrics")
def metrics():
    return Response(
        generate_latest(),
        mimetype=CONTENT_TYPE_LATEST
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
