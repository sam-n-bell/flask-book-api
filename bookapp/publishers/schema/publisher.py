from bookapp.publishers.model.publisher import PublisherModel
from marshmallow_sqlalchemy import ModelSchema

class PublisherSchema(ModelSchema):
    class Meta:
        model = PublisherModel