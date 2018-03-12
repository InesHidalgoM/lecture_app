from flask import Flask , render_template, request
from datetime import datetime

app = Flask("My Flask App")


#@app.route("/")
#def default_path():
#return render_template ("index.html") #This 


@app.route("/show_lectures", methods=["POST"])
def read_form():
	return render_template ("lectures.html", date=date, sign=sign, data=data) 
	#return "All OK"


if __name__ == '__main__':
	app.run(debug=True)
