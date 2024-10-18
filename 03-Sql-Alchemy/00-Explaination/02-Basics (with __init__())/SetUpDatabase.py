from BasicModelApp import db, Puppy, app

sam = Puppy('Sammy',3)
frank = Puppy('Frankie',4)

print(sam.id)                      # print None
print(sam.name)                    # print Sammy
print(sam.age)                     # print 3

print(frank.id)                    # print None
print(frank.name)                  # print Frankie
print(frank.age)                   # print 4

with app.app_context():
    
   sam = Puppy('Sammy',3)
   frank = Puppy('Frankie',4)

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
   
   print(sam.id)                   # print 1
   print(sam.name)                 # print Sammy
   print(sam.age)                  # print 3

   print(frank.id)                 # print 2
   print(frank.name)               # print Frankie
   print(frank.age)                # print 4