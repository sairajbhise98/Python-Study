from flask import Flask ,redirect, url_for, render_template

app = Flask(__name__)

@app.route('/home')
def home() :
	return render_template('child.html',content=['tim','sai','ravi','pruthvi'])

@app.route('/test')
def test() :
	return render_template('new.html')



if __name__ == '__main__':
	app.run(debug=True)