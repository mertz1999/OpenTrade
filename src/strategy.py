import pandas as pd 
import numpy as np
from .backtest import *

# Define Strategy Parent Class
class Strategy():
    def __init__(self,data,name='Martingale'):
        self.name = name
        self.data = data
        self.params = self.get_params()
        self.trades = TradesStructure(name=self.name)
    
    def run(self):
        for idx in range(len(self.data)):
            date        = self.data['date'][idx]
            open_price  = self.data['open'][idx]
            high_price  = self.data['high'][idx]
            low_price   = self.data['low'][idx]
            close_price = self.data['close'][idx]

            self.algo(idx=idx, date=date, open_price=open_price, high_price=high_price, low_price=low_price, close_price=close_price)

        self.result_info()

    def get_params(self):
        pass
    
    def algo(self, idx, date, open_price, high_price, low_price, close_price):
        pass

    def result_info(self):
        pass

        