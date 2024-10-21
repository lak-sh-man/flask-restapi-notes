from db import db


class ItemModel(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    price = db.Column(db.Float(precision=2), unique=False, nullable=False)
    """Trying to delete a store, which has items present in it, will result in error because in StoreModel table
       everything can be deleted but the id column of StoreModel is referenced by store_id column in ItemModel table 
       which has nullable = False on that column"""
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), unique=False, nullable=False)
    store = db.relationship("StoreModel", back_populates="items")
