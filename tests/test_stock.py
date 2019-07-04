from ..resources.stock import Stock

def test_get():
    s = Stock()
    assert s.get("AMZN") == {"AMZN": "abc12345"}