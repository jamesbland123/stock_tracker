from datetime import datetime

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# Data to serve with our API
SYMBOLS = {
    "AMZN": {
        "id": "1",
        "ticker_symbol": "AMZN",
        "timestamp": get_timestamp()
    },
    "FB": {
        "id": "2",
        "ticker_symbol": "FB",
        "timestamp": get_timestamp()
    },
    "NFLX": {
        "id": "3",
        "ticker_symbol": "NFLX",
        "timestamp": get_timestamp()
    }
}

# Create a handler for our read (GET) people
def get():
    """
    This function responds to a request for /api/vi/stocks
    with the complete lists of stocks

    :return:        sorted list of stocks
    """
    # Create the list of people from our data
    return [SYMBOLS[key] for key in sorted(SYMBOLS.keys())]