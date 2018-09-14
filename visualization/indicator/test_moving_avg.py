
from datetime import datetime

from indicator.base_indicator import BaseIndicatorSingCol
from indicator.moving_avg import SimpleMovingAvg, ExponentialMovingAvg
from manager import quotes_manager
import pandas as pd
import matplotlib.pyplot as plt

# Resources: https://www.learndatasci.com/tutorials/python-finance-part-3-moving-average-trading-strategy/

def test_exponential_moving__avg(symbol, start_date: datetime, end_date: datetime):
    df = quotes_manager.get_daily_quotes(start_date,end_date,symbol)
    df = df.rename(columns={quotes_manager.COL_ADJ_CLOSE:symbol})

    ema = ExponentialMovingAvg(20)
    ema.calculate_ind_into_df(df,symbol)

    sma = SimpleMovingAvg(20)
    sma.calculate_ind_into_df(df, symbol)

    ax = df[[symbol, ema.get_ind_column_name(), sma.get_ind_column_name()]].plot()
    plt.show()

start_date = datetime(2015, 7, 1)
end_date = datetime(2018, 8, 15)

test_exponential_moving__avg('GOOG',start_date,end_date)