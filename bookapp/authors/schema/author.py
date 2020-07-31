from bookapp.authors.model.author import AuthorModel
from marshmallow_sqlalchemy import ModelSchema

class AuthorSchema(ModelSchema):

    class Meta:
        model = AuthorModel
