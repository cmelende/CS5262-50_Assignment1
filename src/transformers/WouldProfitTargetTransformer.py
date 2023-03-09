from sklearn.base import BaseEstimator, TransformerMixin


class WouldProfitTargetTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, targetStock: str):
        self.targetStock = targetStock

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X_=X.copy()
        for i in range(0, len(X)-1):
            if X_.loc[i + 1, f'{self.targetStock}'] > 0:
                X_.loc[i, f'{self.targetStock}_WouldProfit'] = 'invest'
            else:
                X_.loc[i, f'{self.targetStock}_WouldProfit'] = 'abstain'
        return X_

