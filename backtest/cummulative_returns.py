from datetime import datetime
from manager import quotes_manager
import pandas as pd
import matplotlib.pyplot as plt
import os

def compare_returns(symbols, start_date: datetime, end_date: datetime):
    df_main = pd.DataFrame(index=pd.date_range(start_date,end_date))
    for symbol in symbols:
        df_temp = quotes_manager.get_daily_quotes(start_date,end_date,symbol)
        df_main = df_main.join(df_temp[quotes_manager.COL_ADJ_CLOSE]).rename(columns={quotes_manager.COL_ADJ_CLOSE:symbol})

    df_main = df_main.dropna()
    df_main = df_main.pct_change().fillna(0).cumsum()
    df_main.plot()
    plt.show()

start_date = datetime(2015, 7, 1)
end_date = datetime(2018, 8, 15)

print(compare_returns(['SPX','AAPL','MSFT'],start_date,end_date))