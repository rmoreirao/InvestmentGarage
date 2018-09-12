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

_cache_folder = None

def get_daily_quotes(start_date: datetime, end_date: datetime, symbol:str):
    if not _cache_folder:
        curr_path_parts = list(Path.cwd().parts)
        for i in reversed(range(len(curr_path_parts))):
            if curr_path_parts[i] != 'InvestimentGarage':
                curr_path_parts.pop(i)
            else:
                break
        _cache_folder = Path(curr_path_parts)
    file_path =  '../quotes_cache/' + symbol + '.pkl'
    df: pd.DataFrame
    if Path(file_path).is_file():
        df = pd.read_pickle(file_path)
    else:
        ts = TimeSeries(key='ZXTHHYQU7E5O8R75', output_format='pandas')
        df, meta_data = ts.get_daily_adjusted(symbol=symbol, outputsize='compact')
        try:
            df.to_pickle(file_path)
        except:
            print("Error trying to save pickle quote: " + file_path)
    return df.ix[start_date.strftime('%Y-%m-%d'):end_date.strftime('%Y-%m-%d')]


