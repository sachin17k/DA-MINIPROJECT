from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/analyze', methods=['POST'])
def analyze():
    distance = float(request.form['distance'])
    expected = float(request.form['expected'])
    actual = float(request.form['actual'])

    delay = actual - expected
    status = "Delayed" if delay > 0 else "On-Time"

    return render_template("index.html", result=status)


if __name__ == "__main__":
    app.run(debug=True)