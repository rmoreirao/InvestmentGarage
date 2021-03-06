from abc import abstractmethod

import pandas as pd


class BaseIndicatorSingCol:

    @abstractmethod
    def get_ind_column_name(self):
        pass

    def get_column_name(self,symbol):
        return self.get_ind_column_name() + '_' + symbol

    @abstractmethod
    def calculate_ind(self, df: pd.DataFrame, symbol: str):
        pass

    def calculate_ind_into_df(self, df: pd.DataFrame, symbol: str):
        df[self.get_column_name(symbol)] = self.calculate_ind(df, symbol)


class BaseIndicatorMultCol:

    @abstractmethod
    def get_column_names(self):
        pass

    @abstractmethod
    def calculate_ind(self, df: pd.DataFrame, symbol: str):
        pass

    def calculate_ind_into_df(self, df: pd.DataFrame, symbol: str, inplace=False):
        if not inplace:
            df = df.copy()

        for i in range(len(self.get_column_names())):
            column_name = self.get_column_names()[i] + '_' + symbol
            ind = self.calculate_ind(df, symbol)[i]
            df[column_name] = ind

        return df