#!/usr/bin/env python3
import json

from flask import Flask,  render_template
from modules.engine.File_Storage import FileStorage
from modules.product import Product
# from data0 import *
APP = Flask(__name__)
HOST, PORT = '0.0.0.0' , 5005
APP.url_map.sort_key = False
APP.debug = True
# Updated items list
products_list = []
with open('data0.json', 'r') as file:
    products_list = json.load(file)
FS = FileStorage()
FS.reload()
products_list= FS.all(Product).values
FileStorage.reload()
@APP.route("/")
@APP.route("/home")

def route_home():

    return render_template("home.html")
@APP.route('/market')
# @APP.route('/prostore/market')
def rout_market():
    return render_template('market.html', products_list=products_list)
@APP.route('/productقاطع_يا_ابن_اليهودية/<int:productId>')
def rout_product(productId):

    concern_product = {}
    for product in products_list:
        if product['id'] == productId:
            concern_product = product


        # else:
        #     pass
        #     concern_product = {"Error":"Not Found", "ID":productId}

    return render_template('product.html', product=concern_product)
@APP.route("/user/<username>")
def rout_usr(username):
    pass



if __name__ == "__main__":
    APP.run(host=HOST, port=PORT, debug=True)
