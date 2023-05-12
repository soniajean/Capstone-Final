from flask import Flask

from config import Config
from .auth.routes import auth
from .payments.routes import payments
from .cart.routes import cart
from .api.routes import api

from .models import db, User, Product
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

login = LoginManager()
@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

login.init_app(app)
login.login_view='auth.loginPage'

app.register_blueprint(auth)
app.register_blueprint(payments)
app.register_blueprint(cart)
app.register_blueprint(api)

from . import routes
