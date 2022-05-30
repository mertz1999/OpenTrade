from ..strategy import *
import matplotlib.pyplot as plt 


class SmartTrade(Strategy):
    def __init__(self,buy_price, trailing_percent, stop_loss, trigger_price, data, invesment, fee, name='SmartTrade', method="VOLUME"):
        super().__init__(data, invesment, fee, name, method)
        
        self.buy_price        = buy_price
        self.trailing_percent = trailing_percent
        self.stop_loss        = stop_loss
        self.trigger_price    = trigger_price

        # Print some information to user
        print(" ----------  LOADING -----------")
        print("Total number of data : ", len(self.data))
        print('\n')

        self.flag = False
        self.below = False


    def algo(self, *args, **kwargs):
        idx             = kwargs['idx']
        close_price     = kwargs['close_price']
        date            = kwargs['date']
        
        # Check price is below buy_price
        if self.trades.open_volume == 0 and self.flag == False:
            print("LOOK", close_price)
            if close_price <= self.buy_price:
                self.below = True
            
            self.flag = True
        
        # Wait for reaching buy price 
        if self.flag == True:
            if self.below == True:
                if close_price >= self.buy_price:
                    print('({})'.format(date), end=" ")
                    self.trades.open(idx, close_price, self.trades.invesment) 
                    self.flag = False
            else:
                if close_price <= self.buy_price:
                    print('({})'.format(date), end=" ")
                    self.trades.open(idx, close_price, self.trades.invesment) 
                    self.flag = False

        # Check Price for stoploss and trigger price
        if self.trades.open_volume != 0 and self.flag == False:
            # Check StopLoss
            if close_price <= self.stop_loss:
                print('({})'.format(date), end=" ")
                self.trades.close_all(idx, close_price)
                self.end = True
            # Check Trigger price
            elif close_price >= self.trigger_price:
                self.stop_loss = self.trigger_price - self.trigger_price*self.trailing_percent/100
                self.trigger_price = close_price


            


            


    def result_info(self):

        print("\n-------------------- Results --------------------")
        print("Investment   : {:.2f}".format(self.trades.invesment))

        print("\nThanks to using ((Smart Trade))")

        self.trades.log("\n-------------------- Results --------------------")
        self.trades.log("Investment   : {:.2f}".format(self.trades.invesment))

