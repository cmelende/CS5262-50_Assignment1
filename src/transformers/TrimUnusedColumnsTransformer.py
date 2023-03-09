from sklearn.base import BaseEstimator, TransformerMixin
from typing import List


class TrimUnusedColumnsTransformer(BaseEstimator, TransformerMixin):

    def __init__(self, keep_columns: List[str]):
        self.keepColumns: List[str] = keep_columns

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X_ = X.copy()
        X_ = X_[self.keepColumns]
        return X_
