from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd


class AddExchangeCloseVolumeTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, source: pd.DataFrame):
        self.source = source

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X_ = X.copy()
        exchange_name = self.source.loc[0, 'Name']
        X_[f'{exchange_name}_Close'] = self.source[f'Close']
        X_[f'{exchange_name}_Volume'] = self.source[f'Volume']
        return X_
