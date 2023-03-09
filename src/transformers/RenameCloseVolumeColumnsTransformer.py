from sklearn.base import BaseEstimator, TransformerMixin


class RenameCloseVolumeColumnsTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X_ = X.copy()
        exchange_name = X.loc[0, 'Name']
        return X_.rename(columns={'Close': f'{exchange_name}_Close', 'Volume': f'{exchange_name}_Volume'})
