
from datetime import datetime

from indicator.base_indicator import BaseIndicatorSingCol
from indicator.moving_avg import SimpleMovingAvg
from manager import quotes_manager
import pandas as pd
import matplotlib.pyplot as plt

# Resources: https://www.learndatasci.com/tutorials/python-finance-part-3-moving-average-trading-strategy/

class MovingStd(BaseIndicatorSingCol):
    def __init__(self,window:int):
        self.window = window

    def get_column_name(self):
        return "MovSTD_" + str(self.window)

    def calculate_ind(self, df: pd.DataFrame,symbol:str):
        return df[symbol].rolling(self.window).std()