import os

from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from resources.user import UserRegister, User, UserLogin
from resources.item import Item, ItemsList
from resources.menu import Menu, MenusList
from seeds.menu import menu
from models.menu import MenuModel
from seeds.item import item
from models.item import ItemModel
from models.orderItem import OrderItemModel
from resources.stripe import StripeCharge

app = Flask(__name__)
CORS(app)

app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
# TODO: .env/.ini file for passwords. app.config['JWT_SECRET_KEY']
app.secret_key = 'tyler'
api = Api(app)


# TODO: https://blog.tecladocode.com/learn-python-advanced-configuration-of-flask-jwt/
jwt = JWTManager(app)

api.add_resource(Menu, '/menu/<string:name>')
api.add_resource(MenusList, '/menus')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemsList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(StripeCharge, '/stripeCharge')
api.add_resource(User, '/user/<int:user_id>')
api.add_resource(UserLogin, '/login')

if __name__ == '__main__':
    from db import db
    db.init_app(app)

    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()

    app.run(port=5000, debug=True)
