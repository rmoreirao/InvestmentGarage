from datetime import datetime

from indicator.returns import NormalizedDailyReturn
from manager import quotes_manager
import pandas as pd
import matplotlib.pyplot as plt

def calculate_portifolio(start_portfolio_value,start_date,end_date, symbols,allocations,use_quotes_cache=True):
    global df_normalized_returns, df_allocations, df_position_value, df_portfolio_value
    df_quotes = pd.DataFrame(index=pd.date_range(start_date, end_date))
    for symbol in symbols:
        df_temp = quotes_manager.get_daily_quotes(start_date, end_date, symbol, use_cache=use_quotes_cache)
        df_quotes = df_quotes.join(df_temp[quotes_manager.COL_ADJ_CLOSE]).rename(
            columns={quotes_manager.COL_ADJ_CLOSE: symbol})
    df_quotes.dropna(inplace=True)
    df_normalized_returns = pd.DataFrame(index=pd.date_range(start_date, end_date))
    norm_ret = NormalizedDailyReturn()
    for symbol in symbols:
        df_normalized_returns = df_normalized_returns.join(norm_ret.calculate_ind_series(df_quotes[symbol]))
    df_normalized_returns.dropna(inplace=True)
    df_allocations = df_normalized_returns * allocations
    df_position_value = df_allocations * start_portfolio_value
    df_portfolio_value = df_position_value.sum(axis=1)

    return df_quotes,df_normalized_returns,df_allocations,df_position_value,df_portfolio_value

start_portfolio_value = 1000000.0
start_date = datetime(2017, 1, 1)
end_date = datetime(2017, 12, 30)
symbols = ['GOOG', 'AAPL', 'GLD' , 'XOM']
allocations = [0.4,0.4,0.1,0.1]

df_quotes,df_normalized_returns,df_allocations,df_position_value,df_portfolio_value = calculate_portifolio(start_portfolio_value,start_date,end_date, symbols,allocations)

symbols_spx = ['SPX']
allocations_spx = [1]

df_quotes_spx,df_normalized_returns_spx,df_allocations_spx,df_position_value_spx,df_portfolio_value_spx = calculate_portifolio(start_portfolio_value,start_date,end_date, symbols_spx,allocations_spx)

# df_normalized_returns.plot(figsize=(15,10))
# plt.title('df_normalized_returns')
# plt.show()
#
# df_allocations.plot(figsize=(15,10))
# plt.title('df_allocations')
# plt.show()
#
# df_position_value.plot(figsize=(15,10))
# plt.title('df_position_value')
# plt.show()
#
# df_portfolio_value.plot(figsize=(15,10))
# plt.title('df_portfolio_value')
# plt.show()

plt.figure(figsize=(15,10))
ax1 = df_portfolio_value.plot(color='Blue',label='Portifolio')
ax2 = df_portfolio_value_spx.plot(color='Red',label='SPX',secondary_y=True)

h1, l1 = ax1.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()

plt.title('Portifolio x SPX')


plt.show()