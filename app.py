from flask import Flask, render_template
from pip import main
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

@app.route("/")
def hello_world():
    # return "<p>Hello, World!</p>"
    return render_template("index.html")
@app.route("/products")
def products():
    return "<p>This is Products Page</p>"

if __name__ == "__main__":
    app.run(debug=True)