from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd


# calculate the rate of change from the previous two days and drop the first day
# we'll use this transformer as a stand-in until an issue with the one hot encoder
# in our pipelin is resolved
class DateToQuarterTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X_ = X.copy()

        X_['Date'] = pd.to_datetime(X_['Date'])
        for i in range(0, len(X_)):
            month = X_.loc[i, 'Date'].month
            if 1 <= month <= 3:
                X_.loc[i, 'Quarter 1'] = 1
                X_.loc[i, 'Quarter 2'] = 0
                X_.loc[i, 'Quarter 3'] = 0
                X_.loc[i, 'Quarter 4'] = 0
            elif 4 <= month <= 6:
                X_.loc[i, 'Quarter 1'] = 0
                X_.loc[i, 'Quarter 2'] = 1
                X_.loc[i, 'Quarter 3'] = 0
                X_.loc[i, 'Quarter 4'] = 0
            elif 7 <= month <= 9:
                X_.loc[i, 'Quarter 1'] = 0
                X_.loc[i, 'Quarter 2'] = 0
                X_.loc[i, 'Quarter 3'] = 1
                X_.loc[i, 'Quarter 4'] = 0
            else:
                X_.loc[i, 'Quarter 1'] = 0
                X_.loc[i, 'Quarter 2'] = 0
                X_.loc[i, 'Quarter 3'] = 0
                X_.loc[i, 'Quarter 4'] = 1

        # X_['DayOfWeek'] = X_['Date'].dt.dayofweek
        # X_['Month'] = X_['Date'].dt.month
        # X_['Year'] = X_['Date'].dt.year
        # X_['Day'] = X_['Date'].dt.day

        X_.drop(columns=['Date'], inplace=True)

        return X_
