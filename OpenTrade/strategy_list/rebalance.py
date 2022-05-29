from ..strategy import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class OneSideRebalancing(Strategy):
    def __init__(self, data, invesment, fee, name='Martingale', method="VOLUME"):
        super().__init__(data, invesment, fee, name, method)
                
    def run(self):
        pass
          
    def algo(self, *args, **kwargs):
        pass
    
    def result_info(self):
        pass

class Rebalance():
    def __init__(self, period ,max_profit, data, invesment, fee, name='temp', method='VOLUME'):
        self.max_profit         = max_profit
        self.data               = data
        self.start_invest       = invesment
        self.total_coins        = len(data)
        self.total_profit_value = 0.0
        self.period             = period
        self.start              = False
        self.symbol             = [data_side['symbol'][10] for data_side in data]

        # Define Each side of balancing
        self.sides_coin = []
        for index, side_data in enumerate(data):
            self.sides_coin.append(OneSideRebalancing(side_data, invesment/self.total_coins, fee, name="Rebalancing_"+self.symbol[index], method=method))

        # path = "./inc/"+name+".txt"
        # os.makedirs('./inc/', exist_ok=True)
        self.log_file_2 = open("temp.txt", "w")
        
        # Iterate on each data points of one point and find datas that are same time
        for idx in range(len(self.data[0])):
            # Every 5 Minute
            if idx % self.period == 0:
                flag = False
                # Find close_prices
                close_price_sides = []
                for side_index,side in enumerate(self.sides_coin):
                    # First coin is Date reference
                    if side_index == 0:
                        date = self.data[side_index]['date'][idx]
                        close_price_sides.append(self.data[side_index]['close'][idx])

                    # Based on reference date select other coin prices
                    else:                    
                        if len(self.data[side_index][self.data[side_index]['date'] == date]) > 0:
                            close_price_sides.append(self.data[side_index][self.data[side_index]['date'] == date].iloc[0].close)
                        else:
                            flag = True
                            break
                
                # If Flag reach True it means that there is not date in other coins data
                if flag == True:
                    continue
                    
                

                # Find profits
                self.total_profit_value = []
                for index_side, side in enumerate(self.sides_coin):
                    self.total_profit_value.append(side.trades.total_online_profit(close_price_sides[index_side]))
                
                self.log_file_2.write(str(sum(self.total_profit_value)))
                self.log_file_2.write('\n')

                # Check for total profit that reaches max threshold 
                if  sum(self.total_profit_value) > (self.start_invest + self.max_profit):
                    print("\nEnd of bot trading (Reach Take profit)")
                    for index_side, side in enumerate(self.sides_coin): 
                        print("("+self.symbol[index_side]+")", end=' ')
                        print("({}) ".format(str(date)), end=' ')
                        side.trades.close_all(idx, close_price_sides[index_side])
                    break
 
                # For First one that bot is 
                if self.start == False:
                    print("-------- BOT IS STARTING --------\n")
                    self.start = True
                    for index_side, side in enumerate(self.sides_coin): 
                        print("("+self.symbol[index_side]+")", end=' ')
                        print("({}) ".format(str(date)), end=' ')
                        side.trades.open(idx, close_price_sides[index_side], side.trades.invesment)

                    continue
            
                # check for loss of balance
                balaced_value = sum(self.total_profit_value) / self.total_coins
                # Itrate on each coin
                for index_side, side in enumerate(self.sides_coin): 
                    # Check how many changes in value
                    if abs(balaced_value - self.total_profit_value[index_side]) > 1:

                        # Sell if balance is lower
                        if balaced_value < self.total_profit_value[index_side]:
                            print("("+self.symbol[index_side]+")", end=' ')
                            print("({}) ".format(str(date)), end=' ')
                            side.trades.sell(idx, close_price_sides[index_side], abs(balaced_value - self.total_profit_value[index_side]))

                        # Buy if balance is higher
                        else:
                            print("("+self.symbol[index_side]+")", end=' ')
                            print("({}) ".format(str(date)), end=' ')
                            side.trades.open(idx, close_price_sides[index_side], abs(balaced_value - self.total_profit_value[index_side]))
                        

        print("\n ---------- Result -----------")
        print("Total value after bot: ", sum(self.total_profit_value))


    






