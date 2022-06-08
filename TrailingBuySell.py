from OpenTrade.strategy_list.trailing_buy_sell import TrailingBuySell
import pandas as pd

data = pd.read_csv('./data/BTC_2021.csv')
data = pd.DataFrame(data.values[::-1], data.index, data.columns)


# Grid Trading parameters
investment         = 600
fee                = 0.1        # In percent


st = TrailingBuySell(data,investment, fee, name="TrailingBuySell", method="VOLUME")
# st.run()
