#!/usr/bin/env python
import ast
import base64
import matplotlib.pyplot as plt
from flask import Flask, request, render_template, jsonify, Response
from io import BytesIO


app = Flask(__name__)
polarities = []
timestamps = []


@app.route('/data')
def get_data_json():
    """Json data of labels and values
    """
    global polarities, timestamps
    polarities_timestamps = []
    for i in range(len(polarities)):
        if (i == 0):
            delta = polarities[i]
        else:
            delta = polarities[i] - polarities[i-1]
        polarities_timestamps.append({'polarity': polarities[i], 'timestamp': timestamps[i], 'delta':delta})
    print(polarities_timestamps)
    return jsonify(polarities_timestamps)


@app.route('/polarity-live', methods=['GET'])
def polarity_waterfall():
    """chartjs barchart with hashtag-count data live, more beautiful than ggplot2
    """
    return render_template('waterfall_plot.html')


@app.route('/update-polarity', methods=['POST'])
def update_data():
    """Endpoint called by Spark client to update polarity
    """
    global polarities, timestamps
    if not request.form or 'polarity' not in request.form:
        return "No polarity in body", 400
    polarity = float(request.form['polarity'])
    timestamp = request.form['timestamp']
    print("polarity received: " + str(polarity))
    print("timestamp received: " + timestamp)
    polarities.append(polarity)
    timestamps.append(timestamp)
    return "success", 201


if __name__ == "__main__":
    app.run(host='localhost', port=3000)
