#!/usr/bin/env python3
import inspect

import ast
import os
import phonenumbers
from modules.base import Base

from Market import session, Column, String, Float,Integer ,Boolean, ForeignKey, DateTime, dec_base, relationship,re, DEBUG

class Users(Base, dec_base):
    __keys =  {"email", "password", "first_name", "last_name", "nickname", "budget", "image"}

    __tablename__ = "users"

    # Define columns with validation in setters
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    nickname = Column(String(128), nullable=True)
    budget = Column(Integer(), nullable=False, default=5000)
    image = Column(String(150), nullable=True)
    products = relationship("Products", backref="Ownser")
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
                if key not in Users.__keys:
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

    def _validate_phone_number(self, value, country):
        if value is not None:
            raise ValueError("Phone number is required ")
        if country is None:
            country = self.country

        if not isinstance(value, str):
            value = str(value)

            # Parse the phone number
            try:
                parsed_number = phonenumbers.parse(value, country)
            except phonenumbers.phonenumberutil.NumberParseException as e:
                raise ValueError(f"Invalid phone number: {str(e)}")

            # Validate the phone number
            if not phonenumbers.is_valid_number(parsed_number):
                raise ValueError("Invalid phone number")
        return value
    def _validate_name(self, value):
        if value is  None:
            return "untitled"
        if not isinstance(value, str):
            value = str(value)
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

    '''
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):


        self._email = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self.__password = value

    @property
    def budget(self):
        return self._budget

    @budget.setter
    def budget(self, value):

        self._budget = value

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):

        self._image = value
'''
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
    # x = Users(email="user0@gmail.com", password="PWD0",first_name="First0", last_name="last0" )
    # x0 = Users("zikoAlJoker@gmail.com","ZikaJok@24","0x500", "last0" )
    # x1 = Users(email="zikoAlJoker@gmail.com",password="ZikaJok@24", nickname="ZikA Al joker", image="/static/images/users/openart-image_3vS15JnT_1710954202493_raw.jpg")

    # x0.save("DB")
    # print(x0.to_dict())
    # print()
    # print()
    # print(x1.to_dict())
    # print()
    # print()
    # print(x0.__password)
    # print(x1.__password)