
from datetime import datetime

from indicator import moving_std, moving_avg
from indicator.base_indicator import BaseIndicatorMultCol
from indicator.moving_avg import SimpleMovingAvg, ExponentialMovingAvg
from indicator.moving_std import MovingStd
from manager import quotes_manager
import pandas as pd
import matplotlib.pyplot as plt

class BollingerBandsBase(BaseIndicatorMultCol):
    LOWER_BAND = 'LowerBand'
    UPPER_BAND = 'UpperBand'

    def __init__(self,sm_indicator_calc,window:int,n_std:int):
        self.sm_indicator_calc = sm_indicator_calc
        self.n_std = n_std
        self.window = window

    def get_column_names(self):
        return [self.UPPER_BAND, self.LOWER_BAND, self.sm_indicator_calc.get_ind_column_name()]

    def calculate_ind(self, df: pd.DataFrame, symbol: str):
        mov_std = MovingStd(self.window)
        mov_std_series = mov_std.calculate_ind(df,symbol)

        sm_series = self.sm_indicator_calc.calculate_ind(df,symbol)

        return [sm_series + (self.n_std * mov_std_series),
            sm_series - (self.n_std * mov_std_series),
                sm_series]

class BollingerBandsSMA(BollingerBandsBase):
    def __init__(self,window:int,n_std:int):
        sma = SimpleMovingAvg(window)
        super().__init__(sma,window,n_std)

class BollingerBandsEMA(BollingerBandsBase):
    def __init__(self,window:int,n_std:int):
        ema = ExponentialMovingAvg(window)
        super().__init__(ema,window,n_std)

def bollinger_bands_test(symbol, start_date: datetime, end_date: datetime,window:int, n_std:int):
    df = quotes_manager.get_daily_quotes(start_date,end_date,symbol)
    df = df.rename(columns={quotes_manager.COL_ADJ_CLOSE:symbol})[[symbol]]

    boll_band_sma = BollingerBandsSMA(window,n_std)
    boll_band_sma_df = boll_band_sma.calculate_ind_into_df(df,symbol)
    boll_band_sma_df.plot(figsize=(12,6))
    plt.show()

    boll_band_ema = BollingerBandsEMA(window, n_std)
    boll_band_ema_df = boll_band_ema.calculate_ind_into_df(df, symbol)
    boll_band_ema_df.plot(figsize=(12, 6))
    plt.show()

start_date = datetime(2015, 7, 1)
end_date = datetime(2018, 8, 15)

bollinger_bands_test('AAPL',start_date,end_date,20,2)