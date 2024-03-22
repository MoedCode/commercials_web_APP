#!/usr/bin/env python3
import inspect

import ast
import os
import re
from Market import app, render_template, jsonify, session, redirect, make_response, request, abort, json, DEBUG
from modules.users import Users


@app.route("/")
def home_rout():
    return render_template("home.html")


@app.route('/api/market')
def marketApi():
    from modules.products import Products

    all_products = session.query(Products).all()
    products_dict_list = [product.to_dict() for product in all_products]

    return jsonify(products_dict_list)


@app.route('/market')
def market_route():
    from modules.products import Products

    products_list = session.query(Products).all()
    # Convert the Products objects to a serializable format
    products_dict_list = [product.to_dict() for product in products_list]
    return render_template('market.html', products_list=products_dict_list)


@app.route('/product/<product_id>')
def product_rout(product_id):
    from modules.products import Products

    product_instance = session.query(Products).get(product_id)
    if product_instance:
        # Convert the string back to a list of image paths
        product_instance.img_list = product_instance.img_list.split(',')
        return render_template('product.html', product=product_instance)
    else:
        return render_template('product_not_found.html', product_id=product_id)

@app.route('/api/product/<product_id>')
def product_API(product_id):
    from modules.products import Products

    product_instance = session.query(Products).get(product_id)

    if product_instance:
        print(product_instance.to_dict())
        return (product_instance.to_dict()), 200
    else:
        return jsonify({"Error":"product not found"}), 304

@app.route('/about')
def about_route():
    return render_template('about.html')
@app.route("/post")
def post_route():

    return render_template("post.html")

# Authentication  Routes

@app.route("/login")
def login_route():

    return render_template("login.html")

@app.route("/register")
def register_route():

    return render_template("register.html")


@app.route("/post_user", methods=["POST"], strict_slashes=False)
def post_user():
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'email' not in request.get_json():
        abort(400, description="Missing email")
    if 'password' not in request.get_json():
        abort(400, description="Missing password")
    data = request.get_json()
    # if "image" in data:
    #     image_file =data["image"]
    #     print(f"\n\n:: image_file >> {image_file}\n\n")
    #     print(f" File:{os.path.abspath(__file__)} ,( line: {inspect.currentframe().f_lineno})")

    #     image_file.save("/Market/static/images/users")

    del data["image"]
    print(f"\n\n {data} \n\n")

    print(f" \n\n :: objToInst >>",{**data})

    instance = Users(email=data["email"], password=data["password"],first_name=data["first_name"], last_name=data["last_name"],
                     nickname=data["nickname"])
    instance.save("DB")
    with open ("tmp1.py", "a") as FILE:
        FILE.write(f"\n instance \n{instance}")

    return redirect("/login")

