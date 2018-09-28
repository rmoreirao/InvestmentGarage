import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import scipy.optimize as spo

from datetime import datetime

from indicator.returns import NormalizedDailyReturn, DailyReturn, CummulativeDailyReturn
from manager import quotes_manager
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def calculate_portifolio(start_portfolio_value,start_date,end_date, symbols,use_quotes_cache=True):
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

    def find_best_allocation(allocs):
        df_allocations = df_normalized_returns * (allocs / 100)
        df_portfolio_value = df_allocations.sum(axis=1)
        portifolio_daily_ret = df_portfolio_value.pct_change().dropna()
        avg_daily_return = portifolio_daily_ret.mean()
        std_daily_return = portifolio_daily_ret.std()
        sharpe = np.sqrt(252) * ((avg_daily_return - 0.0) / std_daily_return)
        return sharpe * -1

    # guess allocation, just a simple distribution
    guess_alloc = np.full(len(symbols), 100 / len(symbols))

    # limiting the values to be from 0 to 100
    bounds = [(0, 100) for x in range(len(symbols))]

    # only satisfied when sum of elements is 1.
    cons = ({'type': 'eq', 'fun': lambda x: 100 - np.sum(x)})
    result = spo.minimize(find_best_allocation, guess_alloc, bounds=bounds, constraints=cons, method='SLSQP',
                          options={'disp': True})
    allocations = result.x / 100
    print('Calculated Sharpe = ' + str(result.fun))
    print('Calculated Allocations = ' + str(allocations))

    df_allocations = df_normalized_returns * allocations
    df_position_value = df_allocations * start_portfolio_value
    df_portfolio_value = df_position_value.sum(axis=1)

    day_ret = DailyReturn()
    day_ret_series = day_ret.calculate_ind_series(df_portfolio_value)
    avg_daily_return = day_ret_series.mean()
    # Risk, Vol
    std_daily_return = day_ret_series.std()
    end_value = df_portfolio_value.iloc[-1]
    cum_return = (end_value / start_portfolio_value) - 1
    rf = 0.
    sharpe = np.sqrt(252) * ((avg_daily_return - rf) / std_daily_return)

    print('Statistics for ' + str(symbols))
    print('avg_daily_return = ' + str(avg_daily_return))
    print('std_daily_return = ' + str(std_daily_return))
    print('end_value = ' + str(end_value))
    print('cum_return = ' + str(cum_return))
    print('sharpe = ' + str(sharpe))

    return df_quotes, df_normalized_returns, df_allocations, df_position_value, df_portfolio_value


start_portfolio_value = 1000000.0
start_date = datetime(2017, 1, 1)
end_date = datetime(2017, 12, 30)
symbols = ['GOOG', 'AAPL', 'GLD' , 'XOM']
allocations = [0.4,0.4,0.1,0.1]

df_quotes,df_normalized_returns,df_allocations,df_position_value,df_portfolio_value = calculate_portifolio(start_portfolio_value,start_date,end_date, symbols)

symbols_spx = ['SPX']
allocations_spx = [1]

df_quotes_spx,df_normalized_returns_spx,df_allocations_spx,df_position_value_spx,df_portfolio_value_spx = calculate_portifolio(start_portfolio_value,start_date,end_date, symbols_spx)

df_portifolio_value_compare = df_portfolio_value.to_frame('Portifolio').join(df_portfolio_value_spx.to_frame('SPX'))
df_portifolio_value_compare.plot(figsize=(15,10))
plt.title('Portifolio x SPX')
plt.show()