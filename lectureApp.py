from flask import Flask , render_template, request
from datetime import datetime
#from eventbrite import Eventbrite

app = Flask("My Flask App")


@app.route("/")
def default_path():
    return render_template ("index.html") #This


@app.route("/show_lectures", methods=["POST"])
def read_form():
	return render_template ("lectures.html", date=date, sign=sign, data=data) 
	#return "All OK"


#eventbrite = Eventbrite("5Q5HRS46AWMKIYGZGEAW")
#user = eventbrite.get_user()
#user["id"]
#63732380485
#user["name"]
#Amelie Johnson-Ferguson


if __name__ == '__main__':
	app.run(debug=True)
