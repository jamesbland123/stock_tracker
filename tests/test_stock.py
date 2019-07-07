from app.stock import get, get_ticker_symbol, add_ticker_symbol
import string
import random

def random_generator(size=4, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

def test_get():
    """
    Test response from stock.get
    """
    list_of_records = get()
    
    # ID for the first returned record should be 1
    assert list_of_records[0]['id'] == 1 

def test_get_ticker_symbol():
    """
    Test to get a specific record for AMZN
    """
    amzn_ticker = get_ticker_symbol('AMZN')
    assert amzn_ticker['id'] == 1
    
def test_add_ticker_symbol():
    """
    This test creates a random 4 character string and inserts
    it into the database.  
    """
    random_chars = random_generator()
    new_ticker_symbol = {"ticker_symbol" : random_chars}
    add_ticker_results = add_ticker_symbol(new_ticker_symbol)
    assert add_ticker_results[0]['ticker_symbol'] == random_chars