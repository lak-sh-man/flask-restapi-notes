from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        "name": "My Store",
        "items": [
            {
                "name": "Chair",
                "price": 15.99
            }
        ]
    }
]

@app.get("/store")
def get_stores():
    return {"stores": stores}


@app.post("/store")
def create_store():
    """ This API block expects a dictionary and a key of "name" inside of it exactly.
        If there are no data sent in request body or no key under "name" is available in the dictionary, then unintentional error occurs. 
        To avoid this, validations has to be done with the incomming data to check whether the required data are present or not. 
        If not present then we have to return an error response with the status code to make it professional. 
        Lets say if the data is not even sent in request body then an error response of msg "No data sent" along with a status code should be returned. 
        If data is sent but the data is not in the expecting way that the API block expects, then an error response of msg "Unexpected data sent" along with a status code should be returned.
        For any incomming data VALIDATION is must to be done in API 
        For any API, customized ERROR RESPONSE is a must to be done to avoid unintentional error occurences (example: POST)
    """
    request_data = request.get_json()
    # print(request_data)
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    # return new_store, 201
    return stores, 201


@app.get("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return store
    return {"message": "Store not found"}, 404


@app.get("/store/<string:name>/item")
def get_item_in_store(name):
    for store in stores:
        if store["name"] == name:
            return {"items": store["items"]}
    return {"message": "Store not found"}, 404


@app.post("/store/<string:name>/item")
def create_item(name):
    request_data = request.get_json()
    # print(request_data)
    for store in stores:
        if store["name"] == name:
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)
            # return new_item, 201
            return stores, 201
    return {"message": "Store not found"}, 404


if __name__ == '__main__':
    # app.run(debug=True, host='0.0.0.0', port=8000) 
    app.run(debug=True) 