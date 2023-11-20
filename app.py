from flask import Flask, render_template, url_for, flash, redirect, request, jsonify
import json
import pandas as pd
import numpy as np
import joblib
from pred import model



app = Flask(__name__)


@app.route("/")
@app.route("/home")


def home():
    return render_template("layout.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from the POST request
        data = request.get_json()

        # print(data)

        prediction = model(data)
        # prediction = "working"

        return jsonify({'prediction': str(prediction)})
    except Exception as e:
        return jsonify({'error': str(e)})


# if __name__ == '__main__':
#     app.run(debug=True)