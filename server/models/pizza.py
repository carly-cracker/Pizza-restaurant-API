from sqlalchemy_serializer import SerializerMixin
from server.models import db

class Pizza(db.Model, SerializerMixin):
    __tablename__='pizzas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ingredients = db.Column(db.String)

    restaurant_pizzas= db.relationship('RestaurantPizza', backref='pizza', cascade='all, delete-orphan')
    serialize_rules=('-restaurant_pizzas',)