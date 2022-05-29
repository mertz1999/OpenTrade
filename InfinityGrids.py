from OpenTrade.strategy_list.infinity_grids import InfinityGrids 
import pandas as pd 


# Preparing TEST data
data = pd.read_csv('./data/BTC_2018.csv')
data = pd.DataFrame(data.values[::-1], data.index, data.columns)

data['date'] = pd.to_datetime(data['date'])
data['symbol']  = 'BTC'

fee = 0.1
investment   = 500
lowest_price = 1000
PPG          = 1  # In % (Profit-Per-Grid)


st = InfinityGrids(lowest_price, PPG, data, investment, fee, name="Infinity_grids", method="VOLUME")
st.run()


