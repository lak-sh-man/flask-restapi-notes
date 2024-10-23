from marshmallow import Schema, fields


class PlainItemSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)


class PlainStoreSchema(Schema):
    id = fields.Str(dump_only=True)
    """1) Fields that are not marked with 'dump_only' or 'load_only' will be included both when 
          serializing (output) and deserializing (input)
       2) The name field in your example doesn't have dump_only=True, so it's included by default in the response"""
    name = fields.Str(required=True)


class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class ItemSchema(PlainItemSchema):
    store_id = fields.Str(required=True, load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)

"""1) The schema (StoreSchema) is responsible for transforming these stores (which are Python objects) 
      into a dictionary-like format (JSON or a Python dict)
   2) The related items and tags are fetched by SQLAlchemy when Marshmallow accesses them as part of the schema
      This happens even though you only queried the StoreModel, because the relationships are dynamically loaded when needed"""

class StoreSchema(PlainStoreSchema):
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True) # If we hide this, items won't be returned


"""1) Serialization: Converting Python objects (like SQLAlchemy models) into a format that can be returned to the client, such as JSON
   2) Deserialization: When data comes from the client, Marshmallow validates and converts the data into the expected format"""



"""1) Those parameters with "required=True" can only be sent in an API request
      Any other more or less will throw an error
   2) Before using this schema, we might have put if condition like "name" should be mustly sent, but more that  
      unwanted data can also be sent
   3) This schema also helps to validate the values to check if they are in defined datatypes 
      that are sent in defined keys"""