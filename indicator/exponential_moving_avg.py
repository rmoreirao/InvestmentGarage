
from datetime import datetime

from indicator.base_indicator import base_indicator
from indicator.simple_moving_avg import simple_moving__avg
from manager import quotes_manager
import pandas as pd
import matplotlib.pyplot as plt

# Resources: https://www.learndatasci.com/tutorials/python-finance-part-3-moving-average-trading-strategy/

class exponential_moving__avg(base_indicator):
    def __init__(self,n_periods:int):
        self.n_periods = n_periods

    def get_column_name(self):
        return "EMA_" + str(self.n_periods)

    def calculate_ind(self, df: pd.DataFrame,symbol:str):
        return df[symbol].ewm(span=20, adjust=False).mean()