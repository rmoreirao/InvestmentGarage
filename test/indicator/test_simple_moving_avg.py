
from datetime import datetime

from indicator.base_indicator import base_indicator
from indicator.simple_moving_avg import simple_moving__avg
from manager import quotes_manager
import pandas as pd
import matplotlib.pyplot as plt

# Resources: https://www.learndatasci.com/tutorials/python-finance-part-3-moving-average-trading-strategy/

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