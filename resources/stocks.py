from flask_restful import Resource

class Stocks(Resource):
    def get(self):
        return {"1":"AMNZ", "2": "APPL", "3": "FB"}