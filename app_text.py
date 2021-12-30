from flask import Flask
from flask import request


app = Flask(__name__)


@app.route("/read")
def read_text():
    with open("/text_dir/text.txt", "r") as file:
        return file.read()


@app.route("/write")
def write_text():
    with open("/text_dir/text.txt", "w") as file:
        text = request.args.get("text")
        file.write(text)
    return text


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
