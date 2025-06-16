# Pizza Restaurant API

A RESTful API for managing restaurants, pizzas, and the prices of specific pizzas at different restaurants.

---

## Setup Instructions

1. **Clone the repository**

   ```bash
   git clone <https://github.com/carly-cracker/Pizza-restaurant-API>
   cd pizza-restaurant-api
   ```

2. **Create a virtual environment with pipenv**

   ```bash
   pipenv install
   pipenv shell
   ```

3. **Install dependencies**

   ```bash
   pip install Flask flask-migrate flask-sqlalchemy sqlalchemy_serializer
   ```

4. **Run the application**

   ```bash
   flask run
   ```

---

## Database Migration & Seeding

1. **Initialize the database**

   ```bash
   flask db init
   ```

2. **Generate migration scripts**

   ```bash
   flask db migrate -m "Initial migration."
   ```

3. **Apply migrations**

   ```bash
   flask db upgrade
   ```

4. **Seed the database**

   Run the `seed.py` file:

   ```bash
   python seed.py
   ```

---

## Routes Summary

| Method | Endpoint                         | Description                                |
|--------|----------------------------------|--------------------------------------------|
| GET    | `/restaurants`                   | List all restaurants                        |
| GET    | `/restaurants/<id>`              | Get details of one restaurant with pizzas   |
| DELETE | `/restaurants/<id>`              | Delete a restaurant                         |
| GET    | `/pizzas`                        | List all pizzas                             |
| POST   | `/restaurant_pizzas`             | Create a restaurant-pizza price relationship|

---

## Thunder Client Usage

Use [Thunder Client](https://www.thunderclient.com/) (VS Code Extension) to test endpoints:

1. **GET Restaurants**
   - Method: `GET`
   - URL: `http://localhost:5555/restaurants`

2. **GET Restaurant by ID**
   - Method: `GET`
   - URL: `http://localhost:5555/restaurants/1`

3. **POST Restaurant Pizza**
   - Method: `POST`
   - URL: `http://localhost:5555/restaurant_pizzas`
   - Body (JSON):

     ```json
     {
       "price": 10,
       "pizza_id": 1,
       "restaurant_id": 2
     }
     ```

4. **DELETE Restaurant**
   - Method: `DELETE`
   - URL: `http://localhost:5555/restaurants/1`

---

## Notes

- Use a WSGI server (e.g. Gunicorn) for production.

---

