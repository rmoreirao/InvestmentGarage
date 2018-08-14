from datetime import datetime
from manager import quotes_manager
import pandas as pd
import matplotlib.pyplot as plt
import os

def compare_daily_returns(symbols, start_date: datetime, end_date: datetime):
    df_main = pd.DataFrame(index=pd.date_range(start_date,end_date))
    for symbol in symbols:
        df_temp = quotes_manager.get_daily_quotes(start_date,end_date,symbol)
        # df_temp = df_temp[[quotes_manager.COL_DATE,quotes_manager.COL_ADJ_CLOSE]].rename(columns={quotes_manager.COL_ADJ_CLOSE:symbol})
        df_main = df_main.join(df_temp[quotes_manager.COL_ADJ_CLOSE]).rename(columns={quotes_manager.COL_ADJ_CLOSE:symbol})
        # df_main = df_main.join(df_temp)

    df_main = df_main.dropna()
    df_dialy_returns = df_main.pct_change()
    df_dialy_returns.plot(figsize=(12,6))
    plt.show()

start_date = datetime(2018, 7, 1)
end_date = datetime(2018, 8, 15)

print(compare_daily_returns(['SPX','AAPL','MSFT'],start_date,end_date))