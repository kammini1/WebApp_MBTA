"""
Simple "Hello, World" application using Flask
"""

from flask import Flask, render_template, request
from flask import render_template
from flask import request

from mbta_helper import find_stop_near

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route("/MBTAHelper/", methods=["GET", "POST"])
def MBTAHelper():
    if request.method == "POST":
        location = str(request.form["location"])
        MBTA_Station = find_stop_near(location)

        if MBTA_Station:
            return render_template("mbta_result.html")
        else:
            # return render_template("calculator_form.html", error=True)
            return 'ERROR!'
    # return render_template("calculator_form.html", error=None)
    return 'GET ERROR!'