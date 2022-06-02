from OpenTrade.strategy_list.spot_future import SpotFuture
import pandas as pd


# Preparing TEST data
data = pd.read_csv('./data/BTC_2021.csv')
data = pd.DataFrame(data.values[::-1], data.index, data.columns)

data['date'] = pd.to_datetime(data['date'])

# Loading Funding rate data 
f_rate = pd.read_csv('./data/funding-rate.csv')
f_rate['date'] = pd.to_datetime(f_rate['date'])



fee              = 0.1
investment       = 10000


st = SpotFuture(f_rate, data, investment, fee, name="Spot_Future", method="ORDER-FUTURE")
# st.run()