from typing import List, Dict


class FeatureEngineeringPipelineConstants:
    def __init__(self, stockSymbols: List[str], treasurySymbols: List[str], common_cols: List[str],
                 industryByStock: Dict[str, str]):
        self.stockSymbols: List[str] = stockSymbols
        self.treasurySymbols: List[str] = treasurySymbols
        self.commonColumns: List[str] = common_cols
        self.industryByStock: Dict[str, str] = industryByStock
