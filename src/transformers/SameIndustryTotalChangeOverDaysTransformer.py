import TotalChangeOverDaysTransformer
from typing import Dict


class SameIndustryTotalChangeOverDaysTransformer(TotalChangeOverDaysTransformer):
    def __init__(self, industryByStock: Dict[str,str], overDays: int, targetStock: str):
        super().__init__(overDays, targetStock)
        self.industryByStock = industryByStock

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X_ = X.copy()
        target_stock_industry = self.industryByStock

        for key in self.industryByStock:
            if self.industryByStock[key] == target_stock_industry and key != self.targetStock:
                X_ = self.add_total_change(X_, self.targetStock)

        return X_
