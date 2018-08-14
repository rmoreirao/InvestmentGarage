import domain
from domain.order import order_type, order
from domain.order import portfolio
from manager import quotes_manager
from datetime import datetime
import pandas as pd


df_quotes: pd.DataFrame
start_date = datetime(2018, 7, 1)
end_date = datetime(2018, 7, 15)
df_quotes = quotes_manager.get_daily_quotes(start_date, end_date, 'AAPL')
print(df_quotes)
# df_quotes['close'].pct_change()

df_quotes['ClosePctChange'] = df_quotes['4. close'].pct_change()

rand_portfolio = portfolio('random')

for index, row in df_quotes.iterrows():
   if not pd.isna(row['ClosePctChange']):
       if row['ClosePctChange'] >0:
           type = order_type.SELL
       else:
           type = order_type.BUY

       rand_portfolio.add_order(order(type,'AAPL',1000,row['4. close'], datetime.strptime(row.name, '%Y-%m-%d')))

print(rand_portfolio.calculate_positions_df(start_date,end_date))
