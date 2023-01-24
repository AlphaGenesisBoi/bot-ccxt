import ccxt
import pandas as pd
import time
import pytz
from datetime import datetime
import os
import numpy as np
import plotly.graph_objects as go
import matplotlib.pyplot as plt 

pd.set_option('display.max_rows', None)

utc_time = datetime.utcnow()
eastern = pytz.timezone('US/Eastern')
local_time = utc_time.astimezone(eastern)

# Define the crypto exchange api and trading pair
exchange = ccxt.kraken({
    'apiKey': 'qdpHu7eaVytffjwTRG2/S4sggkPoQUu8EUS5PgBv+sf+yl/6zHqS7HxD' ,
    'secret': 'jGVodNNmCjiP5ucS+cRI6Kff+qQYXOBRnFWDKNUNee1WSiunDrn1zPhQ9B2KtWqvwZ0JxF8izyac/R72inC3gw==' ,
})


#Exchange Data
symbol = 'ETH/USD'
timeframe = '1d'
ohlcv = exchange.fetch_ohlcv(symbol, timeframe)
ticker = exchange.fetch_ticker(symbol)
data = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'ema1'])

#Creating dataframe from list of lists

data = pd.DataFrame(data).sort_values(by = "timestamp", ascending = False)
DataFrame = pd.DataFrame(data).sort_values(by = "timestamp", ascending = False)
#Creating a dataframe from a dictionary
#data = {ohlcv, 'columns', 'ohlcv', 'timestamp', 'open', 'high', 'low', 'close', 'volume', 'ema1'}

DataFrame['timestamp'] = pd.to_datetime(DataFrame['timestamp'], unit='m')

#####DataFrame['timestamp'] = DataFrame['timestamp'].dt.floor('60s')########
######DataFrame['timestamp'] = DataFrame['timestamp'].dt.round("1m")########("60s")

print(DataFrame.head(10))
DataFrame.to_csv('data.csv', index=False)
DataFrame = pd.read_csv('data.csv')

#Load csv into a DataFrame
#DataFrame = pd.read_csv('directory_name/data.csv')

#Display DataFrame Rows



#re-ordering data for most recent observations to be at top



# Define the moving average periods
#due to python starting index at 0, to have a period of n numnbers, need to set period to n-1
fast_period = 1000
slow_period = 26

#Calculate Simple Moving Average
#this is getting the Simple Moaving Average for close price
sma = data["close"].rolling(window = 5, min_periods = 1, center = True).mean()
#data["Rolling Average"] = 

ema = data['close'].ewm(span=5, adjust = False).mean()
data = data.sort_values("timestamp", ascending = False)
print(data)

plt.show()
plt.plot(ohlcv, label='ohlcv')
plt.plot(ema, label='ema')
plt.plot(sma, label='sma')

plt.xlabel('Week')
plt.ylabel('Value')
plt.legend()

plt.show
#print(data.head(10))
#print(data.head(10))
#data[:fast_period].plot(kind = 'bar', x = 'timestamp', y = "Rolling Average")
#plt.show()


# Fetch historical candlestick data
#Calculate Simple Moving Average
#this is getting the Simple Moaving Average for close price


#Initialize a variable to store the current position(1 = long, -1 = shout)
position = 0

#Iterate through each row of the data

for i in range(1, len(data)):
    #EMA crosses above SMA and not long, go long
    condition = None
    if condition: ema[i] > sma[i] and position <= 0
    position = 1
    print("Going long at " + str(data['close'][i]))
            
    #exchange.create_order(symbol, 'market', 'buy', 1)

#EMA cross below SMA and not short, go short


else:
    if condition: ema[i] < sma[i] and position >= 0
    position = -1 
print("Going short at" + str(data['close'][i]))
                
#exchange.create_order(symbol, 'market', 'sell', 1)
plt.plot(ohlcv, label='ohlcv')
plt.plot(ema, label='ema')
plt.plot(sma, label='sma')

plt.xlabel('Week')
plt.ylabel('Value')
plt.legend()

plt.show
print(data)
print(ema)
str