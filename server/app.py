from flask import Flask
from flask_migrate import Migrate
from server.models import db
from server.config  import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate = Migrate(app, db)

    from server.controllers.restaurant_controller import restaurant_bp
    from server.controllers.pizza_controller import pizza_bp
    from server.controllers.restaurant_pizza_controller import restaurant_pizza_bp

    app.register_blueprint(restaurant_bp, url_prefix='/restaurants')
    app.register_blueprint(pizza_bp, url_prefix='/pizzas')
    app.register_blueprint(restaurant_pizza_bp, url_prefix='/restaurant_pizzas')

    return app
