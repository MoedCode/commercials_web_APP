#!/usr/bin/env python3
from curses import flash
import inspect

import ast
import os
import re
from Market import app, render_template, jsonify, session, redirect, make_response, request, abort, json, DEBUG


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
    from modules.users import Users

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
    data["password"] = data["password"].strip()
    del data["image"]
    print(f"\n\n a7a {data} \n\n")

    instance = Users(email=data["email"], password=data["password"],first_name=data["first_name"], last_name=data["last_name"],
                     nickname=data["nickname"])
    print(f" \n\n :: user instance >>  {instance} \n\n")
    instance.save("DB")
    with open ("tmp1.md", "a") as FILE:
        FILE.write(f"\n instance \n{instance}")

    return redirect("/login")

from flask import jsonify

@app.route("/profile", methods=["POST"])
def profile_rout():
    print(f"\n\n\n{request.form}\n")
    email = request.form.get("email")
    password = request.form.get("password").strip()

    from modules.users import Users
    user = session.query(Users).filter_by(email=email).first()
    print(f"email:{user.email}, password:{user.password}\n\n  ")
    errMsg = f"No data found for {email}. Please ensure that the provided email is correct."

    if user is None:
        return jsonify({'success': False, 'error': errMsg})
    elif user.password != password:
        return jsonify({'success': False, 'error': 'Incorrect Password!'})

    # If everything is fine, return success response
    return render_template("profile.html", user=user)


@app.route("/api/profile/<email>/<PWD>")
def profile_API(email,PWD):
    from modules.users import Users

    user = session.query(Users).filter_by(email=email).first()

    if user:
        if user.password != PWD:
            return ({"error": "password not correct"}), 404
        del user.password
        return jsonify(user.to_dict()), 200
    else:
        return jsonify({"error": "User not found"}), 404
    '''
    if 'email' in session:
        email = session['email']
        # Query the database to retrieve user information based on email
        user = Users.query.filter_by(email=email).first()
        if user:
            return (user)
        else:
            return {"error message":"user not found", "Error code":-1}
    else:
        return {"alert","Please log in to view your profile"}

    '''

'''
@app.route("/profile")
def profile_route():
    from modules.users import Users

    if 'email' in session:
        email = session['email']
        # Query the database to retrieve user information based on email
        user = Users.query.filter_by(email=email).first()
        if user:
            return render_template("profile.html", user=user)
        else:
            flash("User not found", "error")
            return redirect("/login")
    else:
        flash("Please log in to view your profile", "error")
        return redirect("/login")


@app.route("/profile/<email>/<PWD>")
def profile_rout(email,PWD):
    from modules.users import Users
    user = session.query(Users).filter_by(email=email).first()
    errMsg = f"no data found for {email} pleas insure that the provided email is correct "
    if user is None:
        flash(errMsg)
        return redirect("/login")
    if user:
        if user.password != PWD:
            flash("incorrect Password !")
            return redirect("/login")
    del user.password
    return render_template("profile.html", user=user)

'''