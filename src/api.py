#!/usr/bin/env python
import ast
import base64
import matplotlib.pyplot as plt
from flask import Flask, request, render_template, jsonify, Response
from io import BytesIO


app = Flask(__name__)
labels = []
values = []


@app.route('/data')
def get_data_json():
    """Json data of labels and values
    """
    global labels, values
    hashtags_count = []
    for i in range(len(labels)):
        hashtags_count.append({'hashtag': labels[i], 'count': values[i]})
    print(hashtags_count)
    return jsonify(hashtags_count)


@app.route('/data-table')
def get_data_table() -> str:
    """Table with hashtag-count
    """
    global labels, values
    data_dict = {}
    for i in range(len(labels)):
        data_dict[labels[i]] = values[i]
    return render_template('table.html', result=data_dict)


@app.route('/data-live')
def get_data_live() -> str:
    """Live table with hashtag-count
    """
    global labels, values
    data_dict = {}
    for i in range(len(labels)):
        data_dict[labels[i]] = values[i]
    return render_template('table_live.html', result=data_dict)


@app.route('/chart')
def get_data_chart() -> str:
    """ggplot2 barchart with hashtag-count data
    """
    global labels, values
    img = BytesIO()
    plt.bar(labels,values)
    plt.xticks(rotation=80)
    plt.tight_layout()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    return render_template('plot.html', plot_url=plot_url)


@app.route('/chart-live')
def get_chart_live():
    """ggplot2 barchart with hashtag-count data live
    """
    return render_template('plot_live.html')


@app.route('/chartjs-live', methods=['GET'])
def stuff_chart():
    """chartjs barchart with hashtag-count data live, more beautiful than ggplot2
    """
    return render_template('plot_mychart.html')


@app.route('/update-data', methods=['POST'])
def update_data():
    """Endpoint called by Spark client to update data
    """
    global labels, values
    if not request.form or 'data' not in request.form:
        return "error", 400
    labels = ast.literal_eval(request.form['label'])
    values = ast.literal_eval(request.form['data'])
    print("labels received: " + str(labels))
    print("data received: " + str(values))
    return "success", 201


if __name__ == "__main__":
    app.run(host='localhost', port=3000)
