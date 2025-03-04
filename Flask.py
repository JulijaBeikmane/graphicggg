from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/sveiki")
def sveiki():
    return "<h2>Sveiki!<h2>"

if __name__ == "__main__":
    app.run()
