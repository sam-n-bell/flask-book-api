from bookapp import db

class PublisherModel(db.Model):
    __tablename__ = 'publishers'

    publisher_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    books = db.relationship('BookModel', backref='publisher', lazy=True)

    @classmethod 
    def find_by_id(cls, id: int) -> "PublisherModel":
        return cls.query.filter_by(publisher_id=id).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()