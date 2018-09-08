from datetime import datetime

from domain.order_type import order_type
from domain.order import order
from domain.portfolio import portfolio

def test_portfolio():
    p = portfolio('Rodrigo')
    p.add_order(order(order_type.BUY, 'AAPL', 1000, 102, datetime(2018, 1, 10)))
    p.add_order(order(order_type.BUY, 'AAPL', 210, 103, datetime(2018, 1, 10)))
    p.add_order(order(order_type.SELL, 'AAPL', 300, 102, datetime(2018, 1, 11)))
    print(p.calculate_positions_df(datetime(2018, 1, 1), datetime(2018, 1, 15)))


test_portfolio()