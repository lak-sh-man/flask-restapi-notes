import sys
import os

# Get the parent directory (one level up from folder_1)
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the parent directory to the system path
sys.path.insert(0, parent_dir)

from BasicModelApp import db, Puppy, app

with app.app_context():
    # Create 
    sam = Puppy('Sammy',3)
    frank = Puppy('Frankie',4)
    ruf = Puppy('Rufus',5)
    
    db.session.add_all([sam,frank,ruf]) 
    db.session.commit()
