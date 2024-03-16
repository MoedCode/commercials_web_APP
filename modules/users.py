#!/usr/bin/env python3
from Market import db
from modules.base import Base
from modules.products import Products
import re

class Users(Base, db.Model):
    __tablename__ = "users"

    # Define columns with validation in setters
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

    # Define setters with validation for each attribute
    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if value is not None:
            if not isinstance(value, str):
                raise ValueError("First name must be a string")
            if len(value) > 128:
                raise ValueError("First name length cannot exceed 128 characters")
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if value is not None:
            if not isinstance(value, str):
                raise ValueError("Last name must be a string")
            if len(value) > 128:
                raise ValueError("Last name length cannot exceed 128 characters")
        self._last_name = value

    @property
    def nickname(self):
        return self._nickname

    @nickname.setter
    def nickname(self, value):
        if value is not None:
            if not isinstance(value, str):
                raise ValueError("Nickname must be a string")
            if len(value) > 128:
                raise ValueError("Nickname length cannot exceed 128 characters")
        self._nickname = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not isinstance(value, str):
            raise ValueError("Email must be a string")

        # Regular expression pattern for email validation
        email_pattern = r"^[a-zA-Z0-9._%+-]+@(?:gmail|yahoo|outlook|zoho|protonmail)\.(?:com|net|org)$"

        if not re.match(email_pattern, value):
            valid_platforms = ["Gmail", "Yahoo Mail", "Outlook", "Zoho Mail", "ProtonMail"]
            platforms_str = ", ".join(valid_platforms)
            raise ValueError(f"Invalid email format or domain. Valid email platforms are: {platforms_str}")

        self._email = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if not isinstance(value, str):
            raise ValueError("Password must be a string")
        self._password = value

    @property
    def budget(self):
        return self._budget

    @budget.setter
    def budget(self, value):
        if not isinstance(value, int):
            raise ValueError("Budget must be an integer")
        self._budget = value

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        if value is not None:
            if not isinstance(value, str):
                raise ValueError("Image must be a string")
            if len(value) > 150:
                raise ValueError("Image length cannot exceed 150 characters")
        self._image = value

if __name__ == "__main__":
    # Valid email
    valid_email = "user@gmail.com"
    # Invalid email with an unsupported domain
    invalid_email = "user@example.com"

    try:
        # Creating a user with a valid email
        user1 = Users(email=valid_email)
        print("User created successfully with valid email:", user1.email)
    except ValueError as e:
        print("Error creating user:", e)

    try:
        # Attempting to create a user with an invalid email
        user2 = Users(email=invalid_email)
        print("User created successfully with invalid email:", user2.email)
    except ValueError as e:
        print("Error creating user:", e)