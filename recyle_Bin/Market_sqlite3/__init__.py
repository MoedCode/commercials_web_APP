from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
database_path = os.path.join(current_dir, 'market.db')
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{database_path}'
db = SQLAlchemy(app)

from Market import routes