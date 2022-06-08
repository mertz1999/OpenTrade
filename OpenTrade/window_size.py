import plotly.graph_objects as go
import pandas as pd
import matplotlib.pyplot as plt



# Reading Date
data = pd.read_csv('./data/BTC_2021.csv')

# Reverse data
data = pd.DataFrame(data.values[::-1], data.index, data.columns)

# Set data index to "date" for change dataframe
data['date'] = pd.to_datetime(data['date'])
data         = data.set_index("date")

# Change Dataframe
data = data.resample("1D").agg({'open': 'first', 'high': 'max', 'low': 'min', 'close': 'last'})

# Function to select data
def window_size(data, idx, number_of_candle, plot=False):
    if idx > len(data):
        print("Please Enter valid index")
        exit()
    selected_data = data[idx-number_of_candle: idx]
    plot_data(selected_data)
    return selected_data


# Function for plotting data
def plot_data(data):
    plt.style.use('ggplot')

    # Make fiqure
    fig = go.Figure(data=[go.Candlestick(
                x     = data.index,
                open  = data['open'],
                high  = data['high'],
                low   = data['low'],
                close = data['close'])],
                )
    
    fig.update_layout(xaxis_rangeslider_visible=False)
    fig.update_yaxes(type="log")

    fig.show()





print(window_size(data, 100, 28, plot=False))