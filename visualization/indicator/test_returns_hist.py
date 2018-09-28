from datetime import datetime

from indicator.returns import AbsoluteReturn, DailyReturn, CummulativeDailyReturn
from manager import quotes_manager
import pandas as pd
import matplotlib.pyplot as plt

def test_returns_hist(symbol, start_date: datetime, end_date: datetime,ind_return,ax):
    df_main = pd.DataFrame(index=pd.date_range(start_date,end_date))
    df_temp = quotes_manager.get_daily_quotes(start_date,end_date,symbol)
    df_main = df_main.join(df_temp[quotes_manager.COL_ADJ_CLOSE]).rename(columns={quotes_manager.COL_ADJ_CLOSE:symbol})

    df_main.dropna(inplace=True)

    ind_return.calculate_ind_into_df(df_main,symbol)

    ind_column_name = ind_return.get_column_name(symbol)

    mean = df_main[ind_column_name].mean()
    print(ind_column_name + ' mean=' + str(mean))
    std = df_main[ind_column_name].std()
    print(ind_column_name + ' std=' + str(std))
    kurtosis = df_main[ind_column_name].kurtosis()
    # to check if the tail of the histogran is aligned with a normal distribution or not
    print(ind_column_name + ' kurtosis=' + str(kurtosis))


    ax = df_main[ind_column_name].hist(ax=ax,bins=20)
    ax.axvline(mean,color='w', linestyle='dashed', linewidth=2)
    ax.axvline(std, color='r', linestyle='dashed', linewidth=2)
    ax.axvline(-std, color='r', linestyle='dashed', linewidth=2)

start_date = datetime(2015, 7, 1)
end_date = datetime(2018, 8, 15)

fig, axes = plt.subplots(nrows=1, ncols=2,figsize=(15,15))

test_returns_hist('SPX', start_date, end_date, CummulativeDailyReturn(), axes[0])
test_returns_hist('SPX',start_date,end_date,DailyReturn(),axes[1])

plt.show()
