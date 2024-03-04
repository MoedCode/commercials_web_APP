#!/usr/bin/env python3
from flask import Flask,  render_template
from data0 import *
APP = Flask(__name__)
HOST, PORT = '0.0.0.0' , 5005
APP.url_map.sort_key = False
APP.debug = True
# Updated items list


@APP.route("/")
@APP.route("/home")
def routeHome():

    return render_template("home.html")
@APP.route('/market')
# @APP.route('/prostore/market')
def rout_market():
    return render_template('market.html', products_list=products_list)
@APP.route("/user/<username>")
def rout_usr(username):
    pass



if __name__ == "__main__":
    APP.run(host=HOST, port=PORT, debug=True)
