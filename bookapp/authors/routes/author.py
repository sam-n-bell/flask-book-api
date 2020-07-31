from flask import jsonify, request, Response, Blueprint
from marshmallow.exceptions import ValidationError
from bookapp.authors.schema.author import AuthorSchema
from bookapp import db

author_schema = AuthorSchema()
authors = Blueprint('authors', __name__)

@authors.route('/authors', methods=['POST'])
def post_author():
    try:
        author = author_schema.load(request.get_json(), session=db)
        author.save_to_db()
        return Response(None, 201)
    except ValidationError as e:
        return jsonify({'message': str(e)}), 400