from marshmallow import Schema, fields


class PlainItemSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)


class PlainStoreSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)


class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class ItemSchema(PlainItemSchema):
    store_id = fields.Str(required=True, load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)

"""The schema (StoreSchema) is responsible for transforming these stores (which are Python objects) 
   into a dictionary-like format (JSON or a Python dict)"""

class StoreSchema(PlainStoreSchema):
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True) # If we hide this, items won't be returned


"""Serialization: Converting Python objects (like SQLAlchemy models) into a format that can be returned to the client, such as JSON"""
"""Deserialization: When data comes from the client, Marshmallow validates and converts the data into the expected format"""
