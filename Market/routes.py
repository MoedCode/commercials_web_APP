#!/usr/bin/env python3
from Market import app, render_template, jsonify
from modules.products import Products
import ast
@app.route("/")
def home_rout():
    return render_template("home.html")


@app.route('/api/market')
def marketApi():
    all_products = Products.query.all()
    products_dict_list = [product.to_dict() for product in all_products]

    return jsonify(products_dict_list)


@app.route('/market')
def market_route():
    products_list = Products.query.all()
    # Convert the Products objects to a serializable format
    products_dict_list = [product.to_dict() for product in products_list]
    return render_template('market.html', products_list=products_dict_list)


@app.route('/product/<product_id>')
def product_rout(product_id):
    product_instance = Products.query.get(product_id)
    if product_instance:
        # Convert the string back to a list of image paths
        product_instance.img_list = product_instance.img_list.split(',')
        return render_template('product.html', product=product_instance)
    else:
        return render_template('product_not_found.html', product_id=product_id)

@app.route('/api/product/<product_id>')
def product_API(product_id):
    product_instance = Products.query.get(product_id)

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
from modules import product_data
