from ..strategy import *
import matplotlib.pyplot as plt 


class InfinityGrids(Strategy):
    def __init__(self, lowest_price, PPG, data, invesment, fee, name='Infinity_grids', method="VOLUME"):
        super().__init__(data, invesment * 0.9, fee, name, method)

        self.lowest_price = lowest_price
        self.PPG          = PPG
        self.saved        = 0.1 * invesment
        self.saved_list   = []
        self.price_list   = []
        self.inv_list     = []
        self.invest       = 0.9 * invesment
        self.base_price   = 0.0
        self.last_price   = 0.0
        
        # Print some information to user
        print(" ----------  LOADING -----------")
        print("Total number of data : ", len(self.data))
        print("Profit-Per-Grid      : ", PPG)
        print('\n')


    def algo(self, *args, **kwargs):
        idx             = kwargs['idx']
        close_price     = kwargs['close_price']
        date            = kwargs['date']
        self.last_price = close_price

        self.saved_list.append(self.saved)
        self.inv_list.append(self.trades.total_online_profit(close_price))
        if idx < 30000:
            self.price_list.append(close_price)

        # Buy when bot is running
        if self.trades.open_volume == 0:
            self.trades.log("({}) ".format(date), 0)
            self.trades.open(idx, close_price, self.invest)
            self.base_price = close_price

        # Check for price changing
        changing_rate = ((close_price - self.base_price) / self.base_price) * 100
        
        # If price changing rate become higher than PPG value
        if changing_rate > self.PPG:
            # find different
            diff = self.trades.total_online_profit(close_price) - self.invest
            # sell surplus
            self.trades.log("({}) ".format(date), 0)
            self.trades.sell(idx, close_price, diff)
            # change saved value
            self.saved += diff
            # Update base price
            self.base_price = close_price


        # If price changing rate become lower than PPG value
        elif (changing_rate < -1 * self.PPG) and not (self.saved < (self.invest * self.PPG/100)) and (close_price > self.lowest_price):
            # find different
            diff = self.invest - self.trades.total_online_profit(close_price)
            # Buy surplus
            self.trades.log("({}) ".format(date), 0)
            self.trades.open(idx, close_price, diff)
            # Change saved value
            self.saved -= diff 
            # Update base price 
            self.base_price = close_price


        else:
            pass

        



            


    def result_info(self):
        plt.plot(self.saved_list)
        plt.title("Saved values")
        plt.show()

        print("\n-------------------- Results --------------------")
        print("Amount of opening volume : {:.2f}".format(self.trades.total_online_profit(self.last_price)))
        print("Amount of Saved          : {:.2f}".format(self.saved))
        # print("APR                           : {:.2f}%".format((self.trades.total_profit()/self.invest_copy)*100))
        # print("Balance                       : {:.2f}".format(self.trades.invesment))
        # print("Total fees                    : {:.2f}".format(self.trades.fees))
        # print(len(self.trades.closed_positions))

        print("\nThanks to using ((Infinity Grids))")

        self.trades.log("\n-------------------- Results --------------------")
        self.trades.log("Amount of opening volume : {:.2f}".format(self.trades.total_online_profit(self.last_price)))
        self.trades.log("Amount of Saved          : {:.2f}".format(self.saved))




