# Raw Package
import numpy as np
import pandas as pd
import yfinance as yf
import plotly.graph_objs as go



def download(tickers='BTC-USD', start='2022-03-20', end='2022-05-18', interval='5m', save="BTC_USD"):
    data = yf.download(tickers, '2022-03-20', '2022-05-18', '5m')
    data.to_csv("../src/"+save+".csv")

def viz_data(data, name='Bitcoin'):
    fig = go.Figure()

    #Candlestick
    fig.add_trace(go.Candlestick(x=data.index,
                    open=data['Open'],
                    high=data['High'],
                    low=data['Low'],
                    close=data['Close'], name = 'market data'))

    # Add titles
    fig.update_layout(
        title=name+' live share price evolution',
        yaxis_title=name+' Price (kUS Dollars)')

    # X-Axes
    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=15, label="15m", step="minute", stepmode="backward"),
                dict(count=45, label="45m", step="minute", stepmode="backward"),
                dict(count=1, label="HTD", step="hour", stepmode="todate"),
                dict(count=6, label="6h", step="hour", stepmode="backward"),
                dict(step="all")
            ])
        )
    )

    #Show
    fig.show()
