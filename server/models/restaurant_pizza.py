from server.models import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

class RestaurantPizza(db.Model, SerializerMixin):
    __tablename__ = 'restaurant_pizzas'

    id = db.Column(db.Integer, primary_key = True)
    price = db.Column(db.Integer)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'))

    @validates('price')
    def validate_price(self, key, price):
        if not( 1<=price<=30):
            raise ValueError("Price must be between 1 and 30")
        return price
    
    serialize_rules=('-pizza.restaurant_pizzas', '-restaurant.pizza_restaurant_pizzas')