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
    # Read
    # Note lots of ORM filter options here.   
    # filter(), filter_by(), limit(), order_by(), group_by()
    # Also lots of executor options
    # all(), first(), get(), count(), paginate()

    all_puppies = Puppy.query.all() # .all() returns a list  
                                    # fetches all rows from the puppies table.
                                    # SQLAlchemy creates Puppy objects for each row under class puppy
                                    # then three times __init__ is called when the list of object is read 
                                    # then when trying to pring __repr__ is called 
                                    # all_puppies = [Puppy(name='Sammy', age=3),
                                    #                Puppy(name='Frankie', age=4),
                                    #                Puppy(name='Rufus', age=5)]
                                    # similarly think for others

    print("----------->", all_puppies)

    # Grab by id    
    puppy_one = Puppy.query.get(1) # puppy_one = Puppy(name='Sammy', age=3)
    print("----------->", puppy_one)
    print("----------->", puppy_one.name)

    # Filters
    puppy_sam = Puppy.query.filter_by(name='Frankie') # here filtering only occurs
    print("----------->", puppy_sam)                  # this prints the SQL code
    print("----------->", puppy_sam.all())            # .all() returns a list of filtered query
                                                      # puppy_sam = [ Puppy(name='Frankie', age=4) ] 
    
