from flask import Blueprint, jsonify, request
from server.models.restaurant_pizza import RestaurantPizza
from server.models.pizza import Pizza
from server.models.restaurant import Restaurant
from server.models import db

restaurant_pizza_bp = Blueprint('restaurant_pizza_bp', __name__)

@restaurant_pizza_bp.route('/', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    try:
        price = int(data['price'])
        pizza_id = int(data['pizza_id'])
        restaurant_id = int(data['restaurant_id'])

        if price < 1 or price > 30:
            raise ValueError('Price must be between 1 and 30')

        rp = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
        db.session.add(rp)
        db.session.commit()

        pizza = Pizza.query.get(pizza_id)
        restaurant = Restaurant.query.get(restaurant_id)

        return jsonify({
            "id": rp.id,
            "price": rp.price,
            "pizza_id": rp.pizza_id,
            "restaurant_id": rp.restaurant_id,
            "pizza": pizza.to_dict(rules=('-restaurant_pizzas',)),
            "restaurant": restaurant.to_dict(rules=('-restaurant_pizzas',))
        }), 201

    except (KeyError, ValueError) as e:
        return jsonify({"errors": [str(e)]}), 400