from typing import List

import pandas as pd


def load_nyse() -> pd.DataFrame:
    nyse_file = 'Processed_NYSE.csv'
    return pd.read_csv(nyse_file)


def load_additional_exchanges() -> List[pd.DataFrame]:
    dji_file = 'Processed_DJI.csv'
    nasdaq_file = 'Processed_NASDAQ.csv'
    russel_file = 'Processed_RUSSELL.csv'
    sp_file = 'Processed_S&P.csv'

    dji_df = pd.read_csv(dji_file)
    nasdaq_df = pd.read_csv(nasdaq_file)
    russel_df = pd.read_csv(russel_file)
    sp_df = pd.read_csv(sp_file)

    return [dji_df, nasdaq_df, russel_df, sp_df]
