import datetime
import os

from flask import jsonify, request
from flask_restful import Resource, Api
from flask_swagger_ui import get_swaggerui_blueprint

from app import app, db
from .models import Product

api = Api(app=app)

# Define a sample resource
class Healthcheck(Resource):
    def get(self):
        return "WORKING"

# Configure Swagger UI
SWAGGER_URL = '/swagger'
API_URL = 'http://127.0.0.1:5000/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Products API"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/swagger.json')
def swagger():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path + '/swagger.json', 'r') as f:
        return f.read()

class Products(Resource):
    def get(self):
        products = Product.query.all()
        return jsonify(
            {"data": [{"name": p.name, "description": p.description, "id": p.id} for p in products]})

    def post(self):
        json_data = request.get_json(force=True)
        p = Product(
            name=json_data['name'],
            description=json_data['description'],
            created=datetime.datetime.today(),
        )
        db.session.add(p)
        db.session.commit()
        return jsonify(name=p.name)

    def delete(self, id):
        Product.query.filter_by(id=int(id)).delete()
        db.session.commit()
        return jsonify({"status": "success"})

# Add the resource to the API
api.add_resource(Healthcheck, '/')
api.add_resource(Products, '/api/products')
