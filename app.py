from flask import Flask, render_template, url_for, flash, redirect
from models import db, User  # Make sure these imports are correct based on your project structure
from forms import LoginForm, RegistrationForm  # Adjust if using different names

app = Flask(__name__)
app.config['SECRET_KEY'] = '\x16vJ\x8c\x0ecg\xe7$\x0e\x8b\xd6\xab\x9b-['
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db.init_app(app)

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    # Adjust the template path here
    return render_template('signup/index.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            # Logic for successful login
            flash('You have been logged in!', 'success')
            return redirect(url_for('index'))  # Adjust as needed
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    # Adjust the template path here
    return render_template('login/index.html', title='Login', form=form)
