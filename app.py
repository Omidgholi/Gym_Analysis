from flask import Flask, render_template, request, send_file
import os

import statistics

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    venue = request.form["venue"]
    start_date = request.form["start_date"]
    end_date = request.form["end_date"]

    if start_date == "":
        start_date = None
    if end_date == "":
        end_date = None

    statistics.gym_analysis(venue, start_date, end_date)
    return send_file("output/graph.png", mimetype='image/png')

if __name__ == "__main__":
    app.run(debug=True)
