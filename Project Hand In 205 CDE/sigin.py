from flask import Flask, render_template, request
import pymysql
app=Flask(__name__)

db = pymysql.connect("localhost", "root", "12345","db_test")




@app.route("/")
def guest():
	return render_template('signup.html')

@app.route('/insertDB' ,methods=["POST", "GET"])
def enter():
	if request.method=="POST":
		usrname=request.form ["username"]
		pwd=request.form["password"]

		cursor= db.cursor()
		cursor.execute(""" insert into member(username, password)value (%s, %s)""", (usrname, pwd))

		try:
			db.commite();
			msg="Name is successfully inserted!"
		except Exception as e:
			db.rollback();



		msg = 'hello world'

		return render_template("insertDB.html", msg = msg)

if __name__=='__main__':
	app.run(debug=True)
