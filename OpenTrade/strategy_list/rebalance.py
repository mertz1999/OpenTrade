from ..strategy import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class OneSideRebalancing(Strategy):
    def __init__(self, data, invesment, fee, name='Martingale', method="VOLUME"):
        super().__init__(data, invesment, fee, name, method)
        
        self.index = 0
        self.start = False
        
        
        # Print some information to user
        print(" ----------  LOADING -----------")
        print("Total number of data : ", len(self.data))
        print('\n')

    def run(self):
        pass
        # date        = self.data['date'][self.index]
        # open_price  = self.data['open'][self.index]
        # high_price  = self.data['high'][self.index]
        # low_price   = self.data['low'][self.index]
        # close_price = self.data['close'][self.index]

        # self.algo(idx=self.index, date=date, open_price=open_price, high_price=high_price, low_price=low_price, close_price=close_price)
          

    def algo(self, *args, **kwargs):
        pass
    #     idx         = kwargs['idx']
    #     close_price = kwargs['close_price']   

    #     if self.start == False:
    #         self.trades.open(idx, close_price, self.trades.invesment)
    #         self.start = True
    #     else:
    #         self.check_balance()

    
    def result_info(self):
        pass

class Rebalance():
    def __init__(self, data, invesment, fee, name='temp', method='VOLUME'):
        self.data = data
        self.first_side = OneSideRebalancing(data[0], invesment/2, fee, name='First_Side', method=method) #BTC
        self.secou_side = OneSideRebalancing(data[1], invesment/2, fee, name='Secound_Side', method=method) #ETH

        self.total_profit_value = 0.0


        for idx in range(len(data[1])):
            # Every 5 Minute
            if idx % 10 == 0:
                # Find close_prices
                date = self.data[1]['date'][idx]
                close_price_secou = self.data[1]['close'][idx]
                
                if len(self.data[0][self.data[0]['date'] == date]) > 0:
                    close_price_first = self.data[0][self.data[0]['date'] == date].iloc[0].close
                else:
                    continue
                    
                

                # Check for Take profit
                self.total_profit_value = (self.first_side.trades.total_online_profit(close_price_first) + self.secou_side.trades.total_online_profit(close_price_secou))
                print("Total Value: ", self.total_profit_value)
                if  self.total_profit_value > 600:
                    self.first_side.trades.close_all(idx, close_price_first)
                    self.secou_side.trades.close_all(idx, close_price_secou)
                    break

                # For First one that bot is started
                if self.first_side.start == False:
                    self.first_side.start = True
                    self.first_side.trades.open(idx, close_price_first, self.first_side.trades.invesment)
                    self.secou_side.trades.open(idx, close_price_secou, self.secou_side.trades.invesment)

                    continue
            
                # check for loss of balance
                profit_first = self.first_side.trades.total_online_profit(close_price_first)
                profit_secou = self.secou_side.trades.total_online_profit(close_price_secou)
    
                if abs(profit_first - profit_secou) > 1:
                    if profit_first > profit_secou:
                        print()
                        print(date)
                        print("(BTC) ", end="")
                        self.first_side.trades.sell(idx, close_price_first, abs(profit_first - profit_secou)/2)
                        print("(ETH) ", end="")
                        self.secou_side.trades.open(idx, close_price_secou, abs(profit_first - profit_secou)/2)
                        print()
                    else:
                        print()
                        print(date)
                        print("(ETH) ", end="")
                        self.secou_side.trades.sell(idx, close_price_secou, abs(profit_first - profit_secou)/2)
                        print("(BTC) ", end="")
                        self.first_side.trades.open(idx, close_price_first, abs(profit_first - profit_secou)/2)
                        print()
                        

        print("\n ---------- Result -----------")
        print("Total value after bot: ", self.total_profit_value)

    






