from bookapp import db, ma

class BookModel(db.Model):
    __tablename__ = 'books'

    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    pages = db.Column(db.Integer, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.author_id'), nullable=False)
    year_published = db.Column(db.Integer, nullable=False)
    
    @classmethod 
    def find_by_author_id(cls, author_id: int) -> "BookModel":
        return cls.query.filter_by(author_id=author_id).all()

    @classmethod 
    def find_by_id(cls, id: int) -> "BookModel":
        return cls.query.filter_by(book_id=id).first()
    
    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()