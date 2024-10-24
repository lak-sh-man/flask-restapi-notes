from marshmallow import Schema, fields


class ItemSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    store_id = fields.Str(required=True)


class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class StoreSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)


"""Those parameters with "required=True" can only be sent in an API request""" 
"""Any other more or less will throw an error"""
"""Before using this schema, we might have put if condition like "name" should be mustly sent, but more that  
   unwanted data can also be sent""" 
"""This schema also helps to validate the values to check if they are in defined datatypes 
   that are sent in defined keys"""