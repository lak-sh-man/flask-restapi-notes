import sys
import os

# Get the parent directory (one level up from folder_1)
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the parent directory to the system path
sys.path.insert(0, parent_dir)

from BasicModelApp import db, StoreModel, ItemModel, app

"""No need to import these objects, we'll query the data base and assign it to a new object"""
# from Stores.Create import store_1, store_2 

with app.app_context():
    store_query_1 = StoreModel.query.get(1)
    store_query_2 = StoreModel.query.get(2)
    # Create 
    item_1 = ItemModel('Biriyani',230,store_query_1.id)
    item_2 = ItemModel('Pepper Chicken',260,store_query_1.id)
    item_3 = ItemModel('Chicken Manchurian',140,store_query_2.id)
    item_4 = ItemModel('Parotta',25,store_query_2.id)
    
    db.session.add(item_1)
    db.session.add(item_2)
    db.session.add(item_3)
    db.session.add(item_4)
    
    db.session.commit()

    