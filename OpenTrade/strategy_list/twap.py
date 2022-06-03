from ..strategy import *

class TWAP(Strategy):
    def __init__(self, buy_sell, often, transactions, data,invesment, fee,name='TWAP', method="VOLUME"):
        super().__init__(data,invesment, fee, name, method)
        
        # Input parameters
        self.buy_sell         = buy_sell
        self.often            = often
        self.transactions     = transactions
        self.invest_per_order = invesment / transactions

        # Inside parameters
        self.start = False # Start flag
        self.time  = 0     # In minutes
        self.timeframe = {
            '1m': 1,
            '5m': 5,
            }
        

        # Print some information to user
        print(" ----------  LOADING -----------")
        print("Total number of data: ", len(self.data))
        print('\n')
    
    def algo(self, *args, **kwargs):
        idx         = kwargs['idx']
        close_price = kwargs['close_price']
        date        = kwargs['date']

        # Check for starting projects
        if self.start == False:
            if self.buy_sell == 'buy':
                Strategy.print_date(date)
                self.trades.log("({}) ".format(date), 0)
                self.trades.open(idx, close_price, self.invest_per_order)

            elif self.buy_sell == 'sell':
                Strategy.print_date(date)
                self.trades.log("({}) ".format(date), 0)
                self.trades.sell(idx, close_price, self.invest_per_order)
            self.start = True

        else:
            self.time += 1
            if self.time == self.timeframe[self.often]:
                self.time = 0
                self.transactions -= 1
                if self.buy_sell == 'buy':
                    Strategy.print_date(date)
                    self.trades.log("({}) ".format(date), 0)
                    self.trades.open(idx, close_price, self.invest_per_order)
                elif self.buy_sell == 'sell':
                    Strategy.print_date(date)
                    self.trades.log("({}) ".format(date), 0)
                    self.trades.sell(idx, close_price, self.invest_per_order)


        # Check for number of transactions
        if self.transactions == 0:
            self.end = True

        



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