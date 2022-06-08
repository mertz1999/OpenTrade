from ..strategy import *

class TrailingBuySell(Strategy):
    def __init__(self,trigger_price, trailing_percent, amount, data, invesment, fee, name='TrailingBuySell', method="VOLUME"):
        super().__init__(data, invesment, fee, name, method)

        self.trigger_price    = trigger_price
        self.trailing_percent = trailing_percent
        self.amount           = amount

        self.max_or_min       = 0.0
        self.direction        = +1
        self.start            = False
        self.trigger          = False

        # Print some information to user
        print(" ----------  LOADING -----------")
        print("Total number of data : ", len(self.data))
        print('\n')


    def algo(self, *args, **kwargs):
        idx         = kwargs['idx']
        close_price = kwargs['close_price']
        date        = kwargs['date']

        # First of all Check direction to select we must trailing sell or trailing buy
        if self.start == False:
            self.start = True
            if close_price < self.trigger_price:
                print("Trailing Sell: ")
                self.direction = +1
            else:
                print("Trailing Buy: ")
                self.direction = -1
        else:
            # In Trailing sell
            if self.direction == +1:
                # Check if we reach trigger price and update it
                if close_price >= self.trigger_price:
                    self.trigger_price = close_price
                    self.trigger       = True
                # Check when price back based in trailing percent value
                elif close_price <= self.trigger_price + self.trigger_price*self.trailing_percent/100 and self.trigger:
                    Strategy.print_date(date)
                    self.trades.sell(idx, close_price, self.amount * close_price)
                    self.end = True

            # In Trailing buy
            elif self.direction == -1:
                # Check if we reach trigger price and update it
                if close_price <= self.trigger_price:
                    self.trigger_price = close_price
                    self.trigger       = True
                # Check when price back based in trailing percent value
                elif close_price >= self.trigger_price + self.trigger_price*self.trailing_percent/100 and self.trigger:
                    print(self.trigger_price)
                    Strategy.print_date(date)
                    self.trades.open(idx, close_price, self.amount)
                    self.end = True





    def result_info(self):
        pass
        print("\nThanks to using ((Trailing strategy))")

