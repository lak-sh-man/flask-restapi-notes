# just like printing the class attributes or instance attributes doesn't fetch the data from table, it may only print the available data in local memory
# there are special methods available to access data from table in db

from BasicModelApp import db, Puppy, app

with app.app_context():
    # Create 
    puppy_1 = Puppy('Rufus',5)
    puppy_2 = Puppy('Nala',8)
    
    db.session.add(puppy_1)
    db.session.add(puppy_2)
    
    db.session.commit()

    