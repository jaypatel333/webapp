import os
from flask import Flask, render_template, request

__author__ = 'jay'

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("materialize.html")

	

if __name__ == "__main__":
    app.run(port=4550, debug=True)