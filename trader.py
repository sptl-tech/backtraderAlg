import backtrader 
import datetime
from strategy import TestStrategy

cerebro = backtrader.Cerebro() #connects a datafeed and we use it to run our strategy against datafeed to visualize outcome

cerebro.broker.set_cash(100000) #set the cash amount that we want to use

data = backtrader.feeds.YahooFinanceCSVData(
    dataname='nvda.csv',
    # Do not pass values before this date
    fromdate=datetime.datetime(2000, 1, 1), 
    # Do not pass values after this date
    todate=datetime.datetime(2000, 12, 31),
    reverse=False)

cerebro.adddata(data) #passes data and connects to cerebro 

cerebro.addstrategy(TestStrategy)
#use cerebro to see what our intial value is and what our final value would be w/ strategy
print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

cerebro.run()

print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

cerebro.plot()
 