from flask import Flask,render_template
from flask_bootstrap import Bootstrap
import urllib2


app = Flask(__name__)
Bootstrap(app)

@app.route('/weather')
def hello_world():
    urlCurrent = 'http://api.openweathermap.org/data/2.5/weather?id=2643743&appid=30b0e4a13dcb98a91143652520f8f108'
    r = urllib2.urlopen(urlCurrent).read()
    str(r).replace('3h', 'h')
    print r;
    return render_template('weather.html')

@app.route('/stocks')
def Stocks():
    return render_template('stocks.html')

@app.route('/date')
def datetime():
    return render_template('date.html')


if __name__ == "__main__":
    app.run(debug=True)