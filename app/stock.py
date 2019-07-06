from flask import make_response, abort
from .config import db
from .models import Stock, StockSchema

# Create a handler for our read (GET) people
def get():
    """
    This function responds to a request for /api/v1/stock
    with the complete lists of stocks

    :return:        sorted list of stocks
    """
    # Create the list of people from our data
    stock = Stock.query.order_by(Stock.id).all()
    
    stock_schema = StockSchema(many=True)
    return stock_schema.dump(stock).data
    
    
def get_ticker_symbol(ticker_symbol):
    """
    Returns a single single stock ticker symbol for /api/v1/stock/{ticker}
    
    :return:        single ticker symbol
    """
    stock = Stock.query.filter(Stock.ticker_symbol == ticker_symbol).one_or_none()
    
    if stock is not None:
        stock_schema = StockSchema()
        return stock_schema.dump(stock).data
    
    else:
        abort(404, 'Stock does not exist: {ticker_symbol}'.format(ticker_symbol=ticker_symbol))
    
def add_ticker_symbol(ticker_symbol):
    """
    Function to add a ticker symbol to the database
    
    :param ticker_symbol:   ticker symbol to add_ticker_symbol
    :return:                201 on success, 406 on ticker symbol already exists
    """
    symbol = ticker_symbol.get("ticker_symbol")
    existing_symbol = Stock.query.filter(Stock.ticker_symbol == symbol).one_or_none()
    
    if existing_symbol is None:
        schema = StockSchema()
        new_ticker_symbol = schema.load(ticker_symbol, session=db.session).data
        
        db.session.add(new_ticker_symbol)
        db.session.commit()
        
        data = schema.dump(new_ticker_symbol).data
        
        return data, 201
        
    else:
        abort(409, "{ticker_symbol} exists already".format(ticker_symbol=ticker_symbol))
