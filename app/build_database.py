import os
from config import db
from models import Stock

# Data to initialize database with

SYMBOLS = [
    {'ticker_symbol': 'AMZN'},
    {'ticker_symbol': 'FB'},
    {'ticker_symbol': 'NFLX'}

]

# Delete database file if it exists currently
if os.path.exists('stock_tracker.db'):
    os.remove('stock_tracker.db')

# Create the database
db.create_all()

# Iterate over the Stock structure and populate the database
for stock in SYMBOLS:

    s = Stock(ticker_symbol=stock['ticker_symbol'])
    db.session.add(s)

db.session.commit()
