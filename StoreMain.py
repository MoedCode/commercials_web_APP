#!/usr/bin/env python3
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import uuid
from modules.engine.local_storage import LocalStorage

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)
local_storage = LocalStorage()
time = "%Y-%m-%dT%H:%M:%S.%f"
class Base(db.Model):
    id = db.Column(db.String(length=40), nullable=False, unique=True, primary_key=True)
    created_at = db.Column(db.String(length=25), nullable=False)
    updated_at = db.Column(db.String(length=25), nullable=False)

    def __init__(self):
        """ """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow().strftime(time)
        self.updated_at = self.created_at

    def to_dict(self):
        """    """
        instance = self.__dict__.copy()

        self.updated_at = datetime.utcnow().strftime(time)
    def save(self, save_option="both"):
        self.updated_at = datetime.utcnow().strftime(time)
        if save_option in ["local", "both"]:
            local_storage.save(self.__class__.__name__, self)
        if save_option in ["DB", "both"]:
            db.session.add(self)
            db.session.commit()

class Products(Base):
    name = db.Column(db.String(length=50), nullable=False, unique=True)
    category = db.Column(db.String(length=50), nullable=False)
    brand = db.Column(db.String(length=50), nullable=False)
    price = db.Column(db.Float(), nullable=False)
    rating = db.Column(db.Float(), nullable=True)
    In_Stock = db.Column(db.Boolean(), nullable=False)
    discount = db.Column(db.Float(), nullable=True)
    stock_quantity = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=40), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    about = db.Column(db.String(length=2048), nullable=True)
    img_list = db.Column(db.ARRAY(db.String(length=255)), nullable=False)

    def __init__(self, name, category, brand, price, stock_quantity=0, rating=None, discount=None, In_Stock=None, barcode=None, description=None, img_list=None, about=None):
        super().__init__()
        self.name = name
        self.category = category
        self.brand = brand
        self.price = price
        self.stock_quantity = stock_quantity
        self.rating = rating
        self.discount = discount
        self.In_Stock = In_Stock if In_Stock is not None else stock_quantity > 0
        self.barcode = barcode if barcode is not None else str(uuid.uuid4())
        self.description = description
        self.about = about
        self.img_list = img_list if img_list is not None else []

        if not 1 <= len(self.img_list) <= 10:
            raise ValueError("Number of images must be between 1 and 10")

    def __repr__(self):
        return f"Products(name={self.name}, id={self.id})"

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/market')
def market():
    products_list = Products.query.all()
    return render_template('market.html', products_list=products_list)

@app.route('/product/<product_id>')
def product(product_id):
    product_instance = Products.query.get(product_id)
    if product_instance:
        return render_template('product.html', product=product_instance)
    else:
        return render_template('product_not_found.html', product_id=product_id)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5005, debug=True)
