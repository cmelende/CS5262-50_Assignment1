from sklearn.pipeline import Pipeline

from src.transformers.AddExchangeCloseVolumeTransformer import AddExchangeCloseVolumeTransformer
from src.transformers.DateToQuarterTransformer import DateToQuarterTransformer
from src.transformers.DaysBackRateTransformer import DaysBackRateTransformer
from src.transformers.ExchangeCloseRateChangeTransformer import ExchangeCloseRateChangeTransformer
from src.transformers.ExchangeVolumeChangeOverTimeTransformer import ExchangeVolumeChangeOverTime
from src.transformers.FeatureEngineeringPipelineConfig import FeatureEngineeringPipelineConfig
from src.transformers.FinalColCleanupTransformer import FinalColCleanup
from src.transformers.RenameCloseVolumeColumnsTransformer import RenameCloseVolumeColumnsTransformer
from src.transformers.TotalChangeOverDaysTransformer import TotalChangeOverDaysTransformer
from src.transformers.TreasuryRateTransformer import TreasuryRateTransformer
from src.transformers.TrimUnusedColumnsTransformer import TrimUnusedColumnsTransformer
import sklearn as skl

from src.transformers.WouldProfitTargetTransformer import WouldProfitTargetTransformer


class FeatureEngineeringPipelineFactory:
    def __init__(self, config: FeatureEngineeringPipelineConfig):
        self.config = config

    def __create_add_exchange_close_volume_transformers(self):
        l = []

        for i in range(0, len(self.config.dataframes)):
            l.append(
                (f'use_add_df{i}_exchange_transformer', AddExchangeCloseVolumeTransformer(self.config.dataframes[i])))

        return l

    def __create_days_back_rate_transformers(self):
        l = []

        for stock_symbol in self.config.constants.stockSymbols:
            for n in self.config.daysBack:
                l.append(
                    (f'use_{n}_days_back_rate_transformer_{stock_symbol}', DaysBackRateTransformer(stock_symbol, n)))

        return l

    def __create_exchange_close_rate_change(self):
        l = []

        for df in self.config.dataframes:
            exchange_name = df.loc[0, 'Name']
            for n in self.config.daysBack:
                l.append((f'use_exchange_{exchange_name}_close_rate_over_{n}_days_transformer',
                          ExchangeCloseRateChangeTransformer(exchange_name, n)))

        return l

    def __create_exchange_volume_change_over_time_transformers(self):
        l = []

        for df in self.config.dataframes:
            exchange_name = df.loc[0, 'Name']
            for n in self.config.daysBack:
                l.append((f'use_exchange_{exchange_name}_volume_change_over_{n}_days',
                          ExchangeVolumeChangeOverTime(exchange_name, n)))

        return l

    def __create_total_change_over_days_transformers(self):
        l = []

        days = self.config.daysBack
        for stock_symbol in self.config.constants.stockSymbols:
            for n in days:
                l.append((f'use_total_change_over_{n}_day_transformer_{stock_symbol}',
                          TotalChangeOverDaysTransformer(n, stock_symbol)))

        return l

    def __create_treasury_yield_rate_change_transformers(self):
        l = []

        for treasury in self.config.constants.treasurySymbols:
            for n in self.config.daysBack:
                l.append((f'use_treasury_{n}_yield_rate_change_{treasury}', TreasuryRateTransformer(treasury, n)))

        return l

    def create(self) -> skl.pipeline.Pipeline:
        cleanup_steps = [
            ("use_trim_unused_columns_transformer", TrimUnusedColumnsTransformer(self.config.constants.commonColumns)),
            # ("use_date_transformer", DateTransformer()),
            ("use_date_to_quarter_transformer", DateToQuarterTransformer()),
            ("use_rename_close_volume_columns_transformer", RenameCloseVolumeColumnsTransformer()),
        ]

        pipeline_steps: list = cleanup_steps
        pipeline_steps.extend(self.__create_add_exchange_close_volume_transformers())
        pipeline_steps.extend(self.__create_exchange_close_rate_change())
        pipeline_steps.extend(self.__create_exchange_volume_change_over_time_transformers())

        if self.config.includeDaysBackFeature:
            pipeline_steps.extend(self.__create_days_back_rate_transformers())

        if self.config.includeTotalChangeOverDaysFeature:
            pipeline_steps.extend(self.__create_total_change_over_days_transformers())

        pipeline_steps.extend(self.__create_treasury_yield_rate_change_transformers())
        pipeline_steps.extend(
            [('use_would_profit_target_transformer', WouldProfitTargetTransformer(self.config.targetStock))])
        pipeline_steps.extend([('use_final_col_cleanup_transformer', FinalColCleanup())])

        return Pipeline(
            steps=pipeline_steps
        )
