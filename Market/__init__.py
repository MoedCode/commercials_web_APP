#!/usr/bin/env python3
import os
import uuid
from sys import argv
from flask import Flask, render_template, jsonify, redirect, make_response, request, abort, redirect, url_for
from sqlalchemy import create_engine, Column, String, Float, Boolean, Integer, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime
import json
import inspect

import ast
import os
import re
DEBUG = f" File:{os.path.abspath(__file__)} ,( line: {inspect.currentframe().f_lineno})"
DEBUG_ = f"{os.path.basename(__file__)} , line {inspect.currentframe().f_lineno}\n{__file__}\n {os.path.abspath(__file__)}"

app = Flask(__name__)
# app.secret_key = 'ProMarket_SK'
app.config['SECRET_KEY'] = 'a917ead3a9f56eaf1fbc1605273cb71bee52598c26eb9149f3b09a16eafe'
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


from Market import routes
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{database_path}'
# db = SQLAlchemy(app)
