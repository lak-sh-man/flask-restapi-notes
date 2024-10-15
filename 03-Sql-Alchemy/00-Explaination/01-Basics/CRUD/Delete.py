# just like printing the class attributes or instance attributes doesn't fetch the data from table, it may only print the available data in local memory
# there are special methods available to access data from table in db

# NOTE : Usually after querying the data with special methods from data base, they are made to override the instance attributes (etc) inside class to print it anywhere
# NOTE : some attributes can be accessed becaues they are inside __init___() where we pass the arguments while declaring the objects
# NOTE : for relationship attributes - it is different

from BasicModelApp import db, Puppy, app

with app.app_context():
    # Create 
    my_puppy = Puppy('Rufus',5)
    db.session.add(my_puppy)
    db.session.commit()

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
    
    # update
    first_puppy = Puppy.query.get(1)
    first_puppy.age = 10
    db.session.add(first_puppy)
    db.session.commit()

    # delete
    second_pup = Puppy.query.get(2)
    db.session.delete(second_pup)
    db.session.commit()

    # Check for changes:
    all_puppies = Puppy.query.all() # list of all puppies in table
    print("----------->", all_puppies)
