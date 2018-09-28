from datetime import datetime

from indicator.base_indicator import BaseIndicatorSingCol
from manager import quotes_manager
import pandas as pd
import matplotlib.pyplot as plt
import os

class DailyReturn(BaseIndicatorSingCol):
    def get_ind_column_name(self):
        return "DAYRET"

    def calculate_ind(self, df: pd.DataFrame, symbol: str):
        # see https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.pct_change.html for example
        # (t/t-1) - 1
        day_ret = df[symbol].pct_change()
        day_ret[0] = 0
        return day_ret

class CummulativeDailyReturn(BaseIndicatorSingCol):
    def get_ind_column_name(self):
        return "CUMRET"

    # sum of daily returns
    def calculate_ind(self, df: pd.DataFrame, symbol: str):
        day_ret = DailyReturn()
        return day_ret.calculate_ind(df,symbol).fillna(0).cumsum()

class AbsoluteReturn(BaseIndicatorSingCol):
    def get_ind_column_name(self):
        return "ABSRET"

    # Tcurrent / T0
    # First Row = First Row / First Row = Always 1.0000
    # Second Row = Second Row / First Row
    # Third Row = Third Row / First Row
    def calculate_ind(self, df: pd.DataFrame, symbol: str):
        return df[symbol] / df[symbol].iloc[0]