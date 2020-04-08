from flask import Flask, render_template, request
import pymysql
import traceback
app=Flask(__name__)

db = pymysql.connect("localhost", "root", "12345","db_test")




@app.route("/")
def guest():
	return render_template('Website.html')

@app.route("/signin")
def signin():
	return render_template('loginin.html')

@app.route("/signup")
def signup():
	return render_template('signup.html')


@app.route('/signin-success' ,methods=["POST", "GET"])
def signinSuccess():
	if request.method=="POST":
		if request.form['username'] != '' and request.form['password'] != '':
			usrname = request.form['username']
			pwd = request.form['password']
			msg=''

			# prepare a cursor object using cursor() method
			cursor = db.cursor()

			# Execute the SQL command
			sql = ("SELECT username, password FROM member WHERE username = '"+usrname+"' AND password = '" + pwd + "'")
			cursor.execute(sql)

			# Commit your changes in the database
			db.commit()
			results = cursor.fetchone()
			if results != None:
				msg = "Welcome! " + usrname
				return render_template("Website.html", msg = msg, username=usrname)
			else:
				msg = "Username/Password is incorrect"
				usrname = ""
				return render_template("loginin.html", msg = msg)
		else:
			msg = "Username/Password is incorrect"
			return render_template("loginin.html", msg = msg)
	else:
		return render_template("loginin.html")

@app.route('/signup-success' ,methods=["POST", "GET"])
def enter():
	if request.method=="POST":

		if request.form['username'] != '' and request.form['password'] != '':
			usrname=request.form ["username"]
			pwd=request.form["password"]

			cursor = db.cursor()
			sql = ("SELECT username, password FROM member WHERE username = '"+usrname+"'")
			cursor.execute(sql)

			# Commit your changes in the database
			db.commit()
			results = cursor.fetchone()
			if results != None:
				msg = "Username has been used"
				return render_template("signup.html", msg = msg)
			else:
				cursor2= db.cursor()
				cursor2.execute(""" insert into member(username, password)value (%s, %s)""", (usrname, pwd))

				try:
					db.commit();
					msg="Welcome! " + usrname
				except Exception as e:
					db.rollback();

				return render_template("Website.html", msg = msg, username=usrname)
		else:
			msg = "Form Incomplete"
			return render_template("signup.html", msg = msg)	
	else:
		return render_template("Website.html")
if __name__=='__main__':
	app.run(debug=True)
