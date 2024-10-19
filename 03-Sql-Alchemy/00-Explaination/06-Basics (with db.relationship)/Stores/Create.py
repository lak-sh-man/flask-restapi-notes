import sys
import os

# Get the parent directory (one level up from folder_1)
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the parent directory to the system path
sys.path.insert(0, parent_dir)

from BasicModelApp import db, StoreModel, app

with app.app_context():
    # Create 
    store_1 = StoreModel(name="SS")
    store_2 = StoreModel(name="Cheap & Best")
    
    db.session.add(store_1)
    db.session.add(store_2)
    
    db.session.commit()
    