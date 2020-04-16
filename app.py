from flask import render_template
from flask import Flask


app = Flask(__name__, static_folder="static", template_folder="templates")


@app.route("/")
def index():
    return render_template("render4.html")


if __name__ == "__main__":
    app.run()