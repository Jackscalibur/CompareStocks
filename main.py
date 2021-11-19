from urllib import request
from flask import Flask
import requests

app = Flask(__name__)

@app.route('/stockData', methods=['GET'])
def stockData():
    symbols = request.args('symbols')
    return requests.get('http://api.marketstack.com/v1/eod?AAPL=' + symbols + '&access_key=' + '6bac9f78caf133f0f7a5341fbc222afa')


@app.route('/searchStocks', methods=['GET'])
def searchStock():
    search = request.args('search')
    return requests.get('http://api.marketstack.com/v1/tickers?search=' + input + '&access_key=' + '6bac9f78caf133f0f7a5341fbc222afa')


if __name__ == '__main__':
    app.run()
