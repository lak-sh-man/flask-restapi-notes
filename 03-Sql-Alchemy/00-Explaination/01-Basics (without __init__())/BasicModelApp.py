import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# This grabs our directory
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

# Connects our Flask App to our Database
# this line creates the data.sqlite file
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

with app.app_context():
    # this line only creates an empty puppy table, with column title using class attributes in it
    # first db.create_all() should be done, then only object Instantiation should be done
    db.create_all()  