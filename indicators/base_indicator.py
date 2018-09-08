from abc import abstractmethod

import pandas as pd


class base_indicator:

    @abstractmethod
    def get_column_name(self):
        pass

    @abstractmethod
    def calculate_ind(self, df: pd.DataFrame,symbol:str):
        pass

    def calculate_ind_into_df(self, df: pd.DataFrame,symbol:str):
        df[self.get_column_name()] = self.calculate_ind(df,symbol)

