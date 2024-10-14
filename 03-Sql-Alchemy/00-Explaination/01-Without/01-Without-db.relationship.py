import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# This grabs our directory
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

# Connects our Flask App to our Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()

# Store Model
class StoreModel(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

# Item Model
class ItemModel(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)

    # Foreign key to link with stores
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), nullable=False)

# Usage
item = ItemModel.query.get(1)  # Get an item with ID 1

# Without relationship, you need to manually query the store
store = StoreModel.query.get(item.store_id)  # Find the store using the store_id
print(f"Item: {item.name}, Store: {store.name}")  # Manually accessing the store
