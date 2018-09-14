from datetime import datetime

from indicator.returns import AbsoluteReturn, DailyReturn, CummulativeReturn
from manager import quotes_manager
import pandas as pd
import matplotlib.pyplot as plt

def test_returns_hist(symbols, start_date: datetime, end_date: datetime,ind_return,ax):
    df_main = pd.DataFrame(index=pd.date_range(start_date,end_date))
    for symbol in symbols:
        df_temp = quotes_manager.get_daily_quotes(start_date,end_date,symbol)
        df_main = df_main.join(df_temp[quotes_manager.COL_ADJ_CLOSE]).rename(columns={quotes_manager.COL_ADJ_CLOSE:symbol})

    df_main.dropna(inplace=True)

    for symbol in symbols:
        ind_return.calculate_ind_into_df(df_main,symbol)

    df_main[[ind_return.get_column_name(symbol) for symbol in symbols]].hist(ax=ax)


start_date = datetime(2015, 7, 1)
end_date = datetime(2018, 8, 15)

fig, axes = plt.subplots(nrows=1, ncols=3,figsize=(15,15))

test_returns_hist(['SPX'],start_date,end_date,AbsoluteReturn(),axes[0])
test_returns_hist(['SPX'],start_date,end_date,CummulativeReturn(),axes[1])
test_returns_hist(['SPX'],start_date,end_date,DailyReturn(),axes[2])

plt.show()