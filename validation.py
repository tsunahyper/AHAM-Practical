from marshmallow import Schema, fields, ValidationError, validate

not_empty = validate.Length(min=1, error="Field may not be empty.")


# INSERT VALIDATIONS
class CreateFundValidation(Schema):
    fund_id = fields.Int()
    fund_name = fields.Str(required=True,validate=not_empty,allow_none=False)
    fund_manager = fields.Str(required=True,validate=not_empty,allow_none=False)
    description = fields.Str(required=True,validate=not_empty,allow_none=False)
    nav = fields.Int()
    performance = fields.Str(required=True,validate=not_empty,allow_none=False)

class InsertValidationBaseSchema(Schema):
    create_fund = fields.Nested(CreateFundValidation)



# UPDATE VALIDATIONS
class UpdateFundValidation(Schema):
    fund_name = fields.Str(required=True,validate=not_empty,allow_none=False)
    fund_manager = fields.Str(required=True,validate=not_empty,allow_none=False)
    description = fields.Str(required=True,validate=not_empty,allow_none=False)
    nav = fields.Int()
    performance = fields.Str(required=True,validate=not_empty,allow_none=False)

class UpdateValidationBaseSchema(Schema):
    update_fund = fields.Nested(UpdateFundValidation)