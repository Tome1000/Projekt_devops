import os
from flask import Flask, jsonify

app = Flask(__name__)

# odczyt sekretu z GitHub Secrets / środowiska
secret_key = os.getenv("SECRET_KEY")

@app.route("/")
def home():
    return jsonify({"status": "ok", "secret_key": secret_key})

@app.route("/products")
def products():
    return jsonify([
        {"id": 1, "name": "Laptop"},
        {"id": 2, "name": "Phone"}
    ])

if __name__ == "__main__":
    app.run()
