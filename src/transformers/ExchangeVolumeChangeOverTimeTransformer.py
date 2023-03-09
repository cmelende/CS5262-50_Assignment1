from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd


class ExchangeVolumeChangeOverTime(BaseEstimator, TransformerMixin):
    def __init__(self, exchangeName: str, overDays: int):
        self.exchangeName = exchangeName
        self.overDays = overDays

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X_ = X.copy()
        return self.add_total_change(X)

    def add_total_change(self, X_: pd.DataFrame):
        for i in range(self.overDays - 1, len(X_)):
            X_.loc[i, f'{self.exchangeName}_Volume_Change_Over_{self.overDays}_Days'] \
                = self.phi(X_.loc[i - self.overDays + 1:i, f'{self.exchangeName}_Volume'].values.tolist())
        return X_

    @staticmethod
    def phi(numbers):
        product = 1
        for n in numbers:
            product *= (1 + n)
        return product
