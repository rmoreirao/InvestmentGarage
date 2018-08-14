from datetime import datetime
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import pandas as pd

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

def get_daily_quotes(start_date: datetime, end_date: datetime, symbol:str):
    ts = TimeSeries(key='ZXTHHYQU7E5O8R75', output_format='pandas')
    data:pd.DataFrame
    data, meta_data = ts.get_daily_adjusted(symbol=symbol, outputsize='compact')
    print (data.columns.values)
    return data.ix[start_date.strftime('%Y-%m-%d'):end_date.strftime('%Y-%m-%d')]

