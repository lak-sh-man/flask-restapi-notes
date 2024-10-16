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

## ⚠️ EXPLANATION-2
- If we don’t define an __init__() method, the class will use the default Python constructor, which only expects one argument **self**
- Because of this, in this case when we send this data, it says <br> 
**ERROR : Only one argument is expected, but 2 are sent**
  
```python
sam = Puppy('Sammy', 3)
frank = Puppy('Frankie', 4)
```
