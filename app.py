"""
Simple "Hello, World" application using Flask
"""

from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')
    # return 'Hello World!'

@app.route("/MBTAHelper/", methods=["GET", "POST"])
def MBTAHelper():
    if request.method == "POST":
        location = str(request.form["location"])

        if location:
            return render_template(
                "mbta_result.html", location = 'Boston')
        else:
            # return render_template("calculator_form.html", error=True)
            return 'ERROR!'
    # return render_template("calculator_form.html", error=None)
    return 'GET ERROR!'