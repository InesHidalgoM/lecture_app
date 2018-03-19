from eventbrite import Eventbrite
from flask import Flask , render_template, request, jsonify
from datetime import datetime
import requests

eventbrite = Eventbrite("5Q5HRS46AWMKIYGZGEAW")
user = eventbrite.get_user()
user["id"]
user["name"]

@app.route("/show_lectures", methods=["POST"])
def read_form():
    form_data=request.form
    location = (form_data["city"])
    data = city
    return render_template ("lectures.html", data=data)
    return "All OK"

param = {
    "q":"lecture",
    "location.address": "{}".format(city)
}

lectures = eventbrite.event_search(**param)
one = lectures["events"][1]
two = lectures["events"][2]
three = lectures["events"][3]
four = lectures["events"][4]
five = lectures["events"][5]
six = lectures["events"][6]

app = Flask("My Flask App")

@app.route("/")
def default_path():
    return render_template ("index.html", name1=(one["name"]["text"]), content1=(one["description"]["text"]), name2=(two["name"]["text"]), content2=(two["description"]["text"]), name3=(three["name"]["text"]), content3=(three["description"]["text"]), name4=(four["name"]["text"]), content4=(four["description"]["text"]), name5=(five["name"]["text"]), content5=(five["description"]["text"]),name6=(six["name"]["text"]), content6=(six["description"]["text"]))

#@app.route("/get_my_ip", methods=["GET"])
#def get_my_ip():
#return jsonify({"ip": request.remote_addr}), 200
#here = request.remote_addr

#response = requests.get("https://ipinfo.io/{}/json" .format(here))
#response.json()
#location = here[loc]

if __name__ == '__main__':
	app.run(debug=True)


