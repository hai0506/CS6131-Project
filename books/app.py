from flask import Flask, flash, redirect, url_for, render_template, request, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
from werkzeug.security import check_password_hash, generate_password_hash


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'issl3'

# Intialize MySQL
mysql = MySQL(app)

# Change the value of SECRET_KEY to a long random string.
app.secret_key = 'issl3'

@app.route('/')
def home():
    # Check if user is loggedin
    if 'loggedin' in session:
        # User is loggedin show them the home page
        return render_template('home.html')
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    username = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Get the data submitted by user in the form, and store in relevant variables
        username = request.form['username']
        password = request.form['password']
        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s', (username,))
        # Fetch one record and return result
        account = cursor.fetchone()
        cursor.close() #Use close() when you are done using a cursor. 
        if not account:
            flash('Incorrect username!','error')
        elif check_password_hash(account['password'],password):
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = username
            session['email'] = account['email']
            return redirect(url_for('home'))
        else:
            flash('Incorrect password!','error')
    return render_template('login.html')

@app.route('/logout')
def logout():
   # Remove session data, this will log the user out
   session.clear()
   # Redirect to login page
   return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s', (username,))
        account = cursor.fetchone()
        # If account exists show error and validation checks
        if account:
            #Use flash function to flash error message
            flash('Account already exists!','error')
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            #checking email format at server side. This is slightly more 'rigourous' than the client side validation.
            #for example a@a will pass the client side email validation, but will fail the server side validation below.
            flash('Invalid email address!','error')
        elif not re.match(r'[A-Za-z0-9]+', username):
            #ensures username only contains alphabets and digits.
            flash('Username must contain only characters and numbers!','error')
        else:
            # Account does not exists and the form data is valid, now insert new account into accounts table
            cursor.execute('INSERT INTO accounts VALUES (NULL, %s, %s, %s)', (username, generate_password_hash(password), email,))
            mysql.connection.commit() #commit the insertion
            #Use flash function to flash a successfully reigstered message
            flash('Congratulations, you have successfully registered. Try logging in now!','success')
            #redirects to login page with successful message
            return redirect(url_for('login'))

    # Show registration form with relevant message (if any)
    return render_template('register.html')

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'loggedin' in session:
        if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
            password = request.form['password']
            email = request.form['email']
            if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                flash('Invalid email address!','error')
            else:
                cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                cursor.execute('UPDATE accounts set email=%s, password=%s WHERE id = %s ', 
                                (email, generate_password_hash(password), session['id'],))
                mysql.connection.commit() #note that you need to commit the changes for INSERT,UPDATE and DELETE statements
                cursor.close()
                flash('Update successful','success')
        return render_template('profile.html')
    return redirect(url_for('login'))

@app.route('/search', methods=['GET', 'POST'])
def search():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM books')
    print([i[0] for i in cursor.description])
    fields = [i[0] for i in cursor.description][1:]
    if request.method == 'POST':
        category =  request.form.get('category')
        if category in fields: #check that category is indeed a valid category (prevent SQL injection)
            search = '%' + request.form['search'] + '%'
            query = 'SELECT * FROM books WHERE ' + category + ' like %s' 
            cursor.execute(query, (search,))
    books = cursor.fetchall() #fetch all records
    cursor.close()
    return render_template('search.html',books=books, fields=fields) #pass books data to search.html

if __name__ == '__main__':
    app.run(debug = True)