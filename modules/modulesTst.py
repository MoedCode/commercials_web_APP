#!/usr/bin/env python3
import uuid
# from Market import session, Column, String, Float,Integer ,Boolean, ForeignKey, DateTime

from datetime import datetime

import ast
import os
from modules.base import Base
from Market import session, Column, String, Float,Integer ,Boolean, ForeignKey,  dec_base, relationship
from Market import DateTime, dec_base,json,re, DEBUG


time = "%Y-%m-%dT%H:%M:%S.%f"


class Base2:

    __tablename__ = 'base2'
    id = Column(String(length=40), nullable=False, unique=True, primary_key=True)
    created_at = Column(String(length=50), nullable=False, unique=True)
    updated_at = Column(String(length=50), nullable=False, unique=True)
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
            new_dict["created_at"] = new_dict["created_at"].strftime(time)
            # new_dict["created_at"] = new_dict["created_at"]
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
            # new_dict["updated_at"] = new_dict["updated_at"]
        new_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        return new_dict

    def save(self, save_option="both"):
        self.updated_at = datetime.utcnow().strftime(time)
        self.created_at = str(self.created_at)
        self.updated_at = str(self.updated_at)
        if save_option in ["local", "both"]:
            from modules.engine.local_storage import LocalStorage
            local_storage = LocalStorage()
            local_storage.add(self)
            local_storage.commit()
        if save_option in ["DB", "both"]:
            session.add(self)
            session.commit()



class Products2(Base2, dec_base):

    __tablename__ = 'products2'
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
    owner = Column(String(40), ForeignKey('users2.id'))




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

class Users2(Base, dec_base):
    __keys =  {"email", "password", "first_name", "last_name", "nickname", "budget", "image"}

    __tablename__ = "users2"

    # Define columns with validation in setters
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    nickname = Column(String(128), nullable=True)
    budget = Column(Integer(), nullable=False, default=5000)
    image = Column(String(150), nullable=True)
    products = relationship("Products2", backref="owner_user")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # positional Arguments
        if args:
            if len(args) < 2:
                print(f"{__class__.__name__} missing arguments")
                print(f" File:{os.path.abspath(__file__)} ,( line: {inspect.currentframe().f_lineno})")
                exit(-1)
            if len(args) > 7:
                print(f"{__class__.__name__} to much arguments")
                print(f" File:{os.path.abspath(__file__)} ,( line: {inspect.currentframe().f_lineno})")
                exit(-1)

            self.email = self._validate_email(args[0])
            self.password = self._validate_password(args[1])
            self.first_name = self._validate_name(args[2] if len(args) >= 3 else None)
            self.last_name = self._validate_name(args[3] if len(args) >= 4 else None)
            self.nickname = self._validate_name(args[4] if len(args) >= 5 else None)
            self.budget = self._validate_budget(args[5] if len(args) >= 6 else 5000)
            self.image = self._validate_image(args[6] if len(args) >= 7 else None)
        if kwargs:
            for key in kwargs:
                if key not in Users2.__keys:
                    print(f"{__class__.__name__} :: unknown {key} \n{DEBUG}")
                    exit(-2)

            self.email = self._validate_email(kwargs["email"])
            self.password = self._validate_password(kwargs["password"])
            self.first_name = self._validate_name(kwargs["first_name"] if hasattr(kwargs, "first_name") else None)
            self.last_name = self._validate_name(kwargs["last_name"] if hasattr(kwargs, "first_name") else None)
            self.nickname = self._validate_name(kwargs["nickname"] if hasattr(kwargs, "nickname") else None)
            self.budget = self._validate_budget( kwargs["budget"] if hasattr(kwargs, "budget") else None)
            self.image = self._validate_image( kwargs["image"] if hasattr(kwargs, "image") else None)



    # define vallation methods
    def _validate_email(self, value):
        if not isinstance(value, str):
            raise ValueError("Email must be a string")

        # Regular expression pattern for email validation
        email_pattern = r"^[a-zA-Z0-9._%+-]+@(?:gmail|yahoo|outlook|zoho|protonmail)\.(?:com|net|org)$"

        if not re.match(email_pattern, value):
            valid_platforms = ["gmail", "yahoo Mail", "outlook", "zoho Mail", "protonMail"]
            platforms_str = ", ".join(valid_platforms)
            raise ValueError(f"Invalid email format or domain. Valid email platforms are: {platforms_str}")
        return value
    def _validate_name(self, value):
        if value is  None:
            return "untitled"
        if not isinstance(value, str):
             return  str(value)
        if value.replace(" ", "") == "":
            return  "untitled"
        if len(value) > 128:
                raise ValueError("First, last, name and nickname length cannot exceed 128 characters")
        return value
   # password vallation
    def _validate_password(self, value):
        if value is None:
            raise ValueError("Password is required")
        if not isinstance(value, str):
            raise TypeError("Password must be a string")
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long")
        if not re.search(r'[A-Z]', value):
            raise ValueError("Password must contain at least one uppercase letter")
        if not re.search(r'[a-z]', value):
            raise ValueError("Password must contain at least one lowercase letter")
        if not re.search(r'\d', value):
            raise ValueError("Password must contain at least one digit")
        if not re.search(r'[@#$%^&+=]', value):
            raise ValueError("Password must contain at least one special character from '@#$%^&+='")
        if re.search(r'\s', value):
            raise ValueError("Password cannot contain whitespace characters")
        return value


    # budget validation
    def _validate_budget(self, value):
        if value is None:
            value = 5000
        if not isinstance(value, int):
            raise ValueError("Budget must be an integer")
        return value


    def _validate_image(self, value):
        if value is not None:
            if not isinstance(value, str):
                raise ValueError("Image must be a string")
            if len(value) > 150:
                raise ValueError("Image length cannot exceed 150 characters")
        return value
if __name__ == "__main__":
    # userx = Users2("userx@gmail", "Zz123456@x")
    userx = Users2("userx@gmail.com", "Zz123456@x")
    dictx = {
            "name": "Earbuds2",
            "category": "Electronics",
            "brand": "Brand X",
            "price": 149.99,
            "stock_quantity": 30,
            "rating": 4.2,
            "discount": 0.0,
            "in_stock": True,
            "description": "Description2 for Earbuds.",
            "about": "More information about Earbuds.",
            "img_list": [
                "/static/images/market/earpods0.jfif",
                "/static/images/market/earpods1.jfif",
                "/static/images/market/earpods2.jfif"
            ]
    }
    productx = Products2(**dictx)
    userx.products.append(productx)
    userx.save("DB")
    productx.save("DB")
    print(f":: Userx {userx.to_dict()} \n\n :: product {productx.to_dict()}")
