#!/usr/bin/env python3

from modules.base import Base
from modules.products import Products
from Market import session, Column, String, Float,Integer ,Boolean, ForeignKey, DateTime, dec_base

import re

class Users(Base, dec_base):
    __tablename__ = "users"

    # Define columns with validation in setters
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    nickname = Column(String(128), nullable=True)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    budget = Column(Integer(), nullable=False, default=5000)
    image = Column(String(150), nullable=True)
    # product = relationship('Products', backref="Owner", lazy=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if args and len(args) >= 2:
            self.email = args[0]
            self.password = args[1]
            self.first_name = args[2] if len(args) >= 3 else None
            self.last_name = args[3] if len(args) >= 4 else None
            self.nickname = args[4] if len(args) >= 5 else None
            self.budget = args[5] if len(args) >= 6 else None

        else:
            print(f"{__class__.__name__} missing arguments")


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
        if value is None:
            value = 5000
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
    def test():
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
    x = Users("user@gmail.com", "First0", "last0", "PWD0")
    print(x.to_dict())