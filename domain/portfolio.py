from datetime import datetime
from typing import List

import pandas as pd

from domain.order import order


class portfolio:
    name: str
    orders: List[order]

    def __init__(self, name):
        self.name = name
        self.orders = {}

    def add_order(self, order):
        orders_list = self.orders.setdefault(order.date, [])
        orders_list.append(order)
        self.orders[order.date] = orders_list

    def calculate_positions_df(self, start_date: datetime, end_date: datetime):
        col_cash_daily_movement = 'Cash Daily Movement'
        col_cash_balance = 'Cash Balance'
        date_range = pd.date_range(start_date, end_date)
        ids = set()
        for orders in self.orders.values():
            for order in orders:
                ids.add(order.id)
        columns = ids
        columns.add(col_cash_daily_movement)
        columns.add(col_cash_balance)
        df = pd.DataFrame(index=date_range, columns=columns)
        df.fillna(value=0.0, inplace=True)
        for date in sorted(self.orders):
            total_cash_per_day = 0.0
            order_date_str = date.strftime('%Y-%m-%d')
            for order in self.orders[date]:
                df.loc[df.index >= order_date_str, order.id] = df.loc[order_date_str][
                                                                   order.id] + order.get_signed_quantity()
                total_cash_per_day += order.get_signed_cash()
            df.loc[order_date_str][col_cash_daily_movement] = total_cash_per_day
            df.loc[df.index >= order_date_str, col_cash_balance] = df.loc[order_date_str, col_cash_balance] + total_cash_per_day
        return df

