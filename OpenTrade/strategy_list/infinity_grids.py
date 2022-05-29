from ..strategy import *

class InfinityGrids(Strategy):
    def __init__(self, lowest_price, PPG, data, invesment, fee, name='Infinity_grids', method="VOLUME"):
        super().__init__(data, invesment * 0.9, fee, name, method)

        self.lowest_price = lowest_price
        self.PPG          = PPG
        self.saved        = 0.1 * invesment
        self.invest       = 0.9 * invesment
        
        # Print some information to user
        print(" ----------  LOADING -----------")
        print("Total number of data : ", len(self.data))
        print("Profit-Per-Grid      : ", PPG)
        print('\n')


    def algo(self, *args, **kwargs):
        idx         = kwargs['idx']
        close_price = kwargs['close_price']

        # Buy when bot is running
        if self.trades.open_volume == 0:
            self.trades.open(idx, close_price, self.invest)
            


            


    def result_info(self):
        pass
        # print("\n-------------------- Results --------------------")
        # print("Total profit in this strategy : {:.2f}".format(self.trades.total_profit()))
        # print("APR                           : {:.2f}%".format((self.trades.total_profit()/self.invest_copy)*100))
        # print("Balance                       : {:.2f}".format(self.trades.invesment))
        # print("Total fees                    : {:.2f}".format(self.trades.fees))
        # print(len(self.trades.closed_positions))

        # print("\nThanks to using ((Grid trading))")

        # self.trades.log("\n-------------------- Results --------------------")
        # self.trades.log("Total profit in this strategy : {:.2f}".format(self.trades.total_profit()))
        # self.trades.log("APR                           : {:.2f}%".format((self.trades.total_profit()/self.invest_copy)*100))




