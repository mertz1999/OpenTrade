import pandas as pd 
import numpy as np
import os


class TradesStructure():
    def __init__(self, invesment, fee, name='Temp_name') -> None:
        self.profits          = [] # In $
        self.future_close     = {} # index : f_close_price
        self.future_open      = {} # index: price, 
        self.open_flag        = False
        self.close_flag       = [False, 0.0, 0.0] # [FLAG, price, profit]
        self.invesment        = invesment
        self.fee              = fee / 100
        self.fees             = 0.0

        path = "./inc/"+name+".txt"
        os.makedirs('./inc/', exist_ok=True)
        self.log_file = open(path, "w")


    # Add new position
    def open(self, idx, price, amount):
        pass


    # Close all
    def close_all(self, close_idx, close_price):
        pass

    # Balance after backtest
    def total_profit(self):
        sum_profits = np.sum(self.profits)
        return sum_profits
    
    # Get total profit
    def total_online_profit(self, close_price):
        pass

    # Get total Investments
    def total_investment(self):
        pass

    # Log function
    def log(self,string, num_enter=1):
        self.log_file.write(string)
        for i in range(num_enter):
            self.log_file.write('\n')
    
    # Used to close or add future sell 
    def auto_close(self, Type, price=0.0, idx=0):
        pass
    
    # Used to open future by orded
    def auto_open(self, Type, idx, price=0.0, amount=0.0, sell_price=0.0):
        pass
        
    

# This Class is order based trading
class OrderBasedTrading(TradesStructure):
    def __init__(self, invesment, fee, name='Temp_name') -> None:
        super().__init__(invesment, fee, name)

        self.open_positions   = {} # index : [price, amount]
        self.closed_positions = {} # [open_index, open_price, close_idx, close_price]

    
    # Open a Position
    def open(self, idx, price, amount):
        amount_after_fee = amount - (self.fee * amount) 
        self.open_positions[idx] = [price, amount_after_fee]

        self.fees += (amount * self.fee)

        # Log
        out_data = "(OPEN) {:.2f}$ in price {:.2f} ({})".format(amount_after_fee, price, idx)
        self.invesment -= amount
        self.log(out_data)
        print(out_data)

        # Set Open flag
        self.open_flag = True

    # close an Order
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

        # Set close Flag
        self.invesment += (amount + result)
        self.close_flag = [True, close_price, result]
    
    # Close all opening orders
    def close_all(self, close_idx, close_price):
        keys = self.key()
        for key in keys:
            self.close(key, close_idx, close_price)
        return keys
    
    # Find total profit with all opening orders
    def total_online_profit(self, close_price):
        keys = self.key()
        profits = 0.0
        for key in keys:
            open_price, amount = self.open_positions[key]
            profit = ((close_price - open_price) / open_price) * amount
            profits += profit 
        
        return profits

    # Find total of Invertment for all opening irders
    def total_investment(self):
        keys = self.key()
        total = 0

        for key in keys:
            _, amount = self.open_positions[key]
            total += amount 
        
        return total

    # Set Auto close order function
    def auto_close(self, Type, price=0, idx=0):
        # Add new Item to future close list
        if Type == "ADD":
            self.future_close[idx] = price

        # Check which position need to close
        elif Type == "CHECK":
            keys = self.future_close.copy().keys()
            for key in keys:
                if self.future_close[key] <= price:
                    self.close(key, idx, price)
                    # self.future_close.pop(key)

        else:
            print("Type is not corect. Set right one")
            exit()

    # Set Auto open function
    def auto_open(self, Type, idx, price=0, amount=0, sell_price=0):
        if Type == "ADD":
            self.future_open[idx] = [price, amount, sell_price]
        elif Type == "CHECK":
            keys = self.future_open.copy().keys() 
            for key in keys:
                if self.future_open[key][0] >= price:
                    self.open(idx, price, self.future_open[key][1])
                    self.auto_close("ADD", self.future_open[key][2], idx)
                    self.future_open.pop(key)
        else:
            print("Input Type fot auto_buy is incorrect")
            exit()

     


    # This function return a list of keys in open_position (indexes)
    def key(self):
        return self.open_positions.copy().keys()



class VolumeBasedTrading(TradesStructure):
    def __init__(self, invesment, fee, name='Temp_name') -> None:
        super().__init__(invesment, fee, name)

        self.open_volume = 0.0
        self.closed_positions = {} # {close_idx, close_price, amount}

    # Buy funtion
    def open(self, idx, price, amount):
        amount_after_fee = amount-(self.fee * amount)
        vol = (amount_after_fee) / price
        self.open_volume += vol
        self.fees += (amount * self.fee)

        # Log
        out_data = "(OPEN)  {:.2f}$ in price {:.2f} ({})".format(amount_after_fee, price, idx)
        print(out_data)
        self.log(out_data)

        self.invesment -= amount
        self.open_flag = True

    # sell fnuction
    def sell(self, close_idx, close_price, amount):
        vol = amount / close_price
        self.open_volume -= vol 

        out_data = "(CLOSE) {:.2f}$ sell at price {:.2f} ({})".format(amount, close_price, close_idx)
        print(out_data)
        self.log(out_data)

        self.invesment += amount
        self.close_flag = [True, close_price, amount]

    # Sell all thing
    def close_all(self, close_idx, close_price):
        amount = close_price * self.open_volume
        temp = self.open_volume
        self.open_volume = 0.0

        self.invesment += amount

        out_data = "(CLOSE) {:.2f} sell at price {:.2f} ({})".format(amount, close_price, close_idx)
        print(out_data)
        self.log(out_data)
    
    # Find total profit of all volume
    def total_online_profit(self, close_price):
        return self.open_volume * close_price 


    





# balance = 500


# trades = VolumeBasedTrading(500, 0.1, )

# trades.open(5, 100, 500)
# print(trades.open_volume)
# trades.close_all(10, 120)
# print(trades.invesment)
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


