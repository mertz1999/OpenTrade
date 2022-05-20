from OpenTrade.strategy_list.grid_trading import GridTrading
# import OpenTrade
import pandas as pd

data = pd.read_csv('./data/BTC_2020_edited.csv')
data = pd.DataFrame(data.values[::-1], data.index, data.columns)

st = GridTrading(100000, 10000, 400, 600, data, name="Grid-Trading")
st.run()
