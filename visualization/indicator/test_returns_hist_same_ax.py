from datetime import datetime

from indicator.returns import AbsoluteReturn, DailyReturn, CummulativeDailyReturn
from manager import quotes_manager
import pandas as pd
import matplotlib.pyplot as plt

start_date = datetime(2015, 7, 1)
end_date = datetime(2018, 8, 15)


def test_returns_hist_same_ax(symbol, start_date: datetime, end_date: datetime,ind_return):
    df_main = pd.DataFrame(index=pd.date_range(start_date,end_date))
    df_temp = quotes_manager.get_daily_quotes(start_date,end_date,symbol)
    df_main = df_main.join(df_temp[quotes_manager.COL_ADJ_CLOSE]).rename(columns={quotes_manager.COL_ADJ_CLOSE:symbol})

    df_main.dropna(inplace=True)
    ind_return.calculate_ind_into_df(df_main,symbol)
    ind_column_name = ind_return.get_column_name(symbol)
    df_main[ind_column_name].hist(bins=30,alpha=0.5, label=symbol)

test_returns_hist_same_ax('SPX', start_date, end_date, DailyReturn())
test_returns_hist_same_ax('AAPL', start_date, end_date, DailyReturn())

plt.legend(loc='upper right')
plt.show()