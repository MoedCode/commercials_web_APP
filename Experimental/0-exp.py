#!/usr/bin/env python3
from flask import Flask, render_template_string
from  stringTemp import *
APP = Flask(__name__)
HOST, PORT = '0.0.0.0' , 3000
APP.url_map.sort_key = False
APP.debug = True
string_list = ["string0","string1","string2","string4"]
render1 =  html + strtemp + end
render2 = render1 + strtemp1 + end
@APP.route("/")
def routeHome():
    return render_template_string( render1, string_list=string_list)
@APP.route("/user/<username>")
def rout_usr(username):


    return render_template_string (html + strtemp1 + strtemp, username=username,string_list=string_list )
if __name__ == "__main__":
    APP.run(host=HOST, port=PORT, debug=True)
