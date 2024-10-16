## ⚠️ ANATOMY
- **Class** indicates table names
- **Class attributes** indicates column names 
- **Object** instantiation indicates row wise contents 

## ⚠️ EXPLANATION-1
- The objects are initiated with keyword arguments, so __init__() is not needed 
- SQLAlchemy internally assigns the keyword arguments to the respective attributes **self.name**, **self.age** behind the scenes, which is why it works without needing an explicit __init__() method
- As because the keyword arguments are read in behind the scenes, we can also print the instance attributes 
  without the need of __init__()

```python
sam = Puppy(name='Sammy', age=3)
frank = Puppy(name='Frankie', age=4)
```

## ⚠️ EXPLANATION-1
- The objects are initiated with keyword arguments, so __init__() is not needed 
- SQLAlchemy internally assigns the keyword arguments to the respective attributes **self.name**, **self.age** behind the scenes, which is why it works without needing an explicit __init__() method
- As because the keyword arguments are read in behind the scenes, we can also print the instance attributes 
  without the need of __init__()
  
```python
sam = Puppy(name='Sammy', age=3)
frank = Puppy(name='Frankie', age=4)
```

## 🔴 NOTE
- It is the way we script our APIs is important and not actually the GET method itself that is mentioned in the API 
- The script inside the API is crucial, but it's also important to mention GET in the API for code readability and for testers to understand the requirement and test the APIs accordingly
- We can also send data in body using GET method, but it is not common to use body in GET method to send data