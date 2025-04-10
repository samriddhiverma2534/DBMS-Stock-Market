from flask import Flask, request, jsonify
from flask_cors import CORS
import yfinance as yf

app = Flask(__name__)
CORS(app)  # To allow frontend to access the API

@app.route('/get-stock-data', methods=['GET'])
def get_stock_data():
    symbol = request.args.get('symbol')
    if not symbol:
        return jsonify({"error": "Missing symbol parameter"}), 400

    try:
        stock = yf.Ticker(f"{symbol}.NS")  # NSE stocks have `.NS` suffix
        hist = stock.history(period="1d", interval="5m")  # You can customize this

        # Prepare data
        data = {
            "symbol": symbol,
            "timestamps": hist.index.strftime('%H:%M').tolist(),
            "prices": hist['Close'].fillna(method='ffill').tolist()
        }
        return jsonify(data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
