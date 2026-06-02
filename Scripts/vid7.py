from backtesting import Backtest, Strategy
from backtesting.test import GOOG
import pandas as pd

class IchimokuStrategy(Strategy):
    sl = 0.08
    tp = 0.35

    def init(self):

        high_series = pd.Series(self.data.High)
        low_series = pd.Series(self.data.Low)
        close_series = pd.Series(self.data.Close)

        self.tenkan_sen = self.I(lambda h, l: (h + l) / 2.0, high_series, low_series, plot=False)
        self.kijun_sen = self.I(lambda h, l: (h.rolling(window=26).max() + l.rolling(window=26).min()) / 2.0, high_series, low_series, plot=False)
        self.senkou_span_a = self.I(lambda t, k: (t + k) / 2.0, self.tenkan_sen, self.kijun_sen, plot=False)
        self.senkou_span_b = self.I(lambda h, l: (h.rolling(window=52).max() + l.rolling(window=52).min()) / 2.0, high_series, low_series, plot=False)
        self.chikou_span = self.I(lambda c: c.shift(periods=-26), close_series, plot=False)
        self.cloud_top = self.I(lambda a, b: (a + b) / 2.0, self.senkou_span_a, self.senkou_span_b, plot=False)
        self.cloud_bottom = self.I(lambda h, l: (h.rolling(window=52).max() + l.rolling(window=52).min()) / 2.0, high_series, low_series, plot=False)

    def next(self):
        enter_price = self.data.Close[-1]

        # Buy Condition: Tenkan-Sen crossover Kijun-Sen and price > Ichimoku cloud
        if self.kijun_sen < self.tenkan_sen and self.data.Close > self.cloud_top and\
              self.data.Close > self.cloud_bottom and not self.position:
            self.buy(sl = enter_price - self.sl * self.kijun_sen, tp = enter_price * (1.0 +  self.tp ))
        
        
        # Sell Condition: Kijun-Sen crossover Tenkan-Sen and price < Ichimoku cloud
        if self.kijun_sen > self.tenkan_sen and self.data.Close < self.cloud_top and\
              self.data.Close < self.cloud_bottom and self.position:
            self.position.close()


bt = Backtest(GOOG, IchimokuStrategy, cash = 10_000_000, commission=0.001, exclusive_orders=True)

stats = bt.run()
print(stats)
bt.plot()