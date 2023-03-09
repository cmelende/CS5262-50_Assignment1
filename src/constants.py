from typing import List, Dict

random_seed = 42
OIL = "Oil"
GOLD = "Gold"
XOM = "XOM"
JPM = "JPM"
GE = "GE"
JNJ = "JNJ"
WFC = "WFC"
AMZN = "AMZN"
MSFT = "MSFT"

STOCK_COLS: List[str] = [
    OIL, GOLD, XOM, JPM, GE, JNJ, WFC, AMZN, MSFT
]

DTB4WK = "DTB4WK"
DTB3 = "DTB3"
DTB6 = "DTB6"
DGS5 = "DGS5"
DGS10 = "DGS10"

TREASURY_COLS: List[str] = [
    DTB4WK, DTB3, DTB6, DGS5, DGS10
]

STOCKS_BY_INDUSTRY: Dict[str, str] = {
    OIL: 'oil & gas',
    GOLD: 'industrial metal',
    XOM: 'oil & gas',
    JPM: 'banking',
    GE: 'industrial machinery',
    JNJ: 'drugs',
    WFC: 'banking',
    AMZN: 'tech',
    MSFT: 'tech'
}
# ['oil & gas', 'industrial metal', 'Banking', 'industrial machinery', 'drugs', ]
COMMON_COLS: List[str] = [
                             'Date', 'Close', 'Volume',
                             # Add this for convenience
                             'Name'
                         ] + TREASURY_COLS + STOCK_COLS

# columns that need to be calculated
CALC_COLS = [
    # dow jones
    'DJI',
    # ny stock exchang
    'NYSE',
    # russel
    'RUSSEL',
    # s&p 500
    'GSPC',
    # nasdaq
    'IXIC'
]
