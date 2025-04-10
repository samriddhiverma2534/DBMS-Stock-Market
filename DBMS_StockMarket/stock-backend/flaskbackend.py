from flask import Flask, request, jsonify, session
from flask_cors import CORS
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'
CORS(app, supports_credentials=True)

# MySQL config
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''  # 🔒 Set your actual password here
app.config['MYSQL_DB'] = 'stock_app'

mysql = MySQL(app)

# ----------------- AUTH ROUTES -----------------

# ✅ Signup
@app.route('/api/signup', methods=['POST'])
def signup():
    data = request.get_json()
    name = data.get('name')
    phone = data.get('phone')
    email = data.get('email')
    password = generate_password_hash(data.get('password'))

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO users (name, phone, email, password) VALUES (%s, %s, %s, %s)",
                (name, phone, email, password))
    mysql.connection.commit()
    cur.close()
    return jsonify({"message": "User registered successfully"}), 201

# ✅ Login
@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE email = %s", (email,))
    user = cur.fetchone()
    cur.close()

    if user and check_password_hash(user[4], password):
        session['user_id'] = user[0]
        session['user_name'] = user[1]
        return jsonify({"message": "Login successful", "name": user[1]}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401

# ✅ Logout
@app.route('/api/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({"message": "Logged out successfully"}), 200

# ✅ Get logged in user
@app.route('/api/user', methods=['GET'])
def get_user():
    if 'user_id' in session:
        return jsonify({"id": session['user_id'], "name": session['user_name']}), 200
    return jsonify({"error": "Not logged in"}), 401

# ----------------- STOCK ROUTES -----------------

# ✅ Add Stock
@app.route('/api/stocks', methods=['POST'])
def add_stock():
    data = request.get_json()
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO stocks (symbol, company_name, price, volume, last_updated) VALUES (%s, %s, %s, %s, %s)",
                (data['symbol'], data['company_name'], data['price'], data['volume'], datetime.datetime.now()))
    mysql.connection.commit()
    cur.close()
    return jsonify({"message": "Stock added successfully"}), 201

# ✅ Get all stocks
@app.route('/api/stocks', methods=['GET'])
def get_stocks():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM stocks")
    stocks = cur.fetchall()
    cur.close()
    return jsonify(stocks), 200

# ----------------- WATCHLIST ROUTES -----------------

# ✅ Add to Watchlist
@app.route('/api/watchlist', methods=['POST'])
def add_watchlist():
    data = request.get_json()
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"error": "Unauthorized"}), 403

    stock_id = data['stock_id']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO watchlist (user_id, stock_id) VALUES (%s, %s)", (user_id, stock_id))
    mysql.connection.commit()
    cur.close()
    return jsonify({"message": "Stock added to watchlist"}), 201

# ✅ Get Watchlist
@app.route('/api/watchlist', methods=['GET'])
def get_watchlist():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"error": "Unauthorized"}), 403

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM watchlist WHERE user_id = %s", (user_id,))
    data = cur.fetchall()
    cur.close()
    return jsonify(data), 200

# ----------------- PORTFOLIO ROUTES -----------------

# ✅ Add to Portfolio
@app.route('/api/portfolio', methods=['POST'])
def add_portfolio():
    data = request.get_json()
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"error": "Unauthorized"}), 403

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO portfolio (user_id, stock_id, quantity, average_price) VALUES (%s, %s, %s, %s)",
                (user_id, data['stock_id'], data['quantity'], data['average_price']))
    mysql.connection.commit()
    cur.close()
    return jsonify({"message": "Stock added to portfolio"}), 201

# ✅ Get Portfolio
@app.route('/api/portfolio', methods=['GET'])
def get_portfolio():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"error": "Unauthorized"}), 403

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM portfolio WHERE user_id = %s", (user_id,))
    data = cur.fetchall()
    cur.close()
    return jsonify(data), 200
# ✅ Update User Settings
@app.route('/api/update_settings', methods=['POST'])
def update_settings():
    data = request.get_json()
    user_id = session.get('user_id')
    
    if not user_id:
        return jsonify({"error": "Unauthorized"}), 403

    username = data.get('username')
    password = data.get('password')  # Optional
    email = data.get('email')
    mobile = data.get('mobile')

    cur = mysql.connection.cursor()

    if password:
        hashed_password = generate_password_hash(password)
        cur.execute("UPDATE users SET name=%s, password=%s, email=%s, phone=%s WHERE id=%s",
                    (username, hashed_password, email, mobile, user_id))
    else:
        cur.execute("UPDATE users SET name=%s, email=%s, phone=%s WHERE id=%s",
                    (username, email, mobile, user_id))

    mysql.connection.commit()
    cur.close()

    # Update session data if username changes
    session['user_name'] = username

    return jsonify({'message': 'Settings updated successfully'}), 200

# ✅ Raise a Concern
@app.route('/api/raise_concern', methods=['POST'])
def raise_concern():
    data = request.get_json()
    user_id = session.get('user_id')

    if not user_id:
        return jsonify({"error": "Unauthorized"}), 403

    concern = data.get('concern')

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO concerns (user_id, concern_text) VALUES (%s, %s)", (user_id, concern))
    mysql.connection.commit()
    cur.close()

    return jsonify({'message': 'Concern submitted'}), 200

# ----------------- RUN SERVER -----------------
@app.route('/')
def home():
    return "Welcome to Stock App Backend!"
if __name__ == '__main__':
    app.run(debug=True)
