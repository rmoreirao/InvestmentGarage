
from datetime import datetime
from manager import quotes_manager
import pandas as pd
import matplotlib.pyplot as plt


def bollinger_bands(symbol, start_date: datetime, end_date: datetime,window:int, n_std:int):
    df = quotes_manager.get_daily_quotes(start_date,end_date,symbol)
    df = df.rename(columns={quotes_manager.COL_ADJ_CLOSE:symbol})[[symbol]]
    df['Roll Mean'] = df[symbol].rolling(window).mean()
    roll_std = df[symbol].rolling(window).std()
    df['Boll Upper'] = df['Roll Mean'] + (n_std * roll_std)
    df['Boll Lower'] = df['Roll Mean'] - (n_std * roll_std)
    print(df)
    df.plot(figsize=(12,6))
    plt.show()

start_date = datetime(2015, 7, 1)
end_date = datetime(2018, 8, 15)

bollinger_bands('AAPL',start_date,end_date,20,2)