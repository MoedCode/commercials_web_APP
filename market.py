#!/usr/bin/env python3
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from modules import local_storage
import uuid
import json
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
database_path = os.path.join(current_dir, 'market.db')
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{database_path}'
db = SQLAlchemy(app)

time = "%Y-%m-%dT%H:%M:%S.%f"


class Base(db.Model):
    id = db.Column(db.String(length=40), nullable=False, unique=True, primary_key=True)
    created_at = db.Column(db.String(length=25), nullable=False)
    updated_at = db.Column(db.String(length=25), nullable=False)

    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                self.updated_at = datetime.utcnow()
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

    def to_dict(self, save_fs=None):
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
        new_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        return new_dict

    def save(self, save_option="both"):
        self.updated_at = datetime.utcnow().strftime(time)
        if save_option in ["local", "both"]:
            local_storage.add(self)
            local_storage.commit()
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
    img_list = db.Column(db.String(length=4096), nullable=False, default="")

    def __init__(self, name, category, brand, price, stock_quantity=0, rating=None, discount=None, In_Stock=None,
                 barcode=None, description=None, img_list=None, about=None):
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
        self.img_list = ",".join(img_list) if img_list else ""

    def get_img_list(self):
        return [] if not self.img_list else self.img_list.split(",")

    def add_image(self, image_url):
        current_img_list = self.get_img_list()
        current_img_list.append(image_url)
        self.img_list = ",".join(current_img_list)
        db.session.commit()

    def to_dict(self, save_fs=None):
        new_dict = super().to_dict(save_fs)
        new_dict["img_list"] = self.get_img_list()
        return new_dict


@app.route("/")
def home():
    return render_template("home.html")


@app.route('/api/market')
def marketApi():
    all_products = Products.query.all()
    products_dict_list = [product.to_dict() for product in all_products]
    return jsonify(products_dict_list)


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
