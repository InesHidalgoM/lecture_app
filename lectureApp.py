from flask import Flask , render_template, request, jsonify
from datetime import datetime
from eventbrite import Eventbrite
import requests

app = Flask("My Flask App")

eventbrite = Eventbrite("5Q5HRS46AWMKIYGZGEAW")
user = eventbrite.get_user()
user["id"]
user["name"]

@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    return jsonify({'ip': request.remote_addr}), 200


@app.route("/")
def default_path():
    return render_template ("index.html", name="First Lecture") #This


@app.route("/show_lectures", methods=["POST"])
def read_form():
	return render_template ("lectures.html", date=date, sign=sign, data=data) 
	#return "All OK"

if __name__ == '__main__':
	app.run(debug=True)


param = {
    "q" : "seminar" # "lecture", "class", "workshop",
    "location.address" : "Edinburgh"
}
print param["location.address"]

#param = {
#   "q" : "lecture",
#    "location.address" : "Edinburgh"
#}
#print param["location.address"]

#prints first result
first = results["events"][0]

#prints descriptions
print(first['description']['text'])

#this was useful for us just to know which paramters to filter through, or what to print on the website
#print(first.keys())

print(first['name'])

@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    print request.remote_addr
        return jsonify({'ip': request.remote_addr}), 200

response, code = get_my_ip()

print response.text

resp = requests.get('https://ipinfo.io/8.8.8.8/json')

resp.json()
