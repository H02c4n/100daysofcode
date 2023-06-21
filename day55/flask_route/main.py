from flask import Flask

app = Flask(__name__)


def make_bold(fn):
    def wrapper():
        return "<b>" + fn() + "</b>"

    return wrapper


def make_emphasis(fn):
    def wrapper():
        return "<em>" + fn() + "</em>"
    return wrapper

def make_underline(fn):
    def wrapper():
        return "<u>" + fn() + "</u>"
    return wrapper


@app.route("/")
def hello():
    return "<p>Hello World</p>"


@app.route("/hi")
@make_bold
@make_emphasis
@make_underline
def hi():
    return "<p>Hi</p>"


@app.route("/name/<path:ad>/<int:yas>")
def greet(ad, yas):
    return f"{ad} is {yas} years old."


if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True)
