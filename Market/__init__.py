from flask import Flask, jsonify, render_template
#!/usr/bin/env python3
import os
import uuid
from sys import argv
from flask import Flask, jsonify
from sqlalchemy import create_engine, Column, String, Float, Boolean, Integer, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime


app = Flask(__name__)
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
