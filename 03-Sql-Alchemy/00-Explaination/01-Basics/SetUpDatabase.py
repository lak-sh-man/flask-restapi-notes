from BasicModelApp import db, Puppy, app

sam = Puppy('Sammy',3)
frank = Puppy('Frankie',4)



"""accesses the auto created instance attribute that is only available in local memory when added and commited to db
   and do not access it from table Puppy"""
print(sam.id)                   # print None
"""accesses the instance attribute that is available in local memory becaues of __init__
   and do not access it from table Puppy"""
print(sam.name)                 # print Sammy
print(sam.age)                  # print 3


"""accesses the auto created instance attribute that is only available in local memory when added and commited to db
   and do not access it from table Puppy"""
print(frank.id)                 # print None
"""accesses the instance attribute that is available in local memory becaues of __init__
   and do not access it from table Puppy"""
print(frank.name)               # print Frankie
print(frank.age)                # print 4



with app.app_context():
    
    """these object declaration ensures the data that are about to be added in the respective table in db
       session add and commit is must to see the contents in tables just creation of objects doesn't add the 
       data in table row wise and no need to pass value for primary column of any table, it is automatically created"""
    sam = Puppy('Sammy',3)
    frank = Puppy('Frankie',4)


    """accesses the auto created instance attribute that is only available in local memory when added and commited to db
    and do not access it from table Puppy"""
    print(sam.id)                   # print None
    """accesses the instance attribute that is available in local memory becaues of __init__
    and do not access it from table Puppy"""
    print(sam.name)                 # print Sammy
    print(sam.age)                  # print 3


    """accesses the auto created instance attribute that is only available in local memory when added and commited to db
    and do not access it from table Puppy"""
    print(frank.id)                 # print None
    """accesses the instance attribute that is available in local memory becaues of __init__
    and do not access it from table Puppy"""
    print(frank.name)               # print Frankie
    print(frank.age)                # print 4

    
    """again and again running session add and commit, adds the data in table again and again"""
    db.session.add_all([sam,frank])             
    
    """Alternative for individual additions"""
    # db.session.add(sam)
    # db.session.add(frank)

    """Now save it to the database"""
    db.session.commit()                       
                                                               
    ###########################################################################################                                                           

    """now data is added in puppy table
       It is always better to print or access any data from db that is already available in db instead of using it from local memory"""
    
    ###########################################################################################
    
    """accesses the auto created instance attribute that is available in local memory bcoz data added and commited to db
    and do not access it from table Puppy"""
    print(sam.id)                   # print 1
    """accesses the instance attribute that is available in local memory becaues of __init__
    and do not access it from table Puppy"""
    print(sam.name)                 # print Sammy
    print(sam.age)                  # print 3


    """accesses the auto created instance attribute that is available in local memory bcoz data added and commited to db
    and do not access it from table Puppy"""
    print(frank.id)                 # print 2
    """accesses the instance attribute that is available in local memory becaues of __init__
    and do not access it from table Puppy"""
    print(frank.name)               # print Frankie
    print(frank.age)                # print 4
    

