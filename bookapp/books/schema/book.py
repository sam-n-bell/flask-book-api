from bookapp.books.model.book import Book
from marshmallow_sqlalchemy import ModelSchema

class BookSchema(ModelSchema):
    class Meta:
        model = Book