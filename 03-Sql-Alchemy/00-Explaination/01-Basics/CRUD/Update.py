# just like printing the class attributes or instance attributes doesn't fetch the data from table, it may only print the available data in local memory
# there are special methods available to access data from table in db

import sys
import os

# Get the parent directory (one level up from folder_1)
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the parent directory to the system path
sys.path.insert(0, parent_dir)

from BasicModelApp import db, Puppy, app

with app.app_context():
    # update
    first_puppy = Puppy.query.get(1)
    first_puppy.age = 10            # Here mapping occurs 
    db.session.add(first_puppy)
    db.session.commit()

