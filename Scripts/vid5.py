from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from backtesting.test import GOOG
from backtesting.lib import plot_heatmaps

import pandas as pd
import pandas_ta as ta
import numpy as np

def custom_metric(results):
    win_rate = results['Win Rate [%]']
    sharpe_ratio = results['Sharpe Ratio']

    num_trades = results['# Trades']
    if num_trades < 20:
        return -100

    return win_rate * sharpe_ratio

class SmaCross(Strategy):
    fast_sma = 10
    slow_sma = 40
    sl = 0.2
    tp = 1
    
    def init(self):
        self.sma_short = self.I(ta.sma, pd.Series(self.data.Close), self.fast_sma)
        self.sma_long = self.I(ta.sma, pd.Series(self.data.Close), self.slow_sma)

    def next(self):  
        enter_price = self.data.Close[-1]

        if crossover(self.sma_short , self.sma_long) and not self.position:
            self.buy(sl = (1. - self.sl) * enter_price, tp = (1.0 + self.tp) * enter_price)
        elif crossover(self.sma_long , self.sma_short) and self.position.is_long:
            self.position.close()


bt = Backtest(GOOG, SmaCross, commission=0.001, exclusive_orders=True)

# stats = bt.run()
# print(stats)
# bt.plot()

# Simple optimization
stats, heatmap = bt.optimize(
    fast_sma=range(10, 70, 10),
    slow_sma=range(20, 100, 10),
    sl=[x / 10 for x in range(1, 5)],
    maximize=custom_metric,            # Use your custom metric
    constraint=lambda p: p.slow_sma > p.fast_sma + 10,  # Ensure reasonable gap
    return_heatmap=True
)

print("Optimization Results:")
print(f"Best parameters - fast_sma: {stats._strategy.fast_sma}, slow_sma: {stats._strategy.slow_sma},   SL: {stats._strategy.sl}")
print(f"Total return: {stats['Return [%]']:.2f}%")

# Run final backtest with best parameters
print("\nFinal Strategy Performance:")
print(stats)

plot_heatmaps(heatmap, agg='mean')