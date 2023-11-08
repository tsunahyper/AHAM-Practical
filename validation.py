from dataclasses import Field
from json import dumps, loads
from flask import Flask, jsonify, request
from marshmallow import Schema, fields, ValidationError, validate

not_empty = validate.Length(min=1, error="Field may not be empty.")


# INSERT VALIDATIONS
class CreateFundValidation(Schema):
    fund_id = fields.Str(required=True,validate=not_empty,allow_none=False)
    fund_name = fields.Str(required=True,validate=not_empty,allow_none=False)
    fund_manager = fields.Str(required=True,validate=not_empty,allow_none=False)
    description = fields.Str(required=True,validate=not_empty,allow_none=False)
    nav = fields.Str(required=True,validate=not_empty,allow_none=False)
    performance = fields.Str(required=True,validate=not_empty,allow_none=False)

class InsertValidationBaseSchema(Schema):
    create_fund = fields.Nested(CreateFundValidation)



# UPDATE VALIDATIONS
class UpdateFundValidation(Schema):
    fund_id = fields.Str(required=True,validate=not_empty,allow_none=False)
    fund_name = fields.Str(required=True,validate=not_empty,allow_none=False)
    fund_manager = fields.Str(required=True,validate=not_empty,allow_none=False)
    description = fields.Str(required=True,validate=not_empty,allow_none=False)
    nav = fields.Str(required=True,validate=not_empty,allow_none=False)
    performance = fields.Str(required=True,validate=not_empty,allow_none=False)

class UpdateValidationBaseSchema(Schema):
    update_fund = fields.Nested(UpdateFundValidation)