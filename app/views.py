from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps
import models

app = Flask(__name__)



# Register Form Class
class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')

# Shoppinglist Form Class
class ShoppinglistForm(Form):
    title = StringField('Title', [validators.Length(min=1, max=200)])
    

    # Index
@app.route('/')
def index():
    return render_template('home.html')

# About
@app.route('/about')
def about():
    return render_template('about.html')


# User Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))

        flash('You are now registered and can log in', 'success')

        return redirect(url_for('login'))
    return render_template('register.html', form=form)


# User login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get Form Fields
        username = request.form['username']
        password_candidate = request.form['password']

        # Compare Passwords
        if sha256_crypt.verify(password_candidate, request.form['password']):
            # Passed
            session['logged_in'] = True
            session['username'] = username

            flash('You are now logged in', 'success')
            return redirect(url_for('dashboard'))
        else:
            error = 'Invalid login'
            return render_template('login.html', error=error)
    else:
        error = 'Username not found'
        return render_template('login.html', error=error)

# Check if user logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('login'))
    return wrap

# Dashboard
@app.route('/dashboard')
@is_logged_in
def dashboard():
    # Create cursor
    cur = {}

    shoppinglists = cur.view_shoppinglist()

    if len(cur) > 0:
        return render_template('dashboard.html', shoppinglists=shoppinglists)
    else:
        msg = 'No Shoppinglists Found'
        return render_template('dashboard.html', msg=msg)

# Add shoppinglist
@app.route('/add_shoppinglist', methods=['GET', 'POST'])
@is_logged_in
def add_shoppinglist():
    form = ShoppinglistForm(request.form)
    if request.method == 'POST' and form.validate():
        title = form.title.data
     
        # Create Cursor
        cur ={}
        cur.add_shoppinglist()

        flash('Shoppinglist Created', 'success')

        return redirect(url_for('dashboard'))

    return render_template('add_article.html', form=form)

@app.route('/edit_shoppinglist/<string:id>', methods=['GET', 'POST'])
@is_logged_in
def edit_shoppinglist(id):
    # Create cursor
    cur = {}
    cur.view_shoppinglist(id)
    # Get form
    form = ShoppinglistForm(request.form)

    # Populate shoppinglist form fields
    form.title.data = shoppinglist['title']
    
    if request.method == 'POST' and form.validate():
        title = request.form['title']

        # Create Cursor
        cur.edit_shoppinglist(id)
        
        flash('Shoppinglist Updated', 'success')

        return redirect(url_for('dashboard'))

    return render_template('edit_shoppinglist.html', form=form)

# Delete shoppinglist
@app.route('/delete_shoppinglist/<string:id>', methods=['POST'])
@is_logged_in
def delete_shoppinglist(id):
    # Create cursor
    cur = {}
    # Execute
    cur.delete_shoppinglist(id)

    flash('Article Deleted', 'success')

    return redirect(url_for('dashboard'))














# Logout
@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.secret_key='secret123'
    app.run(debug=True)