import pandas as pd 
import numpy as np
from .backtest import *
from .plot_with_marker import plot

# Define Strategy Parent Class
class Strategy():
    def __init__(self,data, invesment, fee,name='Martingale', method="ORDER"):
        self.name = name
        self.data = data
        self.params = self.get_params()
        if method == "ORDER":
            self.trades = OrderBasedTrading(invesment, fee,name=self.name)
        elif method == "VOLUME":
            self.trades = VolumeBasedTrading(invesment, fee,name=self.name)
            self.open_list = []
            self.close_list = [[0,0.0]]

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

            self.trades.auto_close("CHECK", close_price, idx)
            self.trades.auto_open("CHECK", idx, close_price)

            self.algo(idx=idx, date=date, open_price=open_price, high_price=high_price, low_price=low_price, close_price=close_price)

            #  Check fot flag and plotting
            # if self.trades.open_flag:
            #     self.open_list.append([idx, low_price])
            
            # if self.trades.close_flag[0]:
            #     self.close_list.append([idx, high_price])

            # if self.trades.open_flag or self.trades.close_flag[0]:
            #     low_index_open  = -10 if len(self.open_list) >= 10 else 0
            #     low_index_close = -10 if len(self.close_list) >= 10 else 0

            #     temp_idx_low = self.open_list[low_index_open][0] if self.open_list[low_index_open][0] < self.close_list[low_index_close][0] else self.close_list[low_index_close][0]
            #     temp_idx_high = self.open_list[-1][0] if self.open_list[-1][0] > self.close_list[-1][0] else self.close_list[-1][0]
               
            #     temp_data = self.data[temp_idx_low-10 if temp_idx_low > 10 else 0: temp_idx_high+20]
            #     plot(self.open_list[-10:], self.close_list[-10:], temp_data)
        
        self.result_info()
        self.trades.log_file.close()

    def get_params(self):
        pass
    
    def algo(self, idx, date, open_price, high_price, low_price, close_price):
        pass

    def result_info(self):
        pass

  