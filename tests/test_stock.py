from ..app.stock import get, get_ticker_symbol, add_ticker_symbol

def test_get():
    """
    Test response from stock.get
    """
    list_of_records = get()
    
    # ID for the first returned record should be 1
    assert list_of_records[0]['id'] == 1 
    