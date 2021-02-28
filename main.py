import requests


API_KEY = 'ed9a246f20d729a60135881f5e0d6b16'
symbol = requests.get('http://api.marketstack.com/v1/eod?symbols=symbol&access_key=' + API_KEY)
response = requests.get('http://api.marketstack.com/v1/eod?symbols=' + symbol +'&access_key' + API_KEY)
api_response = response.json()
r = requests.post("" , data = api_response)