from ..strategy import *

class Martingale(Strategy):
    def __init__(self, take_profit, price_scale, safety_orders, data,invesment, fee,name='Martingale'):
        super().__init__(data,invesment, fee, name)
        self.take_profit   = take_profit
        self.price_scale   = price_scale
        self.safety_orders = safety_orders
        self.trades.invesment     = invesment
        self.min_lose = 0.0
        self.num_rounds = 0

        share = self.trades.invesment // (2 ** self.safety_orders)
        self.Invertment_parts = [share]

        for i in range(self.safety_orders):
            self.Invertment_parts.append(2**i * share)
        
        # Print some information to user
        print(" ----------  LOADING -----------")
        print("Total number of data: ", len(self.data))
        print("Take profit: {}%".format(self.take_profit))
        print("Price scale: {}%".format(self.price_scale))
        print('\n')
    
    def algo(self, *args, **kwargs):
        idx         = kwargs['idx']
        close_price = kwargs['close_price']

        # Check for zero position opening 
        if len(self.trades.open_positions) == 0:
            self.num_rounds += 1
            print("-------------  Round Started {} -------------- \n".format(self.data['date'][idx]))
            self.trades.log("-------------  Round Started {} -------------- \n".format(self.data['date'][idx]),1)
            self.trades.open(idx, close_price, self.Invertment_parts[0])
        
        else:
            # Check total profit
            total_online_profits = self.trades.total_online_profit(close_price)
            total_online_investment = self.trades.total_investment()
            profit_in_percent = (total_online_profits / total_online_investment) * 100
            # Check min profit
            if profit_in_percent < self.min_lose:
                self.min_lose = profit_in_percent

            # Check take_profit threshold
            if profit_in_percent >= self.take_profit:
                self.trades.close_all(idx, close_price)
                print("\n")
                self.trades.log('', 2)
                # break
            else:
                if len(self.trades.open_positions) < len(self.Invertment_parts):
                    last_position = self.trades.open_positions[max(self.trades.open_positions.copy().keys())]
                    online_last_profit = ((close_price - last_position[0]) / last_position[0]) * 100
                    if online_last_profit <= self.price_scale:
                        self.trades.open(idx, close_price, self.Invertment_parts[len(self.trades.open_positions)])


    def result_info(self):
        print("\n-------------------- Results --------------------")
        print("Total profit in this strategy : {:.2f}".format(self.trades.total_profit()))
        print("APR                           : {:.2f}%".format((self.trades.total_profit()/self.trades.invesment)*100))
        print("Biggest drawdown              : {:.2f}%".format(self.min_lose))
        print("Total number of Rounds        : {}".format(self.num_rounds))
        print("\nThanks to using ((Martingale))")

        self.trades.log("", 2)
        self.trades.log("Total profit in this strategy : {:.2f}".format(self.trades.total_profit()))
        self.trades.log("APR                           : {:.2f}%".format((self.trades.total_profit()/self.trades.invesment)*100))
        self.trades.log("Biggest drawdown              : {:.2f}%".format(self.min_lose))
        self.trades.log("Total number of Rounds        : {}".format(self.num_rounds))