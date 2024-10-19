import sys
import os

# Get the parent directory (one level up from folder_1)
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the parent directory to the system path
sys.path.insert(0, parent_dir)

from BasicModelApp import db, StoreModel, app

with app.app_context():
    # Query a store
    store = StoreModel.query.get(1)  # Get store with id=1

    # Access the related items using the relationship
    items = store.items

    print(f"Store: {store.name}")
    for item in items:
        print(f"Item: {item.name}, Price: {item.price}")
