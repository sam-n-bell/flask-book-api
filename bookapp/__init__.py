from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from bookapp.configurations import DevelopmentConfig
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()

def create_app(config=None):

    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig())

    db.__init__(app)
    ma.__init__(app)
    migrate.__init__(app, db) # putting this below blueprints didn't detect tables for some reason

    from bookapp.books.routes.book import books
    from bookapp.authors.routes.author import authors
    from bookapp.publishers.routes.publisher import publishers
    app.register_blueprint(books, url_prefix=None)
    app.register_blueprint(authors, url_prefix=None)
    app.register_blueprint(publishers, url_prefix=None)


    return app