#!/usr/bin/env python3
from flask import Flask,  render_template

APP = Flask(__name__)
HOST, PORT = '0.0.0.0' , 5005
APP.url_map.sort_key = False
APP.debug = True
pamps_list = ["Product0","Product1","Product2","Product3"]

@APP.route("/")
@APP.route("/home")
def routeHome():

    return render_template("1.html", pamps_list = pamps_list, ROUT="/" )
@APP.route("/user/<username>")
def rout_usr(username):
    pass


if __name__ == "__main__":
    APP.run(host=HOST, port=PORT, debug=True)
