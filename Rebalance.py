from OpenTrade.strategy_list.rebalance import Rebalance
import pandas as pd

# Loading BTC data in 2019
BTC_data = pd.read_csv('./data/BTC_2018.csv')
BTC_data = pd.DataFrame(BTC_data.values[::-1], BTC_data.index, BTC_data.columns)

BTC_data['date'] = pd.to_datetime(BTC_data['date'])


# Loading ETH data from 2016 to 2021 and select 2019
ETH_data = pd.read_csv('./data/ETH.csv')
ETH_data = pd.DataFrame(ETH_data.values[::-1], ETH_data.index, ETH_data.columns)

ETH_data['date'] = pd.to_datetime(ETH_data['date'])

start_date = '2018-01-01'
end_date = '2018-12-30'

mask = (ETH_data['date'] > start_date) & (ETH_data['date'] <= end_date)
ETH_data = ETH_data.loc[mask]
ETH_data.index = range(0,len(ETH_data))


print(len(BTC_data), len(ETH_data))


fee = 0.1
investment = 500

max_profit = 100
num_transactions = 1000

st = Rebalance(10, max_profit,[ETH_data, BTC_data],investment, fee, name="Grid-Trading", method="VOLUME")