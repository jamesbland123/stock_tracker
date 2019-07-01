# app.py

from flask import Flask, request
from flask_restful import Resource, Api
from resources.stock import Stock
from resources.stocks import Stocks


app = Flask(__name__)
api = Api(app)

class Root(Resource):
    def get(self):
        return {'lost' : 'yes'} 

api.add_resource(Root, '/')        
api.add_resource(Stock, '/stock/<ticker_id>') 
api.add_resource(Stocks, '/stocks') 

if __name__ == '__main__':
    app.run(host='0.0.0.0')