from marshmallow import Schema, fields


class CreateMediaSchema(Schema):
    ig_user_id = fields.Str(required=True)
    caption = fields.Str(required=True)
    image_url = fields.Url(required=True)


class ReadMediaSchema(Schema):
    ig_user_id = fields.Str(required=True)


class UpdateMediaSchema(Schema):
    media_id = fields.Str(required=True)
    caption = fields.Str(required=True)


class DeleteMediaSchema(Schema):
    media_id = fields.Str(required=True)