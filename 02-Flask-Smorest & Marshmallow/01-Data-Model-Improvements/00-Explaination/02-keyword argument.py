def greet(**kwargs):       # passing bunch of keyword arguments, creates a dict
    for kwarg in kwargs:
       print (kwarg)

mydict = dict(a=1,b=2,c=3) # mydict = {"a"=1, "b":2, "c":3}
greet(**mydict)            # a dict is converted to bunch of keyword arguments, when **kwarg is inside a function call