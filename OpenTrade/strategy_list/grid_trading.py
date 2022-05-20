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

        self.grid_levels = [level for level in range(low_thresh, high_thresh, (high_thresh-low_thresh)//num_grids)]

        print(self.grid_levels)
        
        # Print some information to user
        print(" ----------  LOADING -----------")
        print("Total number of data: ", len(self.data))
        print("High Price          : {}%".format(self.high_thresh))
        print("Low Price           : {}%".format(self.high_thresh))
        print("Number of Grids     : {}%".format(self.num_grids))
        print('\n')
    
    def algo(self, *args, **kwargs):
        idx         = kwargs['idx']
        close_price = kwargs['close_price']


    def result_info(self):
        pass








# data = pd.read_csv('../data/BTC_2020.csv')
# data = pd.DataFrame(data.values[::-1], data.index, data.columns)

# st = GridTrading(100000, 10000, 500, 600, data, name="Grid-Trading")
# st.run()
