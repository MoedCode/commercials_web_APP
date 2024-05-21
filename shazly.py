#!/usr/bin/env python3
from flask import Flask,  render_template

APP = Flask(__name__)
HOST, PORT = '0.0.0.0' , 3000
APP.url_map.sort_key = False
APP.debug = True
pamps_list = ["../static/images/0.png","../static/images/1.png","../static/images/2.png","../static/images/3.png"]

@APP.route("/shazly")
def routeHome():

    return render_template("0.html", pamps_list = pamps_list, ROUT="shazly" )
@APP.route("/user/<username>")
def rout_usr(username):


    pass

if __name__ == "__main__":
    APP.run(host=HOST, port=PORT, debug=True)
