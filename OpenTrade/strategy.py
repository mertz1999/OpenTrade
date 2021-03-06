import pandas as pd 
import numpy as np
from .backtest import *

# Define Strategy Parent Class
class Strategy():
    def __init__(self,data, invesment, fee,name='Martingale', method="ORDER"):
        self.name = name
        self.data = data
        self.params = self.get_params()
        self.method = method
        if method == "ORDER":
            self.trades = OrderBasedTrading(invesment, fee,name=self.name)
        elif method == "VOLUME":
            self.trades = VolumeBasedTrading(invesment, fee,name=self.name)
            self.open_list = []
            self.close_list = [[0,0.0]]
        elif method == "ORDER-FUTURE":
            self.trades = OrderBasedFutureTrading(invesment, fee, name=self.name)

        self.end = False

    def run(self):
        for idx in range(len(self.data)):
            if self.end == True:
                break
            
            self.trades.open_flag     = False
            self.trades.close_flag[0] = False

            date        = self.data['date'][idx]
            open_price  = self.data['open'][idx]
            high_price  = self.data['high'][idx]
            low_price   = self.data['low'][idx]
            close_price = self.data['close'][idx]

            if self.method == "ORDER-FUTURE":
                self.trades.auto_close("CHECK", close_price, idx)
                self.trades.auto_open("CHECK", idx, close_price, 0.0, close_price, close_price)
            else:
                self.trades.auto_close("CHECK", close_price, idx)
                self.trades.auto_open("CHECK", idx, close_price)

            self.algo(idx=idx, date=date, open_price=open_price, high_price=high_price, low_price=low_price, close_price=close_price)
        

        # print(self.trades.future_close)

        self.result_info()
        self.trades.log_file.close()

    def get_params(self):
        pass
    
    def algo(self, idx, date, open_price, high_price, low_price, close_price):
        pass

    def result_info(self):
        pass

    def print_date(date):
        print("({})".format(date), end=" ")


  