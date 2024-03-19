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

    # prdct_inst1.save(save_option="DB")

    # print(prdct_inst1.to_dict())


    # all_products = session.query(Products).all()
    # print(f"\n\n {all_products}")

    @app.route("/tst")
    def tst_route():

        all_products = session.query(Products).all()
        print(f"\n\n {all_products}")
        products_dict_list = [product.to_dict() for product in all_products]

        return jsonify(products_dict_list)
    app.run(host='0.0.0.0', port=5006, debug=True)

    # Print the details of the new instances

