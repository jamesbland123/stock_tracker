from datetime import datetime
from config import db, ma

class Stock(db.Model):
    __tablename__ = 'stock'
    id = db.Column(db.Integer, primary_key=True)
    ticker_symbol = db.Column(db.String(32), index=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class StockSchema(ma.ModelSchema):
    class Meta:
        model = Stock
        sqla_session = db.session