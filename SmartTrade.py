from OpenTrade.strategy_list.smart_trade import SmartTrade
import pandas as pd

# Preparing TEST data
data = pd.read_csv('./data/BTC_2021.csv')
data = pd.DataFrame(data.values[::-1], data.index, data.columns)

data['date'] = pd.to_datetime(data['date'])

start_date = '2021-01-06 10:00:00'
end_date   = '2021-01-09'

mask = (data['date'] > start_date) & (data['date'] <= end_date)
data = data.loc[mask]
data.index = range(0,len(data))

fee              = 0.1
investment       = 500
buy_price        = 35900
trailing_percent = 5   # In percent
stop_loss        = 34500
trigger_price    = 37100

st = SmartTrade(buy_price, trailing_percent, stop_loss, trigger_price,data, investment, fee, name="SmartTrade", method="VOLUME")
st.run()