from flask import Flask, jsonify
import time

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return jsonify({"result": a + b})


if __name__ == "__main__":
    print("Hello World!", flush=True)
    time.sleep(300)
    app.run(host="0.0.0.0", port=5000)
