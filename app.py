
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/python")
def python_page():
    return render_template(
        "index.html",
        active_section="python"
    )


@app.route("/docker")
def docker_page():
    return render_template(
        "index.html",
        active_section="docker"
    )


@app.route("/aws")
def aws_page():
    return render_template(
        "index.html",
        active_section="aws"
    )


@app.route("/about")
def about_page():
    return render_template(
        "index.html",
        active_section="about"
    )


@app.route("/health")
def health():
    return {"status": "healthy"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
