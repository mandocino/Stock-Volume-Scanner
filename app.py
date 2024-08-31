from flask import Flask, render_template, request, jsonify
import yfinance as yahooFinance
from datetime import datetime
import json
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('volumeSearchUSA.html')

@app.route('/volumeAnalyzeCA')
def volumeCAHomepage():
    return render_template('volumeSearchCA.html')

@app.route('/volumeAnalyzeUSA')
def volumeUSAHomepage():
    return render_template('volumeSearchUSA.html')

@app.route('/getVolumeCSE', methods=['GET'])
def get_volumeCSE():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d")
    data_dict = {}
    sendBackList = []
    with open('/home/mandoh/testdeploy/static/cse.txt', 'r') as file:
        for line in file:
            parts = line.strip().split(',')

            if len(parts) == 2:
                key, value = parts[0], parts[1]
                data_dict[key] = value

    for key in data_dict.items():
        try:
            stock_data = yahooFinance.download(key, period='1d', interval='1d', start=formatted_date, end=formatted_date)
            stock_data['relative volume'] = stock_data['Volume'] / \
            (stock_data['Volume'].rolling(40, min_periods=1).mean())
            if stock_data['relative volume'].iloc[-1] > 15:
                sendBackList.append(key)
        except Exception as e:
            print(f"Skipping {key} due to error: {e}")
    json_data = json.dumps(sendBackList)
    return jsonify(json_data)

@app.route('/getVolumeTSX', methods=['GET'])
def get_volumeTSX():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d")
    data_dict = {}
    sendBackList = []
    with open('/home/mandoh/testdeploy/static/tsv.csv', 'r') as file:
        for line in file:
            parts = line.strip().split(',')

            if len(parts) == 2:
                key, value = parts[0], parts[1]
                data_dict[key] = value

    for key in data_dict.items():
        try:
            stock_data = yahooFinance.download(key, period='1d', interval='1d', start=formatted_date, end=formatted_date)
            stock_data['relative volume'] = stock_data['Volume'] / \
            (stock_data['Volume'].rolling(40, min_periods=1).mean())
            if stock_data['relative volume'].iloc[-1] > 15:
                sendBackList.append(key)
        except Exception as e:
            print(f"Skipping {key} due to error: {e}")
    json_data = json.dumps(sendBackList)
    return jsonify(json_data)

@app.route('/getVolumeTSXV', methods=['GET'])
def get_volumeTSV():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d")
    data_dict = {}
    sendBackList = []
    with open('/home/mandoh/testdeploy/static/tsvx.csv', 'r') as file:
        for line in file:
            parts = line.strip().split(',')

            if len(parts) == 2:
                key, value = parts[0], parts[1]
                data_dict[key] = value

    for key in data_dict.items():
        try:
            stock_data = yahooFinance.download(key, period='1d', interval='1d', start=formatted_date, end=formatted_date)
            stock_data['relative volume'] = stock_data['Volume'] / \
            (stock_data['Volume'].rolling(40, min_periods=1).mean())
            if stock_data['relative volume'].iloc[-1] > 15:
                sendBackList.append(key)
        except Exception as e:
            print(f"Skipping {key} due to error: {e}")
    json_data = json.dumps(sendBackList)
    return jsonify(json_data)

@app.route('/getVolumeNYSE', methods=['GET'])
def get_volumeNYSE():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d")
    data_dict = {}
    sendBackList = []
    with open('/home/mandoh/testdeploy/static/nyse.csv', 'r') as file:
        for line in file:
            parts = line.strip().split(',')

            if len(parts) == 2:
                key, value = parts[0], parts[1]
                data_dict[key] = value

    for key, value in data_dict.items():
        try:
            if '^' not in key:
                stock_data = yahooFinance.download(key, period='1d', interval='1d', start=formatted_date, end=formatted_date)
                stock_data['relative volume'] = stock_data['Volume'] / \
                (stock_data['Volume'].rolling(40, min_periods=1).mean())
                if stock_data['relative volume'].iloc[-1] > 15:
                    sendBackList.append(key)
        except Exception as e:
            print(f"Skipping {key} due to error: {e}")

    json_data = json.dumps(sendBackList)
    return jsonify(json_data)

@app.route('/getVolumeNASDAQ', methods=['GET'])
def get_volumeNASDAQ():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d")
    data_dict = {}
    sendBackList = []
    with open('/home/mandoh/testdeploy/static/nasdaq.csv', 'r') as file:
        for line in file:
            parts = line.strip().split(',')

            if len(parts) == 2:
                key, value = parts[0], parts[1]
                data_dict[key] = value

    for key in data_dict.items():
        try:
            stock_data = yahooFinance.download(key, period='1d', interval='1d', start=formatted_date, end=formatted_date)
            stock_data['relative volume'] = stock_data['Volume'] / \
            (stock_data['Volume'].rolling(40, min_periods=1).mean())
            if stock_data['relative volume'].iloc[-1] > 15:
                sendBackList.append(key)
        except Exception as e:
            print(f"Skipping {key} due to error: {e}")
    json_data = json.dumps(sendBackList)
    return jsonify(json_data)

if __name__ == '__main__':
    app.run(debug=True)