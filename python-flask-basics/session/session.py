from flask import Flask ,redirect, url_for, render_template, request, session
from datetime import timedelta
from flask import flash
from flask_sqlalchemy import SQLAlchemy  # pip install flask-sqlalchemy

app = Flask(__name__)
app.secret_key = 'hello'
app.permanent_session_lifetime = timedelta(minutes=5)  # set time for the session

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'  # creating users.sqlite3 file
app.config['SQLALCHMEY_TRACK_MODIFICATIONS'] = False   # Ignores warnings
db = SQLAlchemy(app)   # initialize the database app

class users(db.Model) :     # create the user database
	_id = db.Column('id', db.Integer, primary_key=True)  # creating the id column so no duplicates will occur
	name = db.Column(db.String(100))                     # creating the name column
	email = db.Column(db.String(100))					 # creating the email column

	def __init__(self, name, email) :                    # __init__ function
		self.name = name 								 # storing the name 
		self.email = email 								 # storing the email

@app.route('/home')
def home() :
	return render_template('index.html')

@app.route('/view')  
def view() :
	return render_template('view.html',values = users.query.all())	# fetching all the columns to display

@app.route("/login", methods=['POST','GET'])
def login() :
	if request.method == 'POST':
		session.permanent = True ## here we keep our session to permanent 
		user = request.form['nm']   # here we take input from the form
		session['user'] = user     ## session is here

		found_user = users.query.filter_by(name=user).first()  		# checking for the user is available or not
		if found_user :
			session['email'] = found_user.email 					# storing the database value to session value

		else :
			usr = users(user,'')
			db.session.add(usr)										# adding the user
			db.session.commit()										# session.commit is compulsory after every operation

		flash('Login successful','info')
		return redirect(url_for('user'))
	else :
		if "user" in session :
			flash('Already Logged In','info')
			return redirect(url_for('user'))
		else :
			return render_template('login.html')

@app.route("/user", methods=['POST','GET'])
def user() :
	if 'user' in session :
		user = session['user']  # here we fetch the values form the session about the user 
		print(session['user'])
		if request.method == 'POST' :
			email = request.form['email']
			session['email'] = email
			
			found_user = users.query.filter_by(name=user).first()
			found_user.email = email
			db.session.commit()

			flash('Your email was saved !','info')
			return render_template('user.html', email=email)
		else :
			if 'email' in session :
				email = session['email']
				

				return render_template('user.html', email=email)

		return render_template('user.html',user=user)
	else :
		flash('You are not logged in !!','info')
		return redirect(url_for('login'))

@app.route('/logout') 
def logout() :
	session.pop('user', None) # here we logout
	session.pop('email', None)
	flash('you have been logged out successfully','info')  ## flash message is here
	return redirect(url_for('login'))

if __name__ == '__main__':
	db.create_all()
	app.run(debug=True)