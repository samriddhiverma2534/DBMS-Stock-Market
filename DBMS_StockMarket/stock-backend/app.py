from flask import Flask, jsonify, request, session
from flask_cors import CORS
import yfinance as yf
import mysql.connector
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

app = Flask(__name__)
CORS(app)
app.secret_key = 'your_secret_key'

# ✅ Connect to MySQL using correct DB name
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sam@2534",
    database="stocks"  # Corrected DB name
)
cursor = conn.cursor(dictionary=True)

# 📊 Chart Data API
@app.route('/api/chart-data/<symbol>')
def chart_data(symbol):
    stock = yf.Ticker(f"{symbol}.NS")
    hist = stock.history(period="1mo", interval="1d")

    if hist.empty:
        return jsonify({"error": "No data found"}), 404

    data = {
        "dates": hist.index.strftime('%Y-%m-%d').tolist(),
        "close": hist['Close'].tolist(),
        "volume": hist['Volume'].tolist()
    }
    return jsonify(data)

# 📋 Get all available stocks
@app.route('/api/stocks')
def get_stocks():
    cursor.execute("SELECT * FROM stocks")
    stocks = cursor.fetchall()
    return jsonify(stocks)

# 📁 Get portfolio for a user
@app.route('/api/portfolio/<username>')
def get_portfolio(username):
    try:
        cursor.execute("SELECT * FROM portfolio WHERE user_id=%s", (username,))
        data = cursor.fetchall()
        if not data:
            return jsonify({"message": f"No portfolio found for user '{username}'"}), 404
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 🔖 Get watchlist for a user
@app.route('/api/watchlist/<username>')
def get_watchlist(username):
    try:
        cursor.execute("SELECT * FROM watchlist WHERE user_id=%s", (username,))
        data = cursor.fetchall()
        if not data:
            return jsonify({"message": f"No watchlist found for user '{username}'"}), 404
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 🤖 AI Chatbot
@app.route('/api/chatbot', methods=['POST'])
def chatbot():
    data = request.get_json()
    username = data.get("username")
    symbol = data.get("symbol")

    if not symbol:
        return jsonify({"error": "Stock symbol is required"}), 400

    try:
        stock = yf.Ticker(f"{symbol}.NS")
        hist = stock.history(period="1mo", interval="1d")

        if hist.empty or len(hist) < 5:
            return jsonify({"error": "Not enough data to predict"}), 400

        hist = hist.reset_index()
        hist['Day'] = np.arange(len(hist))
        X = hist[['Day']]
        y = hist['Close']

        model = LinearRegression()
        model.fit(X, y)
        next_day = [[len(hist)]]
        predicted_price = model.predict(next_day)[0]

        greeting = f"Hi {username}, 👋 I'm your stock assistant!"
        questions = [
            "📊 What stock are you most interested in today?",
            "📈 Are you looking to invest short term or long term?",
            "💰 What's your risk appetite? Low, Medium or High?",
            "🕐 Are you planning to buy today or just monitoring?",
            "📌 Want me to track this stock daily for you?"
        ]

        return jsonify({
            "greeting": greeting,
            "questions": questions,
            "predicted_price": f"₹{predicted_price:.2f}"
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 🚀 Start Flask Server
if __name__ == '__main__':
    print("Flask server is running...")
    app.run(debug=True)
