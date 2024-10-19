import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class StoreModel(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)
    """1) when already existing store name is tried to be inserted, error occurs when unique = True is given,
          which means duplicate values cannot be stored under this column
       2) Remember there is no unique=Flase, either we can give unique=True or we should not even mention it"""
    name = db.Column(db.String(80), nullable=False) 
    items = db.relationship("ItemModel", back_populates="store") 

class ItemModel(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    """Here for name and price no unique = True is given because different stores can have 
       same item, under same name, under same price which means duplicate values can be stored under this column"""
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), nullable=False)
    store = db.relationship("StoreModel", back_populates="items")


    def __init__(self,name,price,store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

with app.app_context():
    db.create_all() # this creates the sqlite file first of all for us to later add and commit data 

