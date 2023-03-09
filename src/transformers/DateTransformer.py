from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd


class DateTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X_=X.copy()
        X_['Date'] = pd.to_datetime(X_['Date'])
        X_['Year'] = X_['Date'].dt.year
        X_['Month'] = X_['Date'].dt.month
        X_['DayOfMonth'] = X_['Date'].dt.day
        X_['DayOfWeek'] = X_['Date'].dt.dayofweek

        X_.drop(columns=['Date'], inplace=True)
        return X_

