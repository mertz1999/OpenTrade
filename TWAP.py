from OpenTrade.strategy_list.twap import TWAP
import pandas as pd

# Loading data
data = pd.read_csv('./data/BTC_2020.csv')
data = pd.DataFrame(data.values[::-1], data.index, data.columns)

# parameters
fee          = 0.1     # fee value for open buy order
investment   = 500     # total investment -> for 'buy' in $, for 'sell' in crypto amount
buy_sell     = "buy"   # buy or sell, You can`t use sell method in backtest
often        = "5m"    # You can choose: 10s 30s 1m 5m (Note: You can use 1m and 5m)
transactions = 100   # number of total order

# running strategy
st = TWAP(buy_sell, often, transactions, data, investment, fee, name='TWAP' ,method="VOLUME")
st.run()

