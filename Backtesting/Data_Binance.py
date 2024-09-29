# Install Libs
#! pip install python-binance

# Source / Documentation : 
# https://github.com/sammchardy/python-binance/tree/master

from binance.client import Client
import pandas as pd
import matplotlib.pyplot as plt


class Crypto :
    def __init__(self, ticker, start_date , end_date, interval) :
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date
        self.interval = interval

    def get_data(self) :
        client = Client('', '')
        klines = client.get_historical_klines(self.ticker, self.interval, self.start_date, self.end_date)
        df = pd.DataFrame(klines, columns=[
                                    'Open_time','Open', 'High', 'Low', 'Close',
                                        'Volume','Close_time', 'dv','num_trades',
                                        'taker_buy_vol','taker_buy_base_vol', 'ignore'
                                ])
        df['Close_time'] = pd.to_datetime(df['Close_time'], unit='ms')
        df.set_index('Close_time', inplace=True)
        df.drop(columns=['Open_time','ignore'], inplace=True)

        
        df.index = df.index.round('min')        # Round close time to normalize
        df = df.astype(float)
        return df
    
    def plot_data(self, df) :
        #Plot close price and volume 
        fig, ax1 = plt.subplots(figsize=(15, 8)) 
        #Price
        ax1.set_xlabel('time')
        ax1.set_ylabel('Close')
        ax1.plot(df.index, df['Close'], color='black', linewidth=2)
        ax1.tick_params(axis='y')
        #Volume
        ax2 = ax1.twinx()
        ax2.set_ylabel('dv')
        ax2.bar(df.index, df['dv'], color='blue', width=0.01, alpha=0.5)
        ax2.tick_params(axis='y')
        #Show
        fig.tight_layout()
        plt.show()

    def save_data(self, df : pd.DataFrame) : 
        hdf5filename = '//Users/theomontant/Quant-project/Backtesting/Time_series//' + self.ticker + '_' + self.interval + '_' + self.start_date + '_' + self.end_date + '.h5'
        df.to_hdf(hdf5filename, key='ohlcv', mode='w')
