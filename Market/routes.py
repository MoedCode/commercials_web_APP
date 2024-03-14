#!/usr/bin/env python3
from Market import app, render_template, jsonify
from Market.modules import Products

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
    return render_template('market.html', products_list=products_list)


@app.route('/product/<product_id>')
def product_rout(product_id):
    product_instance = Products.query.get(product_id)
    if product_instance:
        return render_template('product.html', product=product_instance)
    else:
        return render_template('product_not_found.html', product_id=product_id)
