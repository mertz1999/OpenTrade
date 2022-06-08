from ..strategy import *

class TrailingBuySell(Strategy):
    def __init__(self, data, invesment, fee, name='TrailingBuySell', method="VOLUME"):
        super().__init__(data, invesment, fee, name, method)

        
        # Print some information to user
        print(" ----------  LOADING -----------")
        print("Total number of data : ", len(self.data))
        print('\n')


    def algo(self, *args, **kwargs):
        idx         = kwargs['idx']
        close_price = kwargs['close_price']
        date        = kwargs['date']

           


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

