#!/usr/bin/env python3
import os
import uuid
from sys import argv
from flask import Flask, jsonify
from sqlalchemy import create_engine, Column, String, Float, Boolean, Integer, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime


app = Flask(__name__)
dec_base = declarative_base()

# Update your MySQL database credentials here
HBNB_MYSQL_USER = 'ProMarket'
HBNB_MYSQL_PWD = 'ProMarket_PWD'
HBNB_MYSQL_HOST = 'localhost'
HBNB_MYSQL_DB = 'ProMarket_DB'

# MySQL database URI
DB_URI = f'mysql+pymysql://{HBNB_MYSQL_USER}:{HBNB_MYSQL_PWD}@{HBNB_MYSQL_HOST}/{HBNB_MYSQL_DB}'
engine = create_engine(DB_URI)

Session = sessionmaker(bind=engine)
session = Session()

time = "%Y-%m-%dT%H:%M:%S.%f"


class Base:

    __tablename__ = 'base'
    id = Column(String(length=40), nullable=False, unique=True, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    # relation base class and Products as Products(Base)
    # products = relationship("Products", back_populates="base")
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
            # new_dict["created_at"] = new_dict["created_at"].strftime(time)
            new_dict["created_at"] = new_dict["created_at"]
        if "updated_at" in new_dict:
            # new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
            new_dict["updated_at"] = new_dict["updated_at"]
        new_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        return new_dict

    def save(self, save_option="both"):
        self.updated_at = datetime.utcnow().strftime(time)
        if save_option in ["local", "both"]:
            from modules.engine.local_storage import LocalStorage
            local_storage = LocalStorage()
            local_storage.add(self)
            local_storage.commit()
        if save_option in ["DB", "both"]:
            session.add(self)
            session.commit()

    def save(self):
        """updates the attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.utcnow()
class Products(Base, dec_base):

    __tablename__ = 'products'
    name = Column(String(length=50), nullable=False, unique=True)
    category = Column(String(length=50), nullable=False)
    brand = Column(String(length=50), nullable=False)
    price = Column(Float(), nullable=False)
    rating = Column(Float())
    in_stock = Column(Boolean(), nullable=False)
    discount = Column(Float())
    stock_quantity = Column(Integer(), nullable=False)
    barcode = Column(String(length=40), nullable=False, unique=True)
    description = Column(String(length=1024), nullable=False, unique=True)
    about = Column(String(length=2048))
    img_list = Column(String(length=4096), nullable=False, default="")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Validations for positional arguments
        # Validations for positional arguments
        if args:
            if len(args) != 12:
                raise ValueError("Incorrect number of positional arguments")
            self.name = self._validate_name(args[0])
            self.category = self._validate_category(args[1])
            self.brand = self._validate_brand(args[2])
            self.price = self._validate_price(args[3])
            self.rating = self._validate_rating(args[4])
            self.in_stock = self._validate_in_stock(args[5])
            self.discount = self._validate_discount(args[6])
            self.stock_quantity = self._validate_stock_quantity(args[7])
            self.barcode = self._validate_barcode(args[8])
            self.description = self._validate_description(args[9])
            self.about = self._validate_about(args[10])
            self.img_list = self._validate_img_list(args[11])

            # Other validations for positional arguments...

        # Validations for keyword arguments
        else:
            self.name = self._validate_name(kwargs.get('name'))
            self.category = self._validate_category(kwargs.get('category'))
            self.brand = self._validate_brand(kwargs.get('brand'))
            self.price = self._validate_price(kwargs.get('price'))
            self.rating = self._validate_rating(kwargs.get('rating'))
            self.in_stock = self._validate_in_stock(kwargs.get('in_stock'))
            self.discount = self._validate_discount(kwargs.get('discount'))
            self.stock_quantity = self._validate_stock_quantity(kwargs.get('stock_quantity'))
            self.barcode = self._validate_barcode(kwargs.get('barcode'))
            self.description = self._validate_description(kwargs.get('description'))
            self.about = self._validate_about(kwargs.get('about'))
            self.img_list = self._validate_img_list(kwargs.get('img_list'))
    """
  # Adjusted validation and assignment for in_stock and stock_quantity
            self._validate_in_stock_and_stock_quantity(self.in_stock, self.stock_quantity)

            # Validate each attribute
            self._validate_name(self.name)
            self._validate_category(self.category)
            self._validate_brand(self.brand)
            self._validate_price(self.price)
            self._validate_rating(self.rating)
            self._validate_discount(self.discount)
            self._validate_barcode(self.barcode)
            self._validate_description(self.description)
            self._validate_about(self.about)
            self._validate_img_list(self.img_list)
    """
    # Adjusted validation and assignment method for in_stock and stock_quantity
    def _validate_stock_quantity(self ,value):
        if value is None:
            raise ValueError("Stock quantity cannot be None")
        if not isinstance(value, int):
            raise TypeError("Stock quantity must be an integer")
        return value

    def _validate_in_stock(self, value):
        value = self.stock_quantity > 0
        return value

    # Validation methods
    def _validate_name(self, value):
        if value is None:
            raise ValueError("Name cannot be None")
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if len(value) > 50:
            raise ValueError("Name must be 50 characters or fewer")
        return (value)

    def _validate_category(self, value):
        if value is None:
            raise ValueError("Category cannot be None")
        if not isinstance(value, str):
            raise TypeError("Category must be a string")
        if len(value) > 50:
            raise ValueError("Category must be 50 characters or fewer")
        return value

    def _validate_brand(self, value):
        if value is None:
            raise ValueError("Brand cannot be None")
        if not isinstance(value, str):
            raise TypeError("Brand must be a string")
        if len(value) > 50:
            raise ValueError("Brand must be 50 characters or fewer")
        return value

    def _validate_price(self, value):
        if value is None:
            raise ValueError("Price cannot be None")
        if not isinstance(value, float):
            raise TypeError("Price must be a float")
        return value

    def _validate_rating(self, value):
        if value is None:
            return None
        if value is not None and not isinstance(value, float):
            raise TypeError("Rating must be a float")
        return value

    def _validate_discount(self, value):
        if value is not None and not isinstance(value, float):
            raise TypeError("Discount must be a float")
        return value

    def _validate_barcode(self, value):
        if value is None:
            return  str(uuid.uuid4())
        if not isinstance(value, str):
            raise TypeError("Barcode must be a string")
        if len(value) > 40:
            raise ValueError("Barcode must be 40 characters or fewer")
        if len(value) == 0:
            raise ValueError("Barcode must not be an empty string")
        return value

    def _validate_description(self, value):
        if value is None:
            raise ValueError("Description cannot be None")
        if not isinstance(value, str):
            raise TypeError("Description must be a string")
        if len(value) > 1024:
            raise ValueError("Description must be 1024 characters or fewer")
        return value

    def _validate_about(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("About must be a string")
        if value is not None and len(value) > 2048:
            raise ValueError("About must be 2048 characters or fewer")
        return value

    def _validate_img_list(self, value):
        if value is None:
            raise ValueError("Img_list cannot be None")
        if not isinstance(value, list):
            raise TypeError("Img_list must be a list")
        if len(value) == 0:
            raise ValueError("Img_list must not be an empty list")
        # convert list into to string
        return ",".join(value) if value else ""

    # Getter method to retrieve img_list as a list
    def get_img_list(self):
        # print(self.__dict__.keys())
        # Str = self.img_list
        # print(Str)
        return [] if not self.img_list else self.img_list.split(",")

    # Setter method to store img_list as a string in the database
    @staticmethod
    def set_img_list(value):
        return ",".join(value) if value else ""

    def to_dict(self, save_fs=None):
        new_dict = super().to_dict(save_fs)
        new_dict["img_list"] = self.get_img_list()
        return new_dict


if __name__ == "__main__":
    # Create multiple Products instances
    product_data = {
        "name": "nokia 10 pureView",
        "category": "Electronics - smart phones ",
        "brand": "Nokia",
        "price": 99.99,
        "stock_quantity": 50,
        "rating": 4.5,
        "discount": 10.0,
        "in_stock": True,  # Change this key to "in_stock"
        "description": "Summary Nokia 10 PureView ram 8 GB camera 16 MP + 8 MP + 12 MP +12 MP display 6.1 inches (15.49 cm) performance Qualcomm Snapdragon 875 storage 128 GB battery 4000 mAh",
        "about": "More information about the sample product.",
        "img_list": [
            "/static/images/market/nokia_10_pureview.jfif",
            "/static/images/market/nokia_10_pureview.jfif",
        ]
    }
    # Use the created instances to create new instances
    prdct_inst1 = Products(**product_data)


    # Save products

    prdct_inst1.save()

    print(prdct_inst1.to_dict())



    @app.route("/tst")
    def tst_route():

        all_products = session.query(Products)
        products_dict_list = [product.to_dict() for product in all_products]

        return jsonify(products_dict_list)
    app.run(host='0.0.0.0', port=5006, debug=True)

    # Print the details of the new instances

