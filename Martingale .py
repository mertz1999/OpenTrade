from OpenTrade import Martingale
import pandas as pd

data = pd.read_csv('./data/BTC_2020.csv')
data = pd.DataFrame(data.values[::-1], data.index, data.columns)

st = Martingale(1, -1, 3, data, 700)
st.run()
