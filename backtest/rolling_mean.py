
from datetime import datetime
from manager import quotes_manager
import pandas as pd
import matplotlib.pyplot as plt


def rolling_mean(symbol, start_date: datetime, end_date: datetime):
    df = quotes_manager.get_daily_quotes(start_date,end_date,symbol)
    df = df.rename(columns={quotes_manager.COL_ADJ_CLOSE:symbol})
    df['Rolling Mean 20'] = df[symbol].rolling(20).mean()
    ax = df[[symbol, 'Rolling Mean 20']].plot()
    plt.show()

start_date = datetime(2015, 7, 1)
end_date = datetime(2018, 8, 15)

rolling_mean('GOOG',start_date,end_date)