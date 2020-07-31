from bookapp.authors.model.author import Author
from marshmallow_sqlalchemy import ModelSchema

class AuthorSchema(ModelSchema):

    class Meta:
        model = Author
