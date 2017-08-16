import coinrepo
import bt

def btexample():
    # fetch some data
    data = bt.get('spy,agg', start='2010-01-01')
    print data.head()

    # create the strategy
    s = bt.Strategy('s1', [bt.algos.RunMonthly(),
                        bt.algos.SelectAll(),
                        bt.algos.WeighEqually(),
                        bt.algos.Rebalance()])

    # create a backtest and run it
    test = bt.Backtest(s, data)
    res = bt.run(test)

    res.display()
    res.to_csv(sep=',', path='./bar.csv')
    # first let's see an equity curve
    plot = res.plot(figsize=(15,5))
    fig = plot.get_figure()
    fig.savefig("foo.png")

def main():
    '''entry point'''
    
    # # Test bt framework installed properly  
    # data = bt.get('aapl,msft,c,gs,ge', start='2010-01-01')
    # print data.head()

    # # Test MyCoin DB connection
    # symbol_list = ['BTC', 'ETH']
    # result = coinrepo.get_coinhistory(symbol_list)
    # print result.head()
    
    btexample()

if __name__ == "__main__":
    main()
