
from datetime import datetime

from indicators.base_indicator import base_indicator
from manager import quotes_manager
import pandas as pd
import matplotlib.pyplot as plt

# Resources: https://www.learndatasci.com/tutorials/python-finance-part-3-moving-average-trading-strategy/

class simple_moving__avg(base_indicator):
    def __init__(self,n_periods:int):
        self.n_periods = n_periods

    def get_column_name(self):
        return "SMA_" + str(self.n_periods)

    def calculate_ind(self, df: pd.DataFrame,symbol:str):
        return df[symbol].rolling(window=20).mean()

def test_simple_moving__avg(symbol, start_date: datetime, end_date: datetime):
    df = quotes_manager.get_daily_quotes(start_date,end_date,symbol)
    df = df.rename(columns={quotes_manager.COL_ADJ_CLOSE:symbol})
    rm = simple_moving__avg(20)
    rm.calculate_ind_into_df(df,symbol)
    ax = df[[symbol, rm.get_column_name()]].plot()
    plt.show()

start_date = datetime(2015, 7, 1)
end_date = datetime(2018, 8, 15)

test_simple_moving__avg('GOOG',start_date,end_date)