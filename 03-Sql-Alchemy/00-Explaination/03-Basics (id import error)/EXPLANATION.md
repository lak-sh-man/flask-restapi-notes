## ⚠️ EXPLANATION-1
- When you run Items/Create.py, it imports store_1 and store_2 from Stores/Create.py
- If the print statements are removed, it's possible that the store objects (store_1 and store_2) are not being used after the commit(), so Python might garbage collect the objects before Items/Create.py is run
- As a result, when you import store_1 and store_2 in Items/Create.py, they might not hold the assigned id values because they no longer reference the same objects that were committed to the database 
- **This problem only happens with the primary key id**
- **DetachedInstanceError** occurs because SQLAlchemy is trying to load the ID of a store that is no longer associated with an active session

## ⚠️ EXPLANATION-2
- The print statements keep store_1 and store_2 alive long enough for their id values to be populated before they are imported and used in Items/Create.py

## ⚠️ EXPLANATION-3
- To avoid this unexpected error, we should always query the data base and re-use the values instead of using it from local memory that stays as long as the file is running
- By querying the database for the stores instead of relying on the same objects across modules, you eliminate the dependency on the print statement, and your application will run smoothly without errors