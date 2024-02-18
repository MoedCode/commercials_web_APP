#!/usr/bin/env python3
from flask import Flask

APP = Flask(__name__)
HOST, PORT = '0.0.0.0' , 3000
APP.url_map.sort_key = False
@APP.route("/")
def routeHome():
    return "<h1> احنا مين ..ال ضاع من عمرنا سنين</h1>"

if __name__ == "__main__":
    APP.run(host=HOST, port=PORT)
