from marshmallow import Schema, fields


class PlainItemSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)


class PlainStoreSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)


class PlainTagSchema(Schema):
    id = fields.Str(dump_only=True)
    """1) Fields that are not marked with 'dump_only' or 'load_only' will be included both when 
          serializing (output) and deserializing (input)
       2) The name field in your example doesn't have dump_only=True, so it's included by default in the response
       3) 'name' is not given 'dump_only' but when we give 'required=True' it is automatically made dumpable"""
    name = fields.Str(required=True)


class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class ItemSchema(PlainItemSchema):
    store_id = fields.Str(required=True, load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)


class StoreSchema(PlainStoreSchema):
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)
    tags = fields.List(fields.Nested(PlainTagSchema()), dump_only=True)


class TagSchema(PlainTagSchema):
    store_id = fields.Str(load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)