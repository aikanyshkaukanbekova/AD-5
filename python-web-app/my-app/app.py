from datetime import datetime
from flask import Flask
import os

app = Flask(__name__)

@app.route("/<name>")
def hello_world(name):
    return f"Привет, {name}"

@app.route("/env")
def env():
    return f"{os.environ['DATABASE_URL']}"

if __name__ == "__main__":
    app.run(host="0.0.0.0")