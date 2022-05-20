import enum
from matplotlib.pyplot import close
from ..strategy import *

class GridTrading(Strategy):
    def __init__(self, high_thresh, low_thresh, num_grids, invesment, data, name='Martingale'):
        super().__init__(data, name)
        self.high_thresh = high_thresh
        self.low_thresh  = low_thresh
        self.num_grids   = num_grids
        self.invesment   = invesment
        self.min_lose    = 0.0
        self.num_rounds  = 0
        self.amount      = 10    # -----> NEED TO CHANGE BE VAREFULL

        self.grid_levels = [level for level in range(low_thresh, high_thresh, (high_thresh-low_thresh)//num_grids)]
        self.grid_period = (high_thresh-low_thresh)//num_grids

        
        # Print some information to user
        print(" ----------  LOADING -----------")
        print("Total number of data : ", len(self.data))
        print("High Price           : {}".format(self.high_thresh))
        print("Low Price            : {}".format(self.high_thresh))
        print("Number of Grids      : {}".format(self.num_grids))
        print("Grid Period          : {}".format(self.grid_period))
        print('\n')
    
    def algo(self, *args, **kwargs):
        idx         = kwargs['idx']
        close_price = kwargs['close_price']

        # For first running
        if (len(self.trades.open_positions) == 0) and (len(self.trades.future_open) == 0):
            
            for level_idx, level in enumerate(self.grid_levels):
                if (level >= close_price):
                    break

            self.trades.auto_open("ADD", idx, level, self.amount, self.grid_levels[level_idx+1])
                       
        else:
            # Check When a position is opened
            if self.trades.open_flag == True:
                max_key = max(self.trades.key())
                self.trades.auto_open(
                    "ADD", 
                    idx, 
                    self.trades.open_positions[max_key][0]-self.grid_period, 
                    self.amount, 
                    self.trades.open_positions[max_key][0]
                )

            # Check a position is closed
            if self.trades.close_flag[0] == True:
                self.trades.auto_open(
                    "ADD",
                    idx,
                    self.trades.close_flag[0],
                    self.amount,
                    self.trades.close_flag[0] + self.grid_period
                )



            


    def result_info(self):
        print("\n-------------------- Results --------------------")
        print("Total profit in this strategy : {:.2f}".format(self.trades.total_profit()))
        print("APR                           : {:.2f}%".format((self.trades.total_profit()/self.invesment)*100))

        print("\nThanks to using ((Grid trading))")








# data = pd.read_csv('../data/BTC_2020.csv')
# data = pd.DataFrame(data.values[::-1], data.index, data.columns)

# st = GridTrading(100000, 10000, 500, 600, data, name="Grid-Trading")
# st.run()
