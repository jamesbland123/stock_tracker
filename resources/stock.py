from flask_restful import Resource

class Stock(Resource):
    def get(self, ticker_id):
        return {ticker_id: "abc12345"}
        
    def put(self, ticker_id):
        #STOCKS[ticker_id] = request.form['data']
        return {ticker_id: "abc12345"}