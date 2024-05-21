#!/usr/bin/env python3
from modules.base_module import BaseModules
import uuid

class Product(BaseModules):
    """Class representing a product in a commercial web application."""
    isAClass = True

    def __init__(self, name, barcode=None, category=None, description=None, price=None, discount=None, stock_quantity=None, brand=None, rating=None, in_stock=None, img_list=None, *args, **kyWrdArgs):
        """
        Initialize a Product object.

        Parameters:
        - name (str): The name of the product.
        - barcode (str, optional): The barcode of the product. If not provided, a UUID will be generated.
        - category (str, optional): The category of the product.
        - description (str, optional): The description of the product.
        - price (float, optional): The price of the product.
        - discount (float, optional): The discount applied to the product.
        - stock_quantity (int, optional): The quantity of the product in stock.
        - brand (str, optional): The brand of the product.
        - rating (float or int or None, optional): The rating of the product. If not provided, set to None.
        - in_stock (bool, optional): Whether the product is in stock.
        - img_list (list, optional): List of image URLs associated with the product.
        - *args, **kyWrdArgs: Additional arguments passed to the BaseModules class.
        """
        super().__init__(*args, **kyWrdArgs)
        self.set_attributes(name, barcode, category, description, price, discount, stock_quantity, brand, rating, in_stock, img_list)

    def set_attributes(self, name, barcode, category, description, price, discount, stock_quantity, brand, rating, in_stock, img_list):
        """Set the attributes of the product with validation."""
        self.name = name
        self.barcode = barcode
        self.category = category
        self.description = description
        self.price = price
        self.discount = discount
        self.stock_quantity = stock_quantity
        self.brand = brand
        self.rating = rating
        self.in_stock = in_stock
        self.img_list = img_list
    # Getter and Setter for 'name'
    @property
    def name(self):
        """Get the name of the product."""
        return self.name

    @name.setter
    def name(self, value):
        """Set the name of the product with validation."""
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        self.name = value

    # Getter and Setter for 'barcode'
    @property
    def barcode(self):
        """Get the barcode of the product."""
        if self.barcode is None:
            # Generate barcode if not provided
            self.barcode = str(uuid.uuid4())
        return self.barcode

    @barcode.setter
    def barcode(self, value):
        """Set the barcode of the product with validation."""
        if value is not None and not isinstance(value, (str, int)):
            raise ValueError("Barcode must be a string or integer")
        self.barcode = str(value) if value is not None else str(uuid.uuid4())

    # Getter and Setter for 'category'
    @property
    def category(self):
        """Get the category of the product."""
        return self.category

    @category.setter
    def category(self, value):
        """Set the category of the product with validation."""
        if not isinstance(value, str):
            raise ValueError("Category must be a string")
        self.category = value

    # Getter and Setter for 'description'
    @property
    def description(self):
        """Get the description of the product."""
        return self.description

    @description.setter
    def description(self, value):
        """Set the description of the product with validation."""
        if not isinstance(value, str):
            raise ValueError("Description must be a string")
        self.description = value

    # Getter and Setter for 'price'
    @property
    def price(self):
        """Get the price of the product."""
        return self.price

    @price.setter
    def price(self, value):
        """Set the price of the product with validation."""
        if not isinstance(value, (int, float)):
            raise ValueError("Price must be a numeric value")
        self.price = value

    # Getter and Setter for 'discount'
    @property
    def discount(self):
        """Get the discount applied to the product."""
        return self.discount

    @discount.setter
    def discount(self, value):
        """Set the discount applied to the product with validation."""
        if not isinstance(value, (int, float)):
            raise ValueError("Discount must be a numeric value")
        self.discount = value

    # Getter and Setter for 'stock_quantity'
    @property
    def stock_quantity(self):
        """Get the stock quantity of the product."""
        return self.stock_quantity

    @stock_quantity.setter
    def stock_quantity(self, value):
        """Set the stock quantity of the product with validation."""
        if not isinstance(value, int):
            raise ValueError("Stock quantity must be an integer")
        self.stock_quantity = value

    # Getter and Setter for 'brand'
    @property
    def brand(self):
        """Get the brand of the product."""
        return self.brand

    @brand.setter
    def brand(self, value):
        """Set the brand of the product with validation."""
        if not isinstance(value, str):
            raise ValueError("Brand must be a string")
        self.brand = value

    # Getter and Setter for 'rating'
    @property
    def rating(self):
        """Get the rating of the product as a string or None if not set."""
        return str(self.rating) if self.rating is not None else None

    @rating.setter
    def rating(self, value):
        """Set the rating of the product, convert to string if int or float."""
        if value is not None:
            if isinstance(value, (int, float)):
                value = str(value)
            else:
                raise ValueError("Rating must be a numeric value")
        self.rating = value

    # Getter and Setter for 'in_stock'
    @property
    def in_stock(self):
        """Check if the product is in stock."""
        return self.in_stock

    @in_stock.setter
    def in_stock(self, value):
        """Set whether the product is in stock with validation."""
        if not isinstance(value, bool):
            raise ValueError("In stock must be a boolean")
        self.in_stock = value

    # Getter and Setter for 'img_list'
    @property
    def img_list(self):
        """Get the list of image URLs associated with the product."""
        return self.img_list

    @img_list.setter
    def img_list(self, value):
        """Set the list of image URLs associated with the product with validation."""
        if not isinstance(value, list):
            raise ValueError("Image list must be a list")
        self.img_list = value


if __name__ == "__main__":
    Product_obj = {
        "name": "Phone",
        "category": "Electronics",
        "description": "Smartphone with advanced features",
        # "barcode": None,
        "price": 501,
        "discount": 10,
        "stock_quantity": 50,
        "brand": "BrandA",
        "rating": 4.5,
        "in_stock": True,
        "img_list": [
            "static/images/market/Camera0.jfif",
            "static/images/market/Camera0.jfif",
            "static/images/market/Camera0.jfif",
            "static/images/market/Camera0.jfif",
            "static/images/market/Camera0.jfif",
            "static/images/market/Camera0.jfif",
            "static/images/market/Camera0.jfif",
            "static/images/market/Camera0.jfif",
            "static/images/market/Camera0.jfif",
        ]}
    x = Product(**Product_obj)
    # print(x.__dict__)
    # print(x.__class__)
    x.save()
