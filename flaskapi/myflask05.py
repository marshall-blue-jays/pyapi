#!/usr/bin/python3
"""Alta3 APIs and HTML"""

## best practice says don't use commas in imports
# use a single line for each import
from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template

app = Flask(__name__)
## This is where we want to redirect users to
# This is a landing point for users (a start)
@app.route("/") # user can land at "/"
def seasonal_information():
    return "Seasonal information is available at /inseason"

@app.route("/inseason", methods=['GET']) # or user can land at "/start"
def inseason_check():

    if request.args.get('fruit'):
        fruit = request.args.get('fruit')
        fruit = fruit.lower()
        if fruit == "strawberry":
            return "Yes, strawberries are in season.\n"
        elif fruit == "pumpkin":
            return "No, pumpkins are not in season.\n"
        elif fruit == "mango":
            return "Yes, mangos are in season.\n"
        else:
            return "We do not carry that item.\n"
    if request.args.get('vegetable'):
        vegetable = request.args.get('vegetable')
        vegetable = vegetable.lower()
        if vegetable == "carrot":
            return "Yes, carrots are in season.\n"
        elif vegetable == "broccoli":
            return "No, broccoli is not in season\n"
        elif vegetable == "corn":
            return "Yes, corn is in season.\n"
        else:
            return "We do not carry that item.\n"
    return "To use this endpoint you need to specify either a 'fruit' or a 'vegetable' parameter\n"


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application

