from flask import Flask, flash, redirect, url_for, render_template, request, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'store'

mysql = MySQL(app)
app.secret_key = 'key2'

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/search/<category>", methods=['GET', 'POST'])
def search(category):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('select distinct(color) from color')
    f1 = cursor.fetchall()
    color_dropdown = [c['color'] for c in f1]
    cursor.execute('select distinct(type) from product')
    f2 = cursor.fetchall()
    type_dropdown = [c['type'] for c in f2]
    cursor.close()
    size_dropdown = ['XS','S','M','L','XL','XXL']

    sortby = request.args.get('sort', 'recent')
    selected_colors = request.args.getlist('color', None)
    selected_sizes = request.args.getlist('size', None)
    selected_types = request.args.getlist('type', None)
    search = request.args.get('search', '')
    search = '%'+search+'%'

    if not selected_colors: colors=None
    else: 
        colors = str(selected_colors)
        colors='('+colors[1:len(colors)-1]+')'
    if not selected_sizes: sizes=None
    else: 
        sizes = str(selected_sizes)
        sizes='('+sizes[1:len(sizes)-1]+')'
    if not selected_types: types=None
    else: 
        types = str(selected_types)
        types='('+types[1:len(types)-1]+')'

    items=[]

    query = 'with q as (select distinct p1.pid, p1.name, price, image,addDate from product p1, color, category, designer where p1.pid = color.pid and p1.pid = category.pid and designer.designerid = p1.designerid and (p1.name like \'{0}\' or designer.name like \'{0}\') and (\'{1}\'="All" or category = \'{1}\') '.format(search,category)
    if colors: query += 'and color in {0}'.format(colors)
    if sizes: query += 'and size in {0}'.format(sizes)
    if types: query += 'and type in {0}'.format(types)

    if(sortby=='priMin'): query += ' order by price'
    elif(sortby=='priMax'): query += ' order by price desc'
    else: query += ' order by addDate desc'
    query += ') select * from q q1 where q1.price <= all(select price from q q2 where q1.name = q2.name)'
    
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute(query)
    items = cursor.fetchall()
    cursor.close()

    return render_template('search.html',items=items,color_dropdown=color_dropdown,type_dropdown=type_dropdown,size_dropdown=size_dropdown,
                            sortby=sortby,colors=selected_colors,sizes=selected_sizes,types=selected_types,category=category)

@app.route("/product/<pid>", methods=['GET', 'POST'])
def product(pid):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('select product.*,designer.name as designer from product,designer where pid = %s and designer.designerid = product.designerid',(pid,))
    item = cursor.fetchone()
    cursor.execute('select p1.pid as pid,p1.size as size,p1.price as price from product p1, product p2 where p2.pid = %s and p1.image = p2.image',(pid,))
    others = cursor.fetchall()

    if request.method == 'POST':
            if request.form['submit_button'] == 'Add to favourites':
                if 'loggedin' in session:
                    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                    cursor.execute('INSERT INTO favourite VALUES (%s, %s)', (int(pid),session['id'],))
                    mysql.connection.commit()
                    cursor.close()
            elif request.form['submit_button'] == 'Add to cart':
                if 'loggedin' in session:
                    quantity = request.form['quantity']
                    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                    cursor.execute('select cartid from cart where cid=%s and date is null', (session['id'],))
                    cartid = cursor.fetchone()
                    if not cartid:
                        cursor.execute('INSERT INTO cart VALUES (NULL, DEFAULT, %s, NULL, NULL, NULL)',(session['id'],))
                        cursor.execute('select cartid from cart where cid=%s and date is null', (session['id'],))
                        cartid = cursor.fetchone()
                    cartid = cartid['cartid']
                    try:
                        cursor.execute('INSERT INTO addedto VALUES (%s, %s, %s)', (int(pid),cartid,quantity,))
                    except:
                        cursor.execute('UPDATE addedto set quantity = quantity + %s where cartid = %s and pid = %s',(quantity,cartid,int(pid),))
                    mysql.connection.commit()
                    cursor.close()

    cursor.close()
    return render_template('product.html',item=item,others=others)

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    username = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Get the data submitted by user in the form, and store in relevant variables
        username = request.form['username']
        password = request.form['password']
        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM customer WHERE username = %s', (username,))
        # Fetch one record and return result
        account = cursor.fetchone()
        cursor.close() #Use close() when you are done using a cursor. 
        if not account:
            flash('Incorrect username. Please try again.')
        elif check_password_hash(account['password'],password):
            session['loggedin'] = True
            session['id'] = account['cid']
            session['username'] = username
            session['email'] = account['email']
            session['name'] = account['name']
            session['phone'] = account['phoneNo']
            session['address'] = account['address']
            session['dob'] = account['dateOfBirth'].strftime("%d/%m/%Y")
            return redirect(url_for('home'))
        else:
            flash('Incorrect password. Please try again.')
    return render_template('login.html')

@app.route('/logout')
def logout():
   # Remove session data, this will log the user out
   session.clear()
   return redirect(url_for('home'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        name = request.form['name']
        dob = request.form['dob']
        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM customer WHERE username = %s', (username,))
        account = cursor.fetchone()
        # If account exists show error and validation checks
        if account:
            #Use flash function to flash error message
            flash('Account already exists. Please try again.')
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            #checking email format at server side. This is slightly more 'rigourous' than the client side validation.
            #for example a@a will pass the client side email validation, but will fail the server side validation below.
            flash('Invalid email address!')
        elif not re.match(r'[A-Za-z0-9]+', username):
            #ensures username only contains alphabets and digits.
            flash('Username must contain only characters and numbers!')
        else:
            # Account does not exists and the form data is valid, now insert new account into accounts table
            cursor.execute('INSERT INTO customer VALUES (NULL, %s, NULL, NULL, %s, %s, %s, %s)', (email,username, generate_password_hash(password), name, dob,))
            mysql.connection.commit() #commit the insertion
            cursor.execute('SELECT * FROM customer WHERE username = %s', (username,))
            acc = cursor.fetchone()
            print(acc)
            session['loggedin'] = True
            session['id'] = acc['cid']
            session['username'] = username
            session['email'] = email
            session['name'] = name
            session['dob'] = acc['dateOfBirth'].strftime("%d/%m/%Y")
            cursor.close()
            return redirect(url_for('home'))
        cursor.close()
    # Show registration form with relevant message (if any)
    return render_template('register.html')

@app.route('/profile')
def profile():
    if 'loggedin' in session:
        return render_template('profile.html')
    return redirect(url_for('login'))
@app.route('/past_orders')
def past_orders():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM cart WHERE cid = %s and date is not null', (session['id'],))
    data = cursor.fetchall()
    cursor.close()
    return render_template('past_orders.html', data = data)
@app.route('/vouchers')
def vouchers():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM discount WHERE cid = %s', (session['id'],))
    data = cursor.fetchall()
    cursor.close()
    return render_template('vouchers.html', data = data)

@app.route('/cart', methods=['GET', 'POST'])
def cart():
    if 'loggedin' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('select cartid from cart where cid=%s and date is null', (session['id'],))
        cartid = cursor.fetchone()
        if not cartid:
            cursor.execute('INSERT INTO cart VALUES (NULL, DEFAULT, %s, NULL, NULL, NULL)',(session['id'],))
            items=()
        else:
            cartid = cartid['cartid']
            cursor.execute('select cart.cartid,totalPrice,product.pid,product.name,price,size,quantity,image,totalPrice from cart,addedto,product where addedto.cartid = %s and product.pid = addedto.pid and cid = %s and date is null', (cartid,session['id'],))
            items = cursor.fetchall()
        cursor.close()

        if request.method == 'POST':
            print('form')
            # quantity = request.args.getlist()
            # print(quantity)
            # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            # cursor.execute('UPDATE addedto set quantity = %s where cartid = %s and pid = %s',(quantity,cartid,int(pid),))
            # mysql.connection.commit()
            # cursor.close()
            if 'delete' in request.form:
                print('det')
            if 'checkout' in request.form:
                cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                cursor.execute('UPDATE cart set date = %s,shipCost = %s,status = %s where cartid = %s',(datetime.today().strftime('%Y-%m-%d'),0.0,"Out for delivery",cartid,))
                mysql.connection.commit()
                cursor.close()
                return redirect(url_for('past_orders'))

        return render_template('cart.html',items=items)
    return redirect(url_for('login'))

@app.route('/favourites')
def favourites():
    if 'loggedin' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT product.pid, product.name, product.price, product.image FROM favourite,product WHERE cid = %s and favourite.pid = product.pid', (session['id'],))
        items = cursor.fetchall()
        cursor.close()
        return render_template('favourites.html',items=items)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run()