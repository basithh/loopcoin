from flask import Flask,render_template,request
import requests

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        first = request.form['from']
        second = request.form['to']
        r = requests.get(url=f'https://rest.coinapi.io/v1/exchangerate/{first}/{second}',headers = {"X-CoinAPI-Key": "8BCD2B74-AF33-482D-AD86-C58C41E18968"}).json()
        return render_template('result.html',rate= r['rate'])
    return render_template('index.html')

if __name__=='__main__':
    app.run()