from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import dotenv
import os

dotenv.load_dotenv()

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config["SECRET_KEY"] = os.environ.get("secret-key")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from api.admin.views import admin_bp
from api.users.views import users_bp
app.register_blueprint(admin_bp)
app.register_blueprint(users_bp)

