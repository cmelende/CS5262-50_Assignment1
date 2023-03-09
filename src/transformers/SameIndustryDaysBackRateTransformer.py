import DaysBackRateTransformer
from typing import Dict


class SameIndustryDaysBackRateTransformer(DaysBackRateTransformer):
    def __init__(self, industry_by_stock: Dict[str, str], targetStock: str, numberOfDays: int):
        super().__init__(targetStock, numberOfDays)
        self.industryByStock = industry_by_stock

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X_ = X.copy()
        target_stock_industry = self.industryByStock[self.targetStock]

        for key in self.industryByStock:
            if self.industryByStock[key] == target_stock_industry and key != self.targetStock:
                X_ = self.add_target_stock_day_rate(X_, key)

        return X_
