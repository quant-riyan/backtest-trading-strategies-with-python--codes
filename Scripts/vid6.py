from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from backtesting.test import GOOG

import pandas as pd
import numpy as np

class SimpleRSIStrategy(Strategy):
    rsi_period = 14
    rsi_oversold = 20
    rsi_overbought = 80
    sl = 0.3
    tp = 3
    
    def init(self):
        close = pd.Series(self.data.Close)

        delta = close.diff()
        
        gain = delta.where(delta > 0, 0).rolling(window=self.rsi_period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=self.rsi_period).mean()
        
        # Step 3: Calculate Relative Strength (RS) - avoid division by zero
        rs = gain / loss.where(loss != 0, np.nan)
        
        # Step 4: Calculate RSI
        rsi_series = 100 - (100 / (1 + rs))
        
        # Step 5: Convert to numpy array and store as indicator
        self.rsi = self.I(lambda: rsi_series)
    
    def next(self):
        enter_price = self.data.Close[-1]
        current_rsi = self.rsi[-1] if not np.isnan(self.rsi[-1]) else 50

        if ( self.rsi_oversold > current_rsi and not self.position ):
            self.buy(sl = (1. - self.sl) * enter_price, tp = (1.0 + self.tp) * enter_price)

        elif (self.rsi_overbought < current_rsi and self.position.is_long ):
            self.position.close()


bt = Backtest(GOOG, SimpleRSIStrategy, commission=0.001, exclusive_orders=True)

stats = bt.run()
print(stats)
bt.plot()