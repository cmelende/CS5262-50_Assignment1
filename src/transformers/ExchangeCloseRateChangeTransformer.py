from sklearn.base import BaseEstimator, TransformerMixin


class ExchangeCloseRateChangeTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, exchangeName: str, overDays: int):
        self.exchangeName = exchangeName
        self.overDays = overDays

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X_ = X.copy()

        for i in range(self.overDays, len(X_)):
            X_.loc[i, f'{self.exchangeName}_Close_Rate_Change_Over_{self.overDays}_Days'] \
                = 1 - (X_.loc[i, f'{self.exchangeName}_Close'] / X_.loc[i-self.overDays, f'{self.exchangeName}_Close'])

        return X_
