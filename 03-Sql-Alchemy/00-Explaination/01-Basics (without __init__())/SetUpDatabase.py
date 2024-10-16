from BasicModelApp import db, Puppy, app

# The objects are initiated with keyword arguments in it 
# where no __init__ is available, so 
sam = Puppy(name='Sammy', age=3)
frank = Puppy(name='Frankie', age=4)

"""For sam to come and access its instance attributes sam.name and sam.age, we defined __init__() method.
   But when sam tries to access its instance attribute sam.id, none will be printed because, id for each 
   object instantiation is a primary key. So it is only created after adding and commiting the instantiated objects to the db and
   stored as an instance attribute in local memory as long as the current file is running where adding and commiting is happening.
   
   As of now, no object is added and commited to the db, so when sam tries to access sam.id none will be printed"""
   
print(sam.id)                      # print None
print(sam.name)                    # print Sammy
print(sam.age)                     # print 3

print(frank.id)                    # print None
print(frank.name)                  # print Frankie
print(frank.age)                   # print 4

with app.app_context():
    
   sam = Puppy(name='Sammy', age=3)
   frank = Puppy(name='Frankie', age=4)

   print(sam.id)                   # print None
   print(sam.name)                 # print Sammy
   print(sam.age)                  # print 3

   print(frank.id)                 # print None
   print(frank.name)               # print Frankie
   print(frank.age)                # print 4

   ###########################################################################################            
   """again and again running session add and commit, adds the data in table again and again"""                                               
   db.session.add(sam)
   db.session.add(frank)
   
   """Alternate solution to add all at once"""
   # db.session.add_all([sam,frank]) 

   """Now save it to the database"""
   db.session.commit()                                                     
   ###########################################################################################                                                           

   """Now when sam tries to access its id, it will be printed because,
         1) now objects are added and commited in db and the self.id instance attribute for both sam and frank are available in
            local memory only during the run time of this file where adding and commiting is happening and also as we are 
            printing the sam.id and frank.id in this file itself so that within the runtime of this file itself they can also be printed
         2) now when we try to access the sam.id and frank.id in another file after importing the instantiated objects there,
            none will only be printed because by the time we run that file, the file where we add and commit would have been run,
            which means the sam.id and frank.id are no more accessible in another file and give only none
            
      1) As adding and commiting is done, now when we try to print sam.id or frank.id, 1 and 2 will be printed.
      2) when we re-run this page commenting the session add & commit, now when we try to print sam.id or frank.id, none will only 
         be printed and not their ids.
      3) now when we re-run this page with the session add & commit, now when we try to print sam.id or frank.id, 3 and 4 will be printed
      4) It is always better to retrieve data from db that is already available in db and try to access it instead of depending
         on local memory data"""
   
   print(sam.id)                   # print 1
   print(sam.name)                 # print Sammy
   print(sam.age)                  # print 3

   print(frank.id)                 # print 2
   print(frank.name)               # print Frankie
   print(frank.age)                # print 4