from flask import Flask,url_for,request
from flask import render_template

app = Flask(__name__)

@app.route("/",methods=['GET'.'POST'])
def hello():
	return "Hello World!"

@app.route("/post/<int:post_id>")
def mostrar_post(post_id):
	return "Post %d" %post_id

@app.route("/post/")
@app.route("/post/<nombredeusuario>")
def mostrar_nombre(nombredeusuario=None):
	return render_template("hola.html", name=nombredeusuario)


if __name__ == "__main__":
	url_for('static', filename='style.css')
	app.debug=True
	app.run()

