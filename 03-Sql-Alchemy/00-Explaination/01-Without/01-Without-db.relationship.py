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
    name = db.Column(db.String(80), unique=True, nullable=False)


class ItemModel(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), nullable=False)


    def __init__(self,name,price,store_id):
        self.name = name
        self.price = price
        self.store_id = store_id


with app.app_context():
    my_item = ItemModel('Pen',50)
    db.session.add(my_item)
    db.session.commit()
    
    
    item_1 = ItemModel.query.get(1)  # Get an item with ID 1


    # Without relationship, you need to manually query the store
    store = StoreModel.query.get(item_1.store_id)  # Find the store using the store_id
    print(f"Item: {item_1.name}, Store: {store.name}")  # Manually accessing the store
