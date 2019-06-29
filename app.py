# app.py

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Root(Resource):
    def get(self):
        return {'lost' : 'yes'} 

api.add_resource(Root, '/')

CARS = {
    'car1':'camry',
    'car2':'rav4',
    'car3':'4runner',
}

class Car(Resource):
    def get(self, car_id):
        return {car_id: CARS[car_id]}
        
    def put(self, car_id):
        CARS[car_id] = request.form['data']
        return {car_id: CARS[car_id]}
        
api.add_resource(Car, '/<string:car_id>')        

if __name__ == '__main__':
    app.run(host='0.0.0.0')