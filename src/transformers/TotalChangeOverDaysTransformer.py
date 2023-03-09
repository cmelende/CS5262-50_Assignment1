from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd


class TotalChangeOverDaysTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, overDays: int, targetStock: str):
        self.overDays = overDays
        self.targetStock = targetStock

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X_ = X.copy()
        return self.add_total_change(X_, self.targetStock)

    def add_total_change(self, X_: pd.DataFrame, total_change_stock: str):
        for i in range(self.overDays - 1, len(X_)):
            X_.loc[i, f'{total_change_stock}_TotalChange_Last_{self.overDays}_Days'] \
                = self.phi(X_.loc[i - self.overDays + 1:i, total_change_stock].values.tolist())
        return X_

    @staticmethod
    def phi(numbers):
        product = 1
        for n in numbers:
            mult = (1+n)
            if mult == 1:
                mult = 1

            product *= mult
        return product
