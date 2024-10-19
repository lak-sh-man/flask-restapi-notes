import sys
import os

# Get the parent directory (one level up from folder_1)
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the parent directory to the system path
sys.path.insert(0, parent_dir)

from BasicModelApp import db, ItemModel, app

with app.app_context():
    # Query an item
    item = ItemModel.query.get(2)  # Get item with id=2

    # Access the related store directly using the relationship
    store = item.store

    print(f"Item: {item.name}, Price: {item.price}")
    print(f"Store: {store.name}")
