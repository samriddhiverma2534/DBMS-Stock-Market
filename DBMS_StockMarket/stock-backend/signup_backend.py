from flask import Flask, request, redirect, render_template, session
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Configure MySQL connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Sam@2534'
app.config['MYSQL_DB'] = 'stocks'

mysql = MySQL(app)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        captcha = request.form['captcha']

        if password != confirm_password:
            return "Passwords do not match"

        # ✅ Hash the password
        hashed_pw = generate_password_hash(password)

        # ✅ Store user in DB
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (name, phone, email, username, password) VALUES (%s, %s, %s, %s, %s)",
                    (name, phone, email, username, hashed_pw))
        mysql.connection.commit()
        cur.close()

        return redirect('/dashboard')  # Redirect after signup
    return render_template('signup.html')
