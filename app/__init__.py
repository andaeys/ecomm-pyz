from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_URI
db = SQLAlchemy(app)
login_manager = LoginManager(app)
print("db print: ", db)


from app.models import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from app.routes import routes
app.register_blueprint(routes)
