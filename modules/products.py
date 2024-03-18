
from modules.base import Base
from Market import db
import uuid




class Products(Base, db.Model):
    __tablename__ = 'products'
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
    # owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
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
    from modules import product_data
    from Market import app
    app.app_context().push()
    product_data = {
        "name": "pc_all_in_one-Altra24 ",
        "category": "Electronics - pc_all_in_one ",
        "brand": "Toshiba",
        "price": 150.0,
        "stock_quantity": 50,
        "rating": 4.5,
        "discount": 10.0,
        "In_Stock": True,

        "description": "pc_all_in_one-Altra24 PureView ram 64 GB camera 16 MP + 8 MP + 12 MP +12 MP display 60.1 inches (15.49 cm) performance Qualcomm Snapdragon 875 storage 1 TB ssd 4TB HDD ",
        "about": "More information about the sample product.",
        "img_list": [
            "/Market/static/images/market/pc_all_in_one0.jfif",
            "/Market/static/images/market/pc_all_in_one1.jfif",
            "/Market/static/images/market/pc_all_in_one2.jfif",

    ]
        }


    x = Products(**product_data)

    print(x.img_list)
    x.save("DB")

"""

class Products(Base, db.Model):
    __tablename__ = 'products'
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value is None:
            raise ValueError("Name cannot be None")
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if len(value) > 50:
            raise ValueError("Name must be 50 characters or fewer")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if value is None:
            raise ValueError("Category cannot be None")
        if not isinstance(value, str):
            raise TypeError("Category must be a string")
        if len(value) > 50:
            raise ValueError("Category must be 50 characters or fewer")
        self._category = value

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if value is None:
            raise ValueError("Brand cannot be None")
        if not isinstance(value, str):
            raise TypeError("Brand must be a string")
        if len(value) > 50:
            raise ValueError("Brand must be 50 characters or fewer")
        self._brand = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value is None:
            raise ValueError("Price cannot be None")
        if not isinstance(value, float):
            raise TypeError("Price must be a float")
        self._price = value

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        if value is not None and not isinstance(value, float):
            raise TypeError("Rating must be a float")
        self._rating = value

    @property
    def In_Stock(self):
        return self._In_Stock

    @In_Stock.setter
    def In_Stock(self, value):
        if value is None:
            raise ValueError("In_Stock cannot be None")
        self._In_Stock = value if value is not None else self.stock_quantity > 0

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if value is not None and not isinstance(value, float):
            raise TypeError("Discount must be a float")
        self._discount = value

    @property
    def stock_quantity(self):
        return self._stock_quantity

    @stock_quantity.setter
    def stock_quantity(self, value):
        if value is None:
            raise ValueError("Stock quantity cannot be None")
        if not isinstance(value, int):
            raise TypeError("Stock quantity must be an integer")
        self._stock_quantity = value

    @property
    def barcode(self):
        return self._barcode

    @barcode.setter
    def barcode(self, value):
        if value is None:
            raise ValueError("Barcode cannot be None")
        if not isinstance(value, str):
            raise TypeError("Barcode must be a string")
        if len(value) != 40:
            raise ValueError("Barcode must be 40 characters long")
        self._barcode = value if value is not None else str(uuid.uuid4())

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if value is None:
            raise ValueError("Description cannot be None")
        if not isinstance(value, str):
            raise TypeError("Description must be a string")
        if len(value) > 1024:
            raise ValueError("Description must be 1024 characters or fewer")
        self._description = value

    @property
    def about(self):
        return self._about

    @about.setter
    def about(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("About must be a string")
        if value is not None and len(value) > 2048:
            raise ValueError("About must be 2048 characters or fewer")
        self._about = value

    @property
    def img_list(self):
        return self.img_list

    @img_list.setter
    def img_list(self, value):
        if value is None:
            raise ValueError("Img_list cannot be None")
        if not isinstance(value, list):
            raise TypeError("Img_list must be a list")
        self.img_list = ",".join(value) if value else ""

if __name__ == "__main__":
        # Create multiple Products instances
    product1 = Products(name="Product 1", category="Category 1", brand="Brand 1", price=10.99,
                        stock_quantity=100, description="Description 1")
    product2 = Products(name="Product 2", category="Category 2", brand="Brand 2", price=20.99,
                        stock_quantity=200, description="Description 2")
    product3 = Products(name="Product 3", category="Category 3", brand="Brand 3", price=30.99,
                        stock_quantity=300, description="Description 3")

    # Use the created instances to create new instances
    new_product1 = Products(name=product1.name, category=product1.category, brand=product1.brand,
                            price=product1.price, stock_quantity=product1.stock_quantity,
                            description=product1.description)
    new_product2 = Products(name=product2.name, category=product2.category, brand=product2.brand,
                            price=product2.price, stock_quantity=product2.stock_quantity,
                            description=product2.description)
    new_product3 = Products(name=product3.name, category=product3.category, brand=product3.brand,
                            price=product3.price, stock_quantity=product3.stock_quantity,
                            description=product3.description)

    # Print the details of the new instances
    print(new_product1.to_dict())
    print(new_product2.to_dict())
    print(new_product3.to_dict())

"""