from ..resources.stocks import Stocks

def test_stocks():
    s = Stocks()
    assert s.get() == {'1': 'AMNZ', '2': 'APPL', '3': 'FB'}
    