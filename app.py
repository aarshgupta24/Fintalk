import yfinance as yf
from flask import request , render_template , jsonify , Flask
from flask_cors import CORS

app = Flask(__name__ , template_folder='templates')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_stock_data' , methods=['POST'])
@cross_origin(supports_credentials=True) 

def get_stock_data():
    ticker = request.get_json()['ticker']
    data = yf.Ticker(ticker).history(period='1y')
    return jsonify({'currentPrice': data.iloc[-1].Close , 'openPrice': data.iloc[-1].Open})


if __name__ == '__main__':
    app.run(debug=True)

