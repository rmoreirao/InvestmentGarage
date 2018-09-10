import pandas as pd

from indicator.base_indicator import BaseIndicatorSingCol


# Resources: https://www.learndatasci.com/tutorials/python-finance-part-3-moving-average-trading-strategy/

class SimpleMovingAvg(BaseIndicatorSingCol):
    def __init__(self,n_periods:int):
        self.n_periods = n_periods

    def get_column_name(self):
        return "SMA_" + str(self.n_periods)

    def calculate_ind(self, df: pd.DataFrame,symbol:str):
        return df[symbol].rolling(window=20).mean()


class ExponentialMovingAvg(BaseIndicatorSingCol):
    def __init__(self,n_periods:int):
        self.n_periods = n_periods

    def get_column_name(self):
        return "EMA_" + str(self.n_periods)

    def calculate_ind(self, df: pd.DataFrame,symbol:str):
        return df[symbol].ewm(span=20, adjust=False).mean()