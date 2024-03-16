#!/usr/bin/env python3
from Market import db
from modules.base import Base
from modules.products import Products
class Users(Base, db.Model):
    __tablename__ = "users"
    first_name = db.Column(db.String(128), nullable=True)
    last_name = db.Column(db.String(128), nullable=True)
    nickname = db.Column(db.String(128), nullable=True)
    email = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=5000)
    image = db.Column(db.String(150), nullable=True)
    product = db.relationship('Products', backref="Owner", lazy=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
if __name__ == "__main__":
    x = Users()
    print(x.__dict__)