
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

