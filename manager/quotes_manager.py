from datetime import datetime

import pathlib
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path,WindowsPath


# print(data)
# data[['4. close']].plot()
# plt.title('Intraday Times Series for the MSFT stock (1 min)')
# plt.show()

COL_DATE = 'date'
COL_OPEN = '1. open'
COL_HIGH = '2. high'
COL_LOW = '3. low'
COL_CLOSE = '4. close'
COL_ADJ_CLOSE = '5. adjusted close'
COL_VOL = '6. volume'
COL_DIV = '7. dividend amount'
COL_SPLIT = '8. split coefficient'
COL_SYMBOL = 'symbol'

def __get_quotes_cache_folder():
    curr_path = Path.cwd()
    return next(path for path in curr_path.parents if path.name =='InvestmentGarage')

# _get_quotes_cache_folder = memoize(__get_quotes_cache_folder)

def get_daily_quotes(start_date: datetime, end_date: datetime, symbol:str, use_cache=True):
    quotes_cache_path:Path = __get_quotes_cache_folder()
    quotes_cache_path = quotes_cache_path / 'quotes_cache' / (symbol + '.pkl')
    file_path =  quotes_cache_path.as_posix()
    df: pd.DataFrame
    if Path(file_path).is_file() and use_cache:
        df = pd.read_pickle(file_path)
    else:
        ts = TimeSeries(key='ZXTHHYQU7E5O8R75', output_format='pandas')
        df, meta_data = ts.get_daily_adjusted(symbol=symbol, outputsize='full')
        try:
            df.to_pickle(file_path)
        except:
            print("Error trying to save pickle quote: " + file_path)

    return df.ix[start_date.strftime('%Y-%m-%d'):end_date.strftime('%Y-%m-%d')]

def test_get_daily_quotes():
    start_date = datetime(2015, 7, 1)
    end_date = datetime(2018, 8, 15)
    symbol = 'AAPL'
    get_daily_quotes(start_date,end_date,symbol)

test_get_daily_quotes()