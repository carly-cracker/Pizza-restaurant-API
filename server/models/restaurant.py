from server.models import db
from sqlalchemy_serializer import SerializerMixin

class Restaurant(db.Models, SerializerMixin):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String)
    address= db.Column(db.String)

    