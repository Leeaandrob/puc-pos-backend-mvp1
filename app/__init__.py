from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

from app.config import Config

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*", "methods": ["GET", "POST", "PUT", "DELETE"]}})

app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import controllers, models
