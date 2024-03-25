#!/usr/bin/env python3

from modules.base import Base
from Market import  Column, String, Float,Integer ,Boolean, ForeignKey, DateTime, dec_base,json

import uuid

from datetime import datetime


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
    # owner  = Column(String(40), ForeignKey('users.id'))

    # owner_id = Column(Integer, ForeignKey('users.id'))


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

    # def get_img_list(self):
    #     # print(self.__dict__.keys())
    #     # Str = self.img_list
    #     # print(Str)

    #     return [] if not self.img_list else self.img_list.split(",")
    def get_img_list(self):
        if isinstance(self.img_list, str):
            return self.img_list.split(",")
        else:
            return self.img_list


    # Setter method to store img_list as a string in the database
    @staticmethod
    def set_img_list(value):
        return ",".join(value) if value else ""

    def to_dict(self, save_fs=None):
        new_dict = super().to_dict(save_fs)
        new_dict["img_list"] = self.get_img_list()
        return new_dict
if __name__ == "__main__":
    product_data = {
        "name": "nokia 10 -pureView",
        "category": "Electronics - smart phones ",
        "brand": "Nokia",
        "price": 99.99,
        "stock_quantity": 50,
        "rating": 4.5,
        "discount": 10.0,
        "In_Stock": True,

        "description": "Summary -Nokia 10 PureView ram 8 GB camera 16 -MP + 8 MP + 12 MP +12 MP display 6.1 inches (15.49 cm) performance Qualcomm Snapdragon 875 storage 128 GB battery 4000 mAh",
        "about": "More information about the sample product.",
        "img_list": [
            "/static/images/market/nokia_10_pureview.jfif",
            "/static/images/market/nokia_10_pureview.jfif",
    ]
        }
    x = Products(**product_data)
    # x.created_at = str(x.created_at)
    # x.updated_at =str( x.updated_at)
    # print(x.__dict__)
    with open("tmp1.md", "a") as FILE:
        FILE.write("\n x.to_dict() \n")
        FILE.write(json.dumps(x.to_dict(), indent=4))
        # FILE.write("\n x.__dict__ \n")
        # FILE.write(json.dumps(x.__dict__, indent=4))

    x.save("DB")

    '''
    x = Products(**product_data)
    with open("tmp1.md", "ab") as FILE:
        FILE.write(b"\n x.to_dict() \n")
        pickle.dump(x.to_dict(), FILE)
        FILE.write(b"\n x.__dict__ \n")
        pickle.dump(x.__dict__, FILE)
    '''