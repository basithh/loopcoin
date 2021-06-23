from flask import Flask,render_template,request
from requests import Request, Session, get
import json
import xmltodict

app = Flask(__name__, static_url_path='/static')

@app.route('/',methods=['GET','POST'])
def index():
    abc = get("https://news.google.com/rss/search?q=cryptocurrency")
    final = xmltodict.parse(abc.text) 
    news = []
    news_brand = []

    for i in final['rss']['channel']['item']:
        slit = i['title'].split(' - ')
        news.append(slit[0])
        news_brand.append(slit[1])
        news_a = []
    news = news[:10]
    for i,j in zip(news,news_brand):
        news_a.append({
        'news':i,
        'brand':j
        })
    print(news_a)
    return render_template('index.html',newf=news_a)

@app.route('/value/<string:x>/<string:y>/<int:z>')
def rec78(x,y,z):
    value = z
    first = x
    second = y
    url = 'https://pro-api.coinmarketcap.com/v1/tools/price-conversion'
    parameters = {
        'amount':str(value),
        'symbol':str(first),
        'convert':str(second)
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '08c9e994-6db7-42c7-8bfe-478ffe17fa82',
     }

    session = Session()
    session.headers.update(headers)
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    return str(data['data']['quote'][str(second)]['price'])

@app.route('/table')
def reg():
     #This example uses Python 2.7 and the python-request library.
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
    'start':'1',
    'limit':'5000',
    'convert':'INR'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '08c9e994-6db7-42c7-8bfe-478ffe17fa82',
    }

    session = Session()
    session.headers.update(headers)
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    return render_template('dd.html' , data = data['data'])

if __name__=='__main__':
    app.run()
