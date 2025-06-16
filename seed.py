from faker import Faker
from server.app import create_app
from server.models import db
from server.models.pizza import Pizza
from server.models.restaurant import Restaurant
from server.models.restaurant_pizza import RestaurantPizza
import random

app = create_app()
fake = Faker()

with app.app_context():
    print("Seeding database...")

    RestaurantPizza.query.delete()
    Pizza.query.delete()
    Restaurant.query.delete()

    pizzas = []
    for _ in range(10):
        pizza = Pizza(
            name=fake.word().title() + " Pizza",
            ingredients=', '.join(fake.words(nb=5))
        )
        db.session.add(pizza)
        pizzas.append(pizza)

    restaurants = []
    for _ in range(5):
        restaurant = Restaurant(
            name=fake.company(),
            address=fake.address()
        )
        db.session.add(restaurant)
        restaurants.append(restaurant)

    db.session.commit()

    for _ in range(20):
        rp = RestaurantPizza(
            price=random.randint(5, 25),
            pizza_id=random.choice(pizzas).id,
            restaurant_id=random.choice(restaurants).id
        )
        db.session.add(rp)

    db.session.commit()
    print("Done seeding!")
