## ⚠️ EXPLANATION-1
- When we declare **id = db.Column(db.Integer, primary_key=True)**, we're telling SQLAlchemy that this is the primary key for the table
- If we don't manually assign a value to id while instantiating the object, SQLAlchemy and the database will auto-generate it (often via auto-increment)

## ⚠️ EXPLANATION-2
- The objects are initiated with keyword arguments, so __init__() is not necessarily needed 
- SQLAlchemy internally assigns the keyword arguments to the respective attributes **self.name**, **self.age** behind the scenes while reading the initiated objects, which is why it works without needing an explicit __init__() method
- As because the keyword arguments are read in behind the scenes, we can also print the instance attributes 
  without the need of __init__()

```python
sam = Puppy(name='Sammy', age=3)
frank = Puppy(name='Frankie', age=4)
```

## ⚠️ EXPLANATION-3
- If we don’t define an __init__() method when having only positional arguments, the class will use the default Python constructor, which only expects one argument **self**
- So if the objects are initiated with only positional arguments, then __init__() is necessarily needed 
- Because of this, in this case when we send this data, it says **ERROR : Only one argument is expected, but 2 are sent**
  
```python
sam = Puppy('Sammy', 3)
frank = Puppy('Frankie', 4)
```

## ⚠️ EXPLANATION-4
- For sam to come and access its instance attributes sam.name and sam.age, these data are previously read, so they can be printed
- But when sam tries to access its instance attribute sam.id, none will be printed because, id for each 
initiated object is a primary key and can only be created after adding and commiting the data and they are auto incremental 
- Which means after adding and commiting the data only, SQLAlchemy internally assigns the keyword arguments to the respective attributes **self.id** behind the scenes
- Where this **self.id** is stored in local memory and stays as long as the file is running 
  
```python
print(sam.id)                      # print None
print(sam.name)                    # print Sammy
print(sam.age)                     # print 3

print(frank.id)                    # print None
print(frank.name)                  # print Frankie
print(frank.age)                   # print 4
```

