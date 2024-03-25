@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        input_password = request.form['password']

        cur = conn.cursor()
        cur.execute("SELECT password FROM users WHERE username = %s", (username,))
        user_password = cur.fetchone()
        cur.close()
        
        if user_password and check_password_hash(user_password[0], input_password):
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            return 'Invalid credentials'
    return render_template('login/index.html')
