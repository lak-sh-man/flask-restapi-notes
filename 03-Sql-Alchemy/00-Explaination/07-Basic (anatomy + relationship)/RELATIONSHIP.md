## ⚠️ RELATIONSHIP
- In SQLAlchemy, it is a combination of both the **ForeignKey()** and the **relationship()** that determines the type of relationship

    - ### 1. FOREIGNKEY()
        - The ForeignKey in the child table defines the basic link between two tables
        - It indicates that the value in one column of the child table refers to a row in the parent table
        - However, on its own, a ForeignKey doesn't specify the type of relationship 
        - It just establishes a reference between two tables

    - ### 1. RELATIONSHIP()
        - The relationship() function defines the direction and nature of the relationship
        - It uses the ForeignKey to understand how the tables are related, but the parameters in relationship() <br>
        such as back_populates, uselist etc, influence the type of relationship

## ⚠️ PARENT & CHILD TABLE
- There can be infinite tables, where each table can be both a parent table and a child table or can be either one of them
- Now taking only a pair of table, Among/wrt them both cannot be a parent table & both cannot be a child table
- Among/wrt them, only one table can be a parent and another can be a child
- Among/wrt them, the one with **ForeignKey()** holding the other table name is the child and the other without is the parent

## ⚠️ ONE-TO-ONE 
- ForeignKey still defines the link, but you need to add **uselist=False** in the relationship() on the **parent side** to indicate that only one child record can be related
- without **uselist=False**, this would be a **MANY-TO-MANY** relationship and **uselist=False** can be only given to the parent table and not on the childs table
- From **StoreModel** perspective it is **ONE-->ONE SIDE** relationship 
- From **ItemModel** perspective it is **ONE-->ONE SIDE** relationship

```python
class StoreModel(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False) 
    items = db.relationship("ItemModel", uselist=False, back_populates="store") 

class ItemModel(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), nullable=False)
    store = db.relationship("StoreModel", back_populates="items")
```

:::tip ONE-TO-ONE
One Store has one item, One item has one store
:::

| id       | name                  | 
| -------- | --------------------- | 
| 1        | SS                    | 
| 2        | Cheap And Beast       | 
| 3        | Anandham              | 

| id       | name                  | price    | store_id              | 
| -------- | --------------------- | -------- | --------------------- | 
| 1        | Biriyni               | 240      | 1                     | 
| 2        | Chicken Manchurian    | 140      | 2                     | 
| 3        | Parotta               | 15       | 3                     | 


## ⚠️ ONE-TO-MANY 
- ForeignKey in the child table (many side)
- relationship() in the parent table (one side), often with uselist=True (the default)
- This is the default case where a single row in the parent table can relate to multiple rows in the child table
- From **StoreModel** perspective it is **ONE-->MANY SIDE** relationship 
- From **ItemModel** perspective it is **MANY-->ONE SIDE** relationship

```python
class StoreModel(db.Model):
    __tablename__ = "stores"
    id = db.Column(db.Integer, primary_key=True)
    items = db.relationship("ItemModel", back_populates="store") 

class ItemModel(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True)
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"))  # ForeignKey
    store = db.relationship("StoreModel", back_populates="items")
```



## ⚠️ MANY-TO-MANY 
- This requires a third table (association table) that links two tables with ForeignKeys from both
- The relationship() defines the connection with secondary pointing to the association table
- From **StoreModel** perspective it is **MANY-->MANY SIDE** relationship 
- From **ItemModel** perspective it is **MANY-->MANY SIDE** relationship

```python
# Association table
ThirdTable = db.Table(
                        'third_table',
                        db.Column('stores_id', db.Integer, db.ForeignKey('stores.id')), # ForeignKey
                        db.Column('items_id', db.Integer, db.ForeignKey('items.id'))    # ForeignKey
                     )

class StoreModel(db.Model):
    __tablename__ = "stores"
    id = db.Column(db.Integer, primary_key=True)
    items = db.relationship("ItemModel", secondary=ThirdTable, back_populates="store") 

class ItemModel(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True)
    store = db.relationship("StoreModel", secondary=ThirdTable, back_populates="items")
```

## 🔴 NOTE
- ForeignKey() is required to link tables, but relationship() defines the nature of how tables interact with each other
![SQL-RELATIONSHIP Image](./SQL-RELATIONSHIP.jpg)

