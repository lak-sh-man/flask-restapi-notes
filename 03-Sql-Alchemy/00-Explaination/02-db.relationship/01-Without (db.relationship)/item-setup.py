from db import StoreModel, ItemModel, app, db

with app.app_context():
    
    # Create a store first
    store_1 = StoreModel(name="SS")
    db.session.add(store_1)
    db.session.commit()
    
    store_2 = StoreModel(name="Cheap & Best")
    db.session.add(store_2)
    db.session.commit()
    
    #########################################################################
    
    item_1 = ItemModel('Biriyani',230,store_1.id)
    db.session.add(item_1)
    db.session.commit()
    
    item_2 = ItemModel('Chicken Manchurian',140,store_2.id)
    db.session.add(item_2)
    db.session.commit()
    
    item_3 = ItemModel('Biriyani',100,store_2.id)
    db.session.add(item_3)
    db.session.commit()
    
    
    # item_1 = ItemModel.query.get(2)  # Get an item with ID 1


    # # Without relationship, you need to manually query the store
    # store = StoreModel.query.get(item_1.store_id)  # Find the store using the store_id
    # print(f"Item: {item_1.name}, Store: {store.name}")  # Manually accessing the store