#!/usr/bin/env python3
from flask import Flask
from flask import render_template
import requests

MAJORTOM = "http://api.open-notify.org/astros.json"
MAJORTOMPOS = "http://api.open-notify.org/iss-now.json"

app = Flask(__name__)

#grab the astroindex value
@app.route("/astronum/<int:astroindex>")
def index(astroindex):
    # render the jinja template "nasa.html"
    # apply the value of username for the var name
    try:
        groundctrl = requests.get(MAJORTOM)
        nasa_json = groundctrl.json()

        isspos = requests.get(MAJORTOMPOS)
        isspos_json = isspos.json()
        
        astroman = nasa_json["people"][astroindex]["name"]
        astromanpos_lat = isspos_json["iss_position"]["latitude"]
        astromanpos_lon = isspos_json["iss_position"]["longitude"]

        return render_template("nasa.html", astroname=astroman, lat=astromanpos_lat, lon=astromanpos_lon)
    
    except Exception as err:
        return render_template("nasa.html", astroname = "Out of range.")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
