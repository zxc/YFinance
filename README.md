
YFinance
========

* YFinance is a small Python library to pull stock data from Yahoo Finance.


How To
------

* Get a stock's price:

        import yfinance
        yfinance.price('GOOG') # => '368.91'
    
* Get all available information about a stock:
    
        yfinance.get_all('GOOG') # => {...

* Keys for the resulting dictionary are:
    
        price
        change
        volume
        average_daily_volume
        exchange
        market_cap
        book_value
        ebitda
        dividend_per_share
        dividend_yield
        earnings_per_share
        i52_week_high
        i52_week_low
        i50_day_moving_average
        i200_day_moving_average
        price_to_earnings_ratio
        price_to_earnings_growth_ratio
        price_to_sales_ratio
        price_to_book_ratio
        short_ratio

* You can use these to grab just a few data points for a stock:
    
        yfinance.get('GOOG', yfinance.price & yfinance.volume) # => {...

* You can also call each of these as a function:
    
        yfinance.change('GOOG') # => '+2.10'
        yfinance.price_to_earnings_ratio('GOOG') # => '25.04'

