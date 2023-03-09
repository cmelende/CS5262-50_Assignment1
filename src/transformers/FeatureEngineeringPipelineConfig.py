from typing import List
import FeatureEngineeringPipelineConstants
import pandas as pd


class FeatureEngineeringPipelineConfig:
    def __init__(self, dataframes: List[pd.DataFrame], pipeline_constants: FeatureEngineeringPipelineConstants,
                 daysBack: List[int], targetStock: str, includeDaysBackFeature: bool = True,
                 includeTotalChangeOverDaysFeature: bool = True):

        self.constants: FeatureEngineeringPipelineConstants = pipeline_constants
        self.dataframes: List[pd.DataFrames] = dataframes
        self.targetStock: str = targetStock
        self.daysBack = daysBack
        self.includeDaysBackFeature = includeDaysBackFeature
        self.includeTotalChangeOverDaysFeature = includeTotalChangeOverDaysFeature
