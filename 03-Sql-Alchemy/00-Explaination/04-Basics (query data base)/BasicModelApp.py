# Full docs: http://docs.sqlalchemy.org/en/latest/core/types.html
# class indicates table names 
# class attributes indicates column names 
# object indicates row wise contents 

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# This grabs our directory
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

# Connects our Flask App to our Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Puppy(db.Model):

    __tablename__ = 'puppies'  # If you don't provide this, the default table name will be the class name
    
    id = db.Column(db.Integer,primary_key=True) # Primary Key column, unique id for each puppy
    name = db.Column(db.Text)
    age = db.Column(db.Integer)

    print(id)      # prints (no name)
    print(name)    # prints (no name)
    print(age)     # prints (no name)
 
    def __init__(self,name,age):
        self.name = name
        self.age = age

    # __repr__ function is called when ever we try to print an object of a class (inside which the __repr__function is defined) or try to print a list of object etc.... 
    def __repr__(self):
        return f"Puppy {self.name} is {self.age} years old."
