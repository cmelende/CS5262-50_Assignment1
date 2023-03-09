from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd


class DaysBackRateTransformer(BaseEstimator, TransformerMixin):

    def __init__(self, target_stock: str, number_of_days: int):
        self.targetStock: str = target_stock
        self.numberOfDays: int = number_of_days

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X_ = X.copy()
        return self.add_target_stock_day_rate(X_, self.targetStock)

    def add_target_stock_day_rate(self, X_: pd.DataFrame, stock_day_rate: str):
        for i in range(self.numberOfDays, len(X_)):
            X_.loc[i, f'{stock_day_rate}_-{self.numberOfDays}_DayRate'] = X_.loc[i - self.numberOfDays, stock_day_rate]
        return X_
