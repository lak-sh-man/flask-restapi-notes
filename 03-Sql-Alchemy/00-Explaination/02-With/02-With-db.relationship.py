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

    # One-to-Many relationship: Store has many items
    items = db.relationship("ItemModel", back_populates="store")

# Item Model
class ItemModel(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)

    # Foreign key to link with stores
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), nullable=False)

    # Define the relationship with StoreModel
    store = db.relationship("StoreModel", back_populates="items")

# Usage
item = ItemModel.query.get(1)  # Get an item with ID 1

# You can directly access the store details via the relationship
print(f"Item: {item.name}, Store: {item.store.name}")  # Automatically gets the store name
