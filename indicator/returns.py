from datetime import datetime

from indicator.base_indicator import BaseIndicatorSingCol
from manager import quotes_manager
import pandas as pd
import matplotlib.pyplot as plt
import os

class CummulativeReturn(BaseIndicatorSingCol):
    def get_ind_column_name(self):
        return "CUMRET"

    def calculate_ind(self, df: pd.DataFrame, symbol: str):
        return df[symbol].pct_change().fillna(0).cumsum()

# Daily Returns, starting from 1.0
class NormalizedDailyReturn(BaseIndicatorSingCol):
    def get_ind_column_name(self):
        return "ABSRET"

    def calculate_ind_series(self, quotes: pd.Series):
        return quotes / quotes.iloc[0]

    def calculate_ind(self, df: pd.DataFrame, symbol: str):
        return df[symbol] / df[symbol].iloc[0]

class DailyReturn(BaseIndicatorSingCol):
    def get_ind_column_name(self):
        return "DAYRET"

    def calculate_ind(self, df: pd.DataFrame, symbol: str):
        return df[symbol].pct_change()