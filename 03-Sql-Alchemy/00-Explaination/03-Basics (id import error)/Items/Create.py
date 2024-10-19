import sys
import os

# Get the parent directory (one level up from folder_1)
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the parent directory to the system path
sys.path.insert(0, parent_dir)

from BasicModelApp import db, ItemModel, app
from Stores.Create import store_1, store_2

with app.app_context():
    # Create 
    item_1 = ItemModel('Biriyani',230,store_1.id)
    item_2 = ItemModel('Pepper Chicken',260,store_1.id)
    item_3 = ItemModel('Chicken Manchurian',140,store_2.id)
    item_4 = ItemModel('Parotta',25,store_2.id)
    
    db.session.add(item_1)
    db.session.add(item_2)
    db.session.add(item_3)
    db.session.add(item_4)
    
    db.session.commit()

    