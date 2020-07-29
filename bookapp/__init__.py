from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from bookapp.configurations import DevelopmentConfig
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

def create_app(config=None):

    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig())

    from bookapp.books.routes.book import books
    app.register_blueprint(books, url_prefix=None)

    # from bookapp.books.resources.book import BooksApi
    # app.add_resource(BooksApi, '/books')

    db.__init__(app)
    ma.__init__(app)
    return app