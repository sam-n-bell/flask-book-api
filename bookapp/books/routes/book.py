from flask import Blueprint, jsonify, request, Response
from bookapp.books.schemas.book import BookSchema
from bookapp.books.models.book import BookModel
from bookapp import db
from marshmallow.exceptions import ValidationError

books = Blueprint('books', __name__)
book_schema = BookSchema()

@books.route('/books', methods=['POST'])
def post_book():
    try:
        book = BookSchema().load(request.get_json(), session=db)
        print(book)
        book.save_to_db()
        return Response(None, 201)
    except ValidationError as e:
        return jsonify({'message': str(e)}), 400
