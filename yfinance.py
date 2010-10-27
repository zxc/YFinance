#
# yfinance.py
# -----------
# API for Yahoo Finance
#
import urllib

class StockFormat(object):
    def __init__(self, name, code): 
        self.name = [name] if isinstance(name, str) else name
        self.code = code
    def __and__(self, other): return StockFormat(self.name + other.name,
                                                 self.code + other.code)
    def __repr__(self): return self.code

    def __call__(self, symbol): return get(symbol, self.code)[0]

price                          = StockFormat('price', 'l1')
change                         = StockFormat('change', 'c1')
volume                         = StockFormat('volume', 'v')
average_daily_volume           = StockFormat('average_daily_volume', 'a2')
exchange                       = StockFormat('exchange', 'x')
market_cap                     = StockFormat('market_cap', 'j1')
book_value                     = StockFormat('book_value', 'b4')
ebitda                         = StockFormat('ebitda', 'j4')
dividend_per_share             = StockFormat('dividend_per_share', 'd')
dividend_yield                 = StockFormat('dividend_yield', 'y')
earnings_per_share             = StockFormat('earnings_per_share', 'e')
i52_week_high                  = StockFormat('52_week_high', 'k')
i52_week_low                   = StockFormat('52_week_low', 'j')
i50_day_moving_average         = StockFormat('50_day_moving_average', 'm3')
i200_day_moving_average        = StockFormat('200_day_moving_average', 'm4')
price_to_earnings_ratio        = StockFormat('price_to_earnings_ratio', 'r')
price_to_earnings_growth_ratio = StockFormat('price_to_earnings_growth_ratio', 'r5')
price_to_sales_ratio           = StockFormat('price_to_sales_ratio', 'p5')
price_to_book_ratio            = StockFormat('price_to_book_ratio', 'p6')
short_ratio                    = StockFormat('short_ratio', 's7')

def get(symbol, format):
    if isinstance(format, StockFormat):
        url = 'http://finance.yahoo.com/d/quotes?s=%s&f=%s' % (symbol, format.code)
        data = [x.strip('"') for x in urllib.urlopen(url).read().strip().split(',')]
        return dict((format.name[i], data[i]) for i in range(len(format.name)))
    else:
        url = 'http://finance.yahoo.com/d/quotes?s=%s&f=%s' % (symbol, format)
        return [x.strip('"') for x in urllib.urlopen(url).read().strip().split(',')]

def get_all(symbol):
    return get(symbol, price & change & volume & average_daily_volume &
                       exchange & market_cap & book_value & ebitda &
                       dividend_per_share & dividend_yield & earnings_per_share &
                       i52_week_high & i52_week_low & i50_day_moving_average &
                       i200_day_moving_average & price_to_earnings_ratio &
                       price_to_earnings_growth_ratio & price_to_sales_ratio &
                       price_to_book_ratio & short_ratio)
