
from marshmallow import Schema, fields, validates, ValidationError

class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    username = fields.String(required= True)
    role = fields.String(required=True)
    age = fields.Integer(required=True)
    
    @validates("username")
    def validate_username(self, value):
        if len(value) < 3 or len(value) > 20:
            raise ValidationError("Username must be between 3 and 20 characters long.")
        
    