from datetime import datetime

from indicator.returns import AbsoluteReturn, DailyReturn, CummulativeDailyReturn
from manager import quotes_manager
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def test_returns_scatter(x_symbol,y_symbol, start_date: datetime, end_date: datetime,ind_return,ax):
    symbols = [x_symbol,y_symbol]
    df_main = pd.DataFrame(index=pd.date_range(start_date,end_date))
    for symbol in symbols:
        df_temp = quotes_manager.get_daily_quotes(start_date,end_date,symbol)
        df_main = df_main.join(df_temp[quotes_manager.COL_ADJ_CLOSE]).rename(columns={quotes_manager.COL_ADJ_CLOSE:symbol})

    df_main.dropna(inplace=True)

    for symbol in symbols:
        ind_return.calculate_ind_into_df(df_main,symbol)

    beta_Y,alpha_Y = np.polyfit(df_main[x_symbol],df_main[y_symbol],1)
    print('Beta '+y_symbol+' = ' + str(beta_Y))
    print('Alpha ' + y_symbol + ' = ' + str(alpha_Y))
    ax.plot(df_main[x_symbol],beta_Y*df_main[x_symbol]+alpha_Y,'-',color='r')
    df_main.plot(kind='scatter',x=x_symbol,y=y_symbol, ax=ax)

start_date = datetime(2015, 7, 1)
end_date = datetime(2018, 8, 15)

fig, axes = plt.subplots(nrows=2, ncols=2,figsize=(15,15))

test_returns_scatter('SPX','AAPL',start_date,end_date,DailyReturn(),axes[0,0])
test_returns_scatter('SPX','MSFT',start_date,end_date,DailyReturn(),axes[0,1])
test_returns_scatter('AAPL','MSFT',start_date,end_date,DailyReturn(),axes[1,0])
test_returns_scatter('MSFT','AAPL',start_date,end_date,DailyReturn(),axes[1,1])

plt.show()