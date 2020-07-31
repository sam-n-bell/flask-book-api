from bookapp.books.model.book import BookModel
from marshmallow_sqlalchemy import ModelSchema

class BookSchema(ModelSchema):
    class Meta:
        model = BookModel