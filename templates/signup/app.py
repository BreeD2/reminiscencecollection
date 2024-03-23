from flask import Flask, request, redirect, url_for, render_template
from werkzeug.security import generate_password_hash
import psycopg2

app = Flask(__name__)

# Assuming you've configured your database connection here
conn = psycopg2.connect(
    dbname="yourdbname", user="yourdbuser", password="yourdbpassword", host="localhost"
)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        raw_password = request.form['password']
        hashed_password = generate_password_hash(raw_password)

        # Add user to the database
        cur = conn.cursor()
        cur.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", 
                    (username, email, hashed_password))
        conn.commit()
        cur.close()
        
        return redirect(url_for('login'))
    return render_template('signup/index.html')
