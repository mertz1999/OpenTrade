from OpenTrade.strategy_list.twap import TWAP
import pandas as pd

# Loading data
data = pd.read_csv('./data/BTC_2020.csv')
data = pd.DataFrame(data.values[::-1], data.index, data.columns)

st = TWAP( data, 700, 1)
# st.run()
