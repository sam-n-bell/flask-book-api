from bookapp import db

class Author(db.Model):
    __tablename__ = 'authors'

    author_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    books = db.relationship('Book', backref='author', lazy=True)

    @classmethod
    def find_by_id(cls, author_id: int) -> 'Author':
        return cls.query.filter_by(author_id=author_id).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()