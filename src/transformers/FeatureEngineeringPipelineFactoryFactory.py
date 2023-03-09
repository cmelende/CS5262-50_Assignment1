from typing import List, Dict
import pandas as pd
from src.transformers.FeatureEngineeringPipelineConfig import FeatureEngineeringPipelineConfig
from src.transformers.FeatureEngineeringPipelineConstants import FeatureEngineeringPipelineConstants
from src.transformers.FeatureEngineeringPipelineFactory import FeatureEngineeringPipelineFactory


class FeatureEngineeringPipelineFactoryFactory:
    def __init__(self, additional__exchange_dfs: List[pd.DataFrame]):
        self.additionalExchangeDfs = additional__exchange_dfs

    def create(self, target_stock: str, number_of_back_days: List[int],
               includeDaysBackFeature: bool, includeTotalChangeOverDaysFeature: bool) \
            -> FeatureEngineeringPipelineFactory:

        pipeline_constants = FeatureEngineeringPipelineConstants(const.STOCK_COLS,
                                                                 const.TREASURY_COLS,
                                                                 const.COMMON_COLS,
                                                                 const.STOCKS_BY_INDUSTRY)

        config = FeatureEngineeringPipelineConfig(self.additionalExchangeDfs,
                                                  pipeline_constants,
                                                  number_of_back_days,
                                                  target_stock, includeDaysBackFeature,
                                                  includeTotalChangeOverDaysFeature)

        return FeatureEngineeringPipelineFactory(config)

    def create_many(self,
                    target_stocks: List[str],
                    number_of_back_day_combinations: List[List[int]],
                    includeDaysBackFeature: bool,
                    includeTotalChangeOverDaysFeature: bool) -> Dict[str, FeatureEngineeringPipelineFactory]:

        ret: Dict[str, FeatureEngineeringPipelineFactory] = {}

        for target_stock in target_stocks:
            for n in number_of_back_day_combinations:
                ret[target_stock] = self.create(target_stock,
                                                n,
                                                includeDaysBackFeature,
                                                includeTotalChangeOverDaysFeature)

        return ret
