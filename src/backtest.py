import pandas as pd 
import numpy as np
import os

class TradesStructure():
    def __init__(self, name='Temp_name') -> None:
        self.open_positions   = {} # index : [price, amount]
        self.closed_positions = {} # [open_index, open_price, close_idx, close_price]
        self.profits          = [] # In $
        self.future_close     = {} # index : f_close_price
        self.future_open      = {} # index: price, 

        path = "./inc/"+name+".txt"
        os.makedirs('./inc/', exist_ok=True)
        self.log_file = open(path, "w")


    
    def __str__(self) -> str:
        return "-------- New Structure has been made -------- \n"

    # Add new position
    def open(self, idx, price, amount):
        self.open_positions[idx] = [price, amount]
        out_data = "(OPEN) {:.2f}$ in price {:.2f} ({})".format(amount, price, idx)
        self.log(out_data)
        print(out_data)

    # Close a certain position
    def close(self, open_idx, close_idx, close_price):
        open_price, amount = self.open_positions[open_idx]
        self.open_positions.pop(open_idx)
        if open_idx in self.future_close:
            self.future_close.pop(open_idx)
        self.closed_positions[open_idx] = [open_idx, open_price, close_idx, close_price]
        result = ((close_price - open_price) / open_price) * amount
        self.profits.append(result)
        out_data = "(CLOSE) Order closed with {:.1f}$ change at price {:.2f} ({})".format(result, close_price, open_idx)
        self.log(out_data)
        print(out_data)

    # Close all
    def close_all(self, close_idx, close_price):
        keys = self.__key()
        for key in keys:
            self.close(key, close_idx, close_price)

    # Balance after backtest
    def total_profit(self):
        sum_profits = np.sum(self.profits)
        return sum_profits
    
    # Get total profit
    def total_online_profit(self, close_price):
        keys = self.__key()
        profits = 0
        for key in keys:
            open_price, amount = self.open_positions[key]
            profit = ((close_price - open_price) / open_price) * amount
            profits += profit 
        
        return profits

    # Get total Investments
    def total_investment(self):
        keys = self.__key()
        total = 0

        for key in keys:
            _, amount = self.open_positions[key]
            total += amount 
        
        return total

    # Log function
    def log(self,string, num_enter=1):
        self.log_file.write(string)
        for i in range(num_enter):
            self.log_file.write('\n')
    
    # Used to close or add future sell 
    def auto_close(self, Type, price=0.0, idx=0):
        # Add new Item to future close list
        if Type == "ADD":
            self.future_close[idx] = price

        # Check which position need to close
        elif Type == "CHECK":
            keys = self.future_close.copy().keys()
            for key in keys:
                if self.future_close[key] <= price:
                    self.close(key, idx, price)

        else:
            print("Type is not corect. Set right one")
            exit()
    
    # Used to open future by orded
    def auto_open(self, Type, idx, price=0.0, amount=0.0, sell_price=0.0):
        if Type == "ADD":
            self.future_open[idx] = [price, amount, sell_price]
        elif Type == "CHECK":
            keys = self.future_open.copy().keys() 
            for key in keys:
                if self.future_open[key][0] >= price:
                    self.open(idx, price, self.future_open[key][1])
                    self.auto_close("ADD", self.future_open[key][2], idx)
        else:
            print("Input Type fot auto_buy is incorrect")
            exit()
        


    
    # This function return a list of keys in open_position (indexes)
    def __key(self):
        return self.open_positions.copy().keys()








# balance = 500


trades = TradesStructure()

# trades.open(5, 100, 500)
# trades.auto_close("ADD", 150, 5)
# trades.auto_close("CHECK", 200, 40)
# trades.open(6, 110, 400)

# trades.auto_open("ADD", 5, 100, 10, 150)
# trades.auto_open("CHECK", 10, 80)
# trades.auto_close("CHECK", 160, 15)


# # print(trades.open_positions)

# # trades.close_all(7, 100)
# print(trades.total_profit(200))

# print(trades.open_positions)
# print(trades.closed_positions)


