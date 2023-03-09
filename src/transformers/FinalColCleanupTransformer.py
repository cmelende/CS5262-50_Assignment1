from sklearn.base import BaseEstimator, TransformerMixin


class FinalColCleanup(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X.drop(columns=['Name'], inplace=True)
        return X
