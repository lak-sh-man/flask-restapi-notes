from db import StoreModel, ItemModel, app, db

with app.app_context():
    db.create_all()
    
    # Create a store first
    my_store = StoreModel(name="SS")
    db.session.add(my_store)
    db.session.commit()
    
    my_item = ItemModel('biriyani',230,my_store.id)
    db.session.add(my_item)
    db.session.commit()
    
    
    item_1 = ItemModel.query.get(2)  # Get an item with ID 1


    # Without relationship, you need to manually query the store
    store = StoreModel.query.get(item_1.store_id)  # Find the store using the store_id
    print(f"Item: {item_1.name}, Store: {store.name}")  # Manually accessing the store