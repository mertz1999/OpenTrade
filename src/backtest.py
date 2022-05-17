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
        print("New Order: ({}) in price: {}".format(idx, price))

    # Close a certain position
    def close(self, open_idx, close_idx, close_price):
        open_price, amount = self.open_positions[open_idx]
        self.open_positions.pop(open_idx)
        self.closed_positions[open_idx] = [open_idx, open_price, close_idx, close_price]
        result = ((close_price - open_price) / open_price) * amount
        self.profits.append(result)
        print("Order ({}) closed with {:.1f}$ change".format(open_idx, result))

    # Close all
    def close_all(self, close_idx, close_price):
        keys = self.open_positions.copy().keys()
        for key in keys:
            self.close(key, close_idx, close_price)

    # Balance after backtest
    def make_balance(self, balance):
        sum_profits = np.sum(self.profits)
        return sum_profits
