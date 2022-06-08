from OpenTrade.strategy_list.trailing_buy_sell import TrailingBuySell
import pandas as pd

data = pd.read_csv('./data/BTC_2020.csv')
data = pd.DataFrame(data.values[::-1], data.index, data.columns)

"""
    If Trigger price being Higher than now close price Trailing Sell will be start and 
    If Trigger price being Lower than now close price Trailing buy will be start.

"""

# Grid Trading parameters
investment         = 600
fee                = 0.1        # In percent
trigger_price      = 7076       # 
trailing_percent   = 3          # In percent
amount             = 100        # In Buy method: $, In sell method: number of coins


st = TrailingBuySell(trigger_price, trailing_percent, amount, data,investment, fee, name="TrailingBuySell", method="VOLUME")
st.run()



