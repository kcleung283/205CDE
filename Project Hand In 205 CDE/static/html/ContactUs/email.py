from flask import Flask
from flask_mail import Mail, Message

app= Flask(__name__)
app.config.from_pyfile('config.cfg')

mail=Mail(app)

@app.route('/', methods=['GET','POST'])
def index():
	if request.method=='GET':
		return ' <form action="/" method="POST"><input name ="email"><input type="submit"></form>'
	return 'The email you entered is{}'.format(request.form['email'])


if __name__=='__main__':
app.run(debug=True)