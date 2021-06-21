from flask import Flask,render_template,request
import requests

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    abc = requests.get("https://news.google.com/rss/search?q=cryptocurrency")
    final = xmltodict.parse(abc.text) 
    news = []
    news_brand = []

    for i in final['rss']['channel']['item']:
        slit = i['title'].split(' - ')
        news.append(slit[0])
        news_brand.append(slit[1])
        news_a = []
    news = news[:10]
    for i in news:
        news_a.append({
        'news':i,
        })
    if request.method == 'POST':
        first = request.form['from']
        second = request.form['to']
        r = requests.get(url=f'https://rest.coinapi.io/v1/exchangerate/{first}/{second}',headers = {"X-CoinAPI-Key": "8BCD2B74-AF33-482D-AD86-C58C41E18968"}).json()
        return render_template('result.html',rate= r['rate'],newf=news_a)
    return render_template('index.html',newf=news_a)

if __name__=='__main__':
    app.run()
