from sklearn.base import BaseEstimator, TransformerMixin


class TreasuryRateTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, target_treasury: str, back_number_of_days: int):
        self.targetTreasury: str = target_treasury
        self.backNumberOfDays: int = back_number_of_days

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X_ = X.copy()

        for i in range(self.backNumberOfDays, len(X)):
            X_.loc[i, f'{self.targetTreasury}_Last_{self.backNumberOfDays}_Yield_Change'] \
                = X_.loc[i, self.targetTreasury] - X_.loc[i - self.backNumberOfDays, self.targetTreasury]

        return X_
