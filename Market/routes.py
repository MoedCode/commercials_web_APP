#!/usr/bin/env python3
from Market import app, render_template, jsonify, session, redirect, make_response, request, abort, json

import ast


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


@app.route("/post_user", methods=["POST"])
def post_user():

    with open ("tmp1.md", "w") as FILE:
        FILE.write(f"# {request.url}\n{request.get_json()}\n")
    if "image" in request.files:
        image_file = request.files["image"]
        print(image_file)
        image_file.save("/Market/static/images/users")
    with open ("tmp1.md", "a") as FILE:
        FILE.write(f"image_received\n{request.files}\n")

    from modules.users import Users
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'email' not in request.get_json():
        abort(400, description="Missing email")
    if 'password' not in request.get_json():
        abort(400, description="Missing password")

    data = request.get_json()
    print(data)
    instance = Users(**data)
    # instance.save()
    with open ("tmp1.py", "a") as FILE:
        FILE.write(instance)

    return redirect("/login")