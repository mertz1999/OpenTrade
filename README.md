# OpenTrade
## OpenSource Algo-Trading Bots



OpenTrade is an open source project that consist of Popular strategies and backtest.

- Popular strategies
- Backtest
- Open sourse
- Easy to run

## List of strategies

- Martingale
- Grid Trading
- Infinity Grid
- Rebalance
- SmartTrade
- Spot-Future arbintage
- TWAP

> Some strtegies are implemented based on [Pionex blog page](https://www.pionex.com/blog/)

## What about backtest:
A built-in backtest is used to test strategies ,so you need to download historical data for testing.
You can make strategies for Spot and future markets by yourself. 


## How to use?
By running Strategies file in base folder you can run demo files.
but if you download or clone project you can use this approach:

```
git clone https://github.com/mertz1999/OpenTrade.git
cd Opentrade
```

Then you can load OpenTrade in you python file:
```python
from OpenTrade.strategy_list.martingale import Martingale
import pandas as pd

data = pd.read_csv('./data/BTC_2020.csv')
data = pd.DataFrame(data.values[::-1], data.index, data.columns)

st = Martingale(1, -1, 3, data, 700, 1)
st.run()
```

### [See Strategies Doc](https://github.com/mertz1999/OpenTrade/tree/main/Doc)

# Todo:
##### Todo Feature and fix bug:
- <del>Make Auto sell at certain price</del>
- <del>Make Auto buy at certain price</del>
- <del>Set fee value to hole positions</del>
- <del>Set volume </del>
- Plotting
- <del>Volume based backtest beside orderbased</del>
- Make plot
- <del>Future trading</del>
- Leverage

##### Todo Strategy:
- <del>Martinglae</del>
- <del>Grid Trafing</del>
- <del>Rebalancing</del>
- <del>InfinityGrids</del>
- <del>Smart Trade</del>
- <del>Spot Future</del>
- <del>TWAP</del>









