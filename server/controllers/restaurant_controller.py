from flask import Blueprint, jsonify, request ,make_response
from server.models.restaurant import Restaurant
from server.models import db

restaurant_bp = Blueprint('restaurant_bp', __name__)

@restaurant_bp.route('/', methods=['GET'])
def get_restuarnts():
    restaurants= Restaurant.query.all()
    response = [restaurant.to_dict(rules=('-restaurant_pizzas',)) for restaurant in restaurants] 
    return make_response(jsonify(response), 200)

@restaurant_bp.route('/<int:id>', methods=['GET','DELETE'])
def restaurant_by_id(id):
    restaurant = Restaurant.query.filter(Restaurant.id==id).first()
    if restaurant is None:
        response_body = {
            'message':f'the restaurant{id} is not found in our database.' } 
        return make_response(jsonify(response_body), 404)
    
    if request.method =='GET':
        restaurant_dict=restaurant.to_dict()
        return make_response(jsonify(restaurant_dict), 200)
    
    elif request.method =='DELETE':
        db.session.delete(restaurant)
        db.session.commit()
        return make_response(jsonify({'message':f'the restaurant{id} is deleted'}), 204)
