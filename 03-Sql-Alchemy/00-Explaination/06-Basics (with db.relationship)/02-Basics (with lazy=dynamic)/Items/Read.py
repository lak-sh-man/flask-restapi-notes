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
    # store = StoreModel.query.get(item.store_id) ------> It is being alternated
    store = item.store # provides the single StoreModel objects that matches the id of item 2

    try:
        # Attempt to use it like a query (which is incorrect)
        store = store.all()  # This will throw an error since it's not a collection
    except Exception as e:
        print(f"Error: {e}")

    print(f"Item: {item.name}, Price: {item.price}")
    print(f"Store: {store.name}")
                # OR
    print(f"Store: {item.store.name}") # This is just an another way to call without using "store = item.store"
