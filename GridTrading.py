from OpenTrade.strategy_list.grid_trading import GridTrading
# import OpenTrade
import pandas as pd

data = pd.read_csv('./data/BTC_2020.csv')
data = pd.DataFrame(data.values[::-1], data.index, data.columns)

st = GridTrading(100000, 10000, 500, 0.1,data, 600, name="Grid-Trading")
st.run()
