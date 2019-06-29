# app.py

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Root(Resource):
    def get(self):
        return {'lost' : 'yes'} 


# Testing only, should not have
# this in containers as they should be 
# immutable
CARS = {
    '1':'camry',
    '2':'rav4',
    '3':'4runner',
}

class Car(Resource):
    def get(self, car_id):
        return {car_id: CARS[car_id]}
        
    def put(self, car_id):
        CARS[car_id] = request.form['data']
        return {car_id: CARS[car_id]}

class Cars(Resource):
    def get(self):
        return CARS

api.add_resource(Root, '/')        
api.add_resource(Car, '/car/<car_id>') 
api.add_resource(Cars, '/cars') 

if __name__ == '__main__':
    app.run(host='0.0.0.0')