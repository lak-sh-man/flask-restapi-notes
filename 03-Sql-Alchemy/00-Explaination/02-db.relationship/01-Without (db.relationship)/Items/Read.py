import sys
import os

# Get the parent directory (one level up from folder_1)
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the parent directory to the system path
sys.path.insert(0, parent_dir)

from db import db, StoreModel, ItemModel, app

with app.app_context():
    # Read
    item_1 = ItemModel.query.get(2)  # Get an item with ID 1

    # Without relationship, you need to manually query the store
    store = StoreModel.query.get(item_1.store_id)  # Find the store using the store_id
    print(f"Item: {item_1.name}, Store: {store.name}")  # Manually accessing the store