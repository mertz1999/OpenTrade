from ..strategy import *
import matplotlib.pyplot as plt 



class OneSideSF(Strategy):  # One Side of SpotFuture
    def __init__(self, data, invesment, fee, name='Martingale', method="VOLUME"):
        super().__init__(data, invesment, fee, name, method)
                
    def run(self):
        pass
          
    def algo(self, *args, **kwargs):
        pass
    
    def result_info(self):
        pass






class SpotFuture():
    def __init__(self, f_rate, data, invesment, fee, name='SpotFuture', method="ORDER-FUTURE"):
        
        self.data = data
        self.spot_side   = OneSideSF(data, invesment/2, fee, name="Spot_Side_SP", method="ORDER")
        self.future_side = OneSideSF(data, invesment/2, fee, name="Future_Side_SP", method="ORDER-FUTURE")

        self.f_rate  = f_rate
        self.fr_date = list(self.f_rate['date'])
        self.start   = False
        self.total_fund = 0.0
        self.total_fund_list = []

        # Print some information to user
        print(" ----------  LOADING -----------")
        print("Total number of data : ", len(self.spot_side.data))
        print('\n')

        fund = 0.0

        # Iterate on data 
        for idx in range(len(self.data)):

            date        = self.data['date'][idx]
            open_price  = self.data['open'][idx]
            high_price  = self.data['high'][idx]
            low_price   = self.data['low'][idx]
            close_price = self.data['close'][idx]

            # Start strategy by open position in spot market and sell position in future market
            if self.start == False:
                self.start = True
                Strategy.print_date(date)
                self.spot_side.trades.open(idx, close_price, self.spot_side.trades.invesment)
                Strategy.print_date(date)
                self.future_side.trades.open(idx, close_price, self.future_side.trades.invesment, type='sell')

            else:
                # Find Profits until now (date)
                future_profit = self.future_side.trades.total_online_profit(close_price) + self.future_side.trades.total_investment()
                spot_profit   = self.spot_side.trades.total_online_profit(close_price) + self.future_side.trades.total_investment()

                # Check for being Zero profit or low profit
                if future_profit < 10 or spot_profit < 10:
                    print("============= END OF BOT AND START AGAIN ==============")
                    print("Total fund in this round: {:.2f}\n".format(self.total_fund))

                    # Save Total fund
                    self.total_fund_list.append(self.total_fund)

                    # Close all open positions
                    self.spot_side.trades.close_all(idx, close_price)
                    self.future_side.trades.close_all(idx, close_price)

                    # New Investment value
                    invest = self.spot_side.trades.invesment + self.future_side.trades.invesment
                    self.total_fund = 0.0
                    self.spot_side.trades.invesment = invest / 2
                    self.future_side.trades.invesment = invest / 2

                    # Open New positions
                    Strategy.print_date(date)
                    self.spot_side.trades.open(idx, close_price, self.spot_side.trades.invesment)
                    Strategy.print_date(date)
                    self.future_side.trades.open(idx, close_price, self.future_side.trades.invesment, type='sell')
                    
                    continue


                if date in self.fr_date:
                                        
                    fund = future_profit * self.f_rate[self.f_rate['date'] == date].iloc[0].rate
                    self.total_fund += fund

                    print("======== Funding Time ========")
                    print("Date         : {}".format(date))
                    print("Spot   Profit: {:.2f}".format(spot_profit))
                    print("Future Profit: {:.2f}".format(future_profit))
                    print("Funding      : {:.2f}".format(fund))
                    print("\n")

        
        print("\n-------- Result -------")
        print("Total funds         : {:.2f}".format(self.total_fund + sum(self.total_fund_list)))
        print("Total account value : {:.2f}".format(future_profit + spot_profit))




                




