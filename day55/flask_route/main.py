from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "<p>Hello World</p>"


@app.route("/hi")
def hi():
    return "<p>Hi</p>"


@app.route("/name/<path:ad>/<int:yas>")
def greet(ad, yas):
    return f"{ad} is {yas} years old."


if __name__ == "__main__":
    app.run(debug=True)
