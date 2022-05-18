import pandas as pd 
import numpy as np
from src.backtest import *

data = pd.read_csv('./src/BTC_2020.csv')

data = pd.DataFrame(data.values[::-1], data.index, data.columns)
# print(data)


# Martingle parameters
take_profit = 1    # In percent
price_scale = -1   # In Percent
safety_orders = 3 # We devide Invetment in 2^safety_orders parts
invesment   = 700 # In $


share = invesment // (2 ** safety_orders)
Invertment_parts = [share]

for i in range(safety_orders):
    Invertment_parts.append(2**i * share)


# Print some information to user
print(" ----------  LOADING -----------")
print("Total number of data: ", len(data))
print("Take profit: {}%".format(take_profit))
print("Price scale: {}%".format(price_scale))
print('\n')

trades = TradesStructure(name='Martingale')
min_lose = 0.0
for idx in range(len(data)):
    close_price = data['close'][idx]

    # Check for zero position opening 
    if len(trades.open_positions) == 0:
        print("-------------  Round Started {}-------------- \n".format(data['date'][idx]))
        trades.open(idx, close_price, Invertment_parts[0])
    
    else:
        # Check total profit
        total_online_profits = trades.total_online_profit(close_price)
        total_online_investment = trades.total_investment()
        profit_in_percent = ((total_online_profits - total_online_investment) / total_online_investment) * 100
        # Check min profit
        if profit_in_percent < min_lose:
            min_lose = profit_in_percent
        # Check take_profit threshold
        if profit_in_percent >= take_profit:
            trades.close_all(idx, close_price)
            print("\n")
            # break
        else:
            if len(trades.open_positions) < 4:
                last_position = trades.open_positions[max(trades.open_positions.copy().keys())]
                online_last_profit = ((close_price - last_position[0]) / last_position[0]) * 100
                if online_last_profit <= price_scale:
                    trades.open(idx, close_price, Invertment_parts[len(trades.open_positions)])
                

        


print("\n-------------------- Results --------------------")
print("Total profit in this strategy: {:.2f}".format(trades.total_profit()))
print("APR                          : {:.2f}%".format((trades.total_profit()/invesment)*100))
print("Biggest drawdown             : {:.2f}".format(min_lose))

print("\nThanks to using ((Martingale))")


trades.log("", 3)
trades.log("Total profit in this strategy: {:.2f}".format(trades.total_profit()))
trades.log("APR                          : {:.2f}%".format((trades.total_profit()/invesment)*100))
trades.log("Biggest drawdown             : {:.2f}".format(min_lose))

