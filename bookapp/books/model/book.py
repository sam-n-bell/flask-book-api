from bookapp import db, ma

class BookModel(db.Model):
    __tablename__ = 'books'

    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    pages = db.Column(db.Integer, nullable=False)
    author = db.Column(db.String(), nullable=False)
    publisher = db.Column(db.String(), nullable=False)
    year_published = db.Column(db.Integer, nullable=False)
    
    @classmethod 
    def find_by_author(cls, author: str) -> "BookModel":
        return cls.query.filter_by(author=author).all()

    @classmethod 
    def find_by_id(cls, id: int) -> "BookModel":
        return cls.query.filter_by(book_id=id).first()
    
    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()