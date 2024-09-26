mydict = dict(a=1,b=2,c=3)   # mydict = {"a"=1, "b":2, "c":3}
stores = {**mydict, "id":1}  # a dict is converted to bunch of key value pairs, when **kwarg is inside a dictionary     
print(stores)              