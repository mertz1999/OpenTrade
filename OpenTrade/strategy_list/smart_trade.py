from ..strategy import *
import matplotlib.pyplot as plt 


class SmartTrade(Strategy):
    def __init__(self, data, invesment, fee, name='Infinity_grids', method="VOLUME"):
        super().__init__(data, invesment * 0.9, fee, name, method)
        
        # Print some information to user
        print(" ----------  LOADING -----------")
        print("Total number of data : ", len(self.data))
        print('\n')


    def algo(self, *args, **kwargs):
        idx             = kwargs['idx']
        close_price     = kwargs['close_price']
           



            


    def result_info(self):

        # print("\n-------------------- Results --------------------")
        # print("Amount of opening volume : {:.2f}".format(self.trades.total_online_profit(self.last_price)))
        # print("Amount of Saved          : {:.2f}".format(self.saved))
        # print("APR                           : {:.2f}%".format((self.trades.total_profit()/self.invest_copy)*100))
        # print("Balance                       : {:.2f}".format(self.trades.invesment))
        # print("Total fees                    : {:.2f}".format(self.trades.fees))
        # print(len(self.trades.closed_positions))

        print("\nThanks to using ((Smart Trade))")

        # self.trades.log("\n-------------------- Results --------------------")
        # self.trades.log("Amount of opening volume : {:.2f}".format(self.trades.total_online_profit(self.last_price)))
        # self.trades.log("Amount of Saved          : {:.2f}".format(self.saved))




