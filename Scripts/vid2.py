from backtesting import Backtest, Strategy
from backtesting.lib import crossover
import pandas as pd
import pandas_ta as ta

from backtesting.test import SMA, GOOG


class SmaCross(Strategy):
    fast_sma = 20
    slow_sma = 50
    sl = 0.05
    tp = 200
    
    def init(self):
        # self.sma_short = self.I(lambda x: pd.Series(x).rolling(self.fast_sma).mean(), self.close_prices)
        # self.sma_long = self.I(lambda x: pd.Series(x).rolling(self.slow_sma).mean(), self.close_prices)
        self.sma_short = self.I(ta.sma, pd.Series(self.data.Close), self.fast_sma)
        self.sma_long = self.I(ta.sma, pd.Series(self.data.Close), self.slow_sma)

    def next(self):
        price = self.data.Close[-1]
        
        if crossover(self.sma_short , self.sma_long) and not self.position:
            # self.buy(sl = (1.0-self.sl)*price, tp = (1.0+self.tp)*price)
            self.buy()
        elif crossover(self.sma_long , self.sma_short) and self.position.is_long:
            self.position.close()


bt = Backtest(GOOG, SmaCross, commission=.002,
              exclusive_orders=True)
stats = bt.run()
bt.plot()