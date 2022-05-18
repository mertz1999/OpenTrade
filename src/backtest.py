import pandas as pd 
import numpy as np


class TradesStructure():
    def __init__(self) -> None:
        self.open_positions   = {}
        self.closed_positions = {} # [open_index, , open_price, close_idx, close_price]
        self.profits          = []
    
    def __str__(self) -> str:
        return "-------- New Structure has been made -------- \n"

    # Add new position
    def open(self, idx, price, amount):
        self.open_positions[idx] = [price, amount]
        print("(OPEN) {:.2f}$ in price ({:.2f})".format(amount, price, idx))

    # Close a certain position
    def close(self, open_idx, close_idx, close_price):
        open_price, amount = self.open_positions[open_idx]
        self.open_positions.pop(open_idx)
        self.closed_positions[open_idx] = [open_idx, open_price, close_idx, close_price]
        result = ((close_price - open_price) / open_price) * amount
        self.profits.append(result)
        print("(CLOSE) Order closed with {:.1f}$ change. ({})".format(result, open_idx))

    # Close all
    def close_all(self, close_idx, close_price):
        keys = self.open_positions.copy().keys()
        for key in keys:
            self.close(key, close_idx, close_price)

    # Balance after backtest
    def total_profit(self):
        sum_profits = np.sum(self.profits)
        return sum_profits
    
    # Get total profit
    def total_online_profit(self, close_price):
        keys = self.open_positions.copy().keys()
        profits = 0
        for key in keys:
            open_price, amount = self.open_positions[key]
            profit = ((close_price - open_price) / open_price) * amount
            profits += profit 
        
        return profits

    # Get total Investments
    def total_investment(self):
        keys = self.open_positions.copy().keys()
        total = 0

        for key in keys:
            _, amount = self.open_positions[key]
            total += amount 
        
        return total


class log(TradesStructure):
    def print_t(self):
        print("LOOK AT HERE")




# balance = 500


# trades = TradesStructure()

# trades.open(5, 100, 500)
# trades.open(6, 110, 400)

# # print(trades.open_positions)

# # trades.close_all(7, 100)
# print(trades.total_profit(200))

# print(trades.open_positions)
# print(trades.closed_positions)


