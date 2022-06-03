from ..strategy import *

class TWAP(Strategy):
    def __init__(self, data,invesment, fee,name='Martingale', method="ORDER"):
        super().__init__(data,invesment, fee, name, method)
        
        
        # Print some information to user
        print(" ----------  LOADING -----------")
        print("Total number of data: ", len(self.data))
        print('\n')
    
    def algo(self, *args, **kwargs):
        idx         = kwargs['idx']
        close_price = kwargs['close_price']
        date        = kwargs['date']


    def result_info(self):
        pass
        # print("\n-------------------- Results --------------------")
        # print("Total profit in this strategy : {:.2f}".format(self.trades.total_profit()))
        # print("APR                           : {:.2f}%".format((self.trades.total_profit()/self.trades.invesment)*100))
        # print("Biggest drawdown              : {:.2f}%".format(self.min_lose))
        # print("Total number of Rounds        : {}".format(self.num_rounds))
        # print("\nThanks to using ((Martingale))")

        # self.trades.log("", 2)
        # self.trades.log("Total profit in this strategy : {:.2f}".format(self.trades.total_profit()))
        # self.trades.log("APR                           : {:.2f}%".format((self.trades.total_profit()/self.trades.invesment)*100))
        # self.trades.log("Biggest drawdown              : {:.2f}%".format(self.min_lose))
        # self.trades.log("Total number of Rounds        : {}".format(self.num_rounds))