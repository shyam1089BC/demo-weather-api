from copy import deepcopy

import marshmallow
from marshmallow import Schema, fields

class createBookRecord(Schema):
    lat = fields.Float(required=True)
    lon = fields.Float(required=True)
    cnt = fields.Integer()
    units = fields.String()


def validate_input_json(data):
    try:
        createBookRecord().load(data)
        return False, data
    except marshmallow.exceptions.ValidationError as e:
        error = deepcopy(e.messages)
        error = {key: " ,".join(value) for (key, value) in error.items() if isinstance(value, list)}
        return True, error
