#!/usr/bin/env python3
from flask import Flask, render_template_string

APP = Flask(__name__)
HOST, PORT = '0.0.0.0' , 3000
APP.url_map.sort_key = False
APP.debug = True
string_list = ["string0","string1","string2","string4"]
strtemp = """
<style> body{
    background-color: aqua;
}</style>
<ul>{% for _ in string_list  %} <li><h2>{{ _ }}</h2></li>{% endfor%}</ul>
"""
@APP.route("/")
def routeHome():
    return render_template_string( strtemp, string_list=string_list)
@APP.route("/user/<username>")
def rout_usr(username):

    strtemp1 = """
    {% if username %} <h1> {{ username}} </h1>
    {% else %} <h1> no name! </h1>
    {% endif %}
    """
    return render_template_string (strtemp1 + strtemp, username=username,string_list=string_list )
if __name__ == "__main__":
    APP.run(host=HOST, port=PORT, debug=True)
