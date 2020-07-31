from flask import Blueprint, jsonify, request, Response
from bookapp.publishers.schema.publisher import PublisherSchema
from bookapp import db
from marshmallow.exceptions import ValidationError

publishers = Blueprint('publisher', __name__)
publisher_schema = PublisherSchema()

@publishers.route('/publishers', methods=['POST'])
def post_publisher():
    try:
        publisher = publisher_schema.load(request.get_json(), session=db)
        publisher.save_to_db()
        return Response(None, 201)
    except ValidationError as e:
        return jsonify({'message': str(e)}), 400
