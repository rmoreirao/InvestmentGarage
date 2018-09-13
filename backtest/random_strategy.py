import domain
from domain.order import order
from domain.order_type import order_type
from domain.portfolio import portfolio
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


df_positions = rand_portfolio.calculate_positions_df(start_date,end_date)
print(df_positions)

last_close_price = df_quotes.tail(1).iloc[0]['4. close']

last_position = df_positions.tail(1).iloc[0]['AAPL']

rand_portfolio.add_order(order(type,'AAPL',last_position,last_close_price, end_date))

print(rand_portfolio.calculate_positions_df(start_date,end_date))