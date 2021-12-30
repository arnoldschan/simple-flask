from flask import Flask
import requests

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Welcome to Docker Tutorial"


@app.route("/network")
def read_text():
    text = requests.get("http://text:5000/read").text
    return f"READ THROUGH NETWORK: {text}"


@app.route("/volume")
def read_text():
    with open("/text_dir/text.txt", "r") as file:
        text = file.read()
    return f"READ THROUGH VOLUME: {text}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
