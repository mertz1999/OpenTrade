from OpenTrade.strategy_list.grid_trading import GridTrading
# import OpenTrade
import pandas as pd

data = pd.read_csv('./data/BTC_2020.csv')
data = pd.DataFrame(data.values[::-1], data.index, data.columns)


# Grid Trading parameters
High_price         = 100000
Low_price          = 10000
num_grids          = 500 
per_order          = 0.1
investment         = 600
fee                = 1        # In percent
max_open_positions = 8


st = GridTrading(High_price , Low_price, num_grids, per_order, max_open_positions,data,investment, fee, name="Grid-Trading")
st.run()
