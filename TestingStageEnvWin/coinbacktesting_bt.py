import coinrepo
import bt

def main():
    '''entry point'''
    
    # Get Test Data with all fields
    symbol_list = ['BTC', 'ETH']
    history = coinrepo.get_coinhistory(symbol_list)
    history = history.set_index('Date')

    # Pivot to have only price as timeseries
    pricehistory = history.pivot(columns='Symbol')['Price']

    # Create the strategy
    s = bt.Strategy('s1', [bt.algos.RunMonthly(),
                            bt.algos.SelectAll(),
                            bt.algos.WeighEqually(),
                            bt.algos.Rebalance()])

    # create a backtest and run it
    test = bt.Backtest(s, pricehistory)
    res = bt.run(test)

    res.display()

    # Save figures
    plot = pricehistory.plot(figsize=(15,5))
    fig = plot.get_figure()
    fig.savefig("price.png")
    plot1 = res.plot_weights(figsize=(15,5))
    fig1 = plot1.get_figure()
    fig1.savefig("bt_rest.png")

    # # Test bt framework installed properly
    # data = bt.get('aapl,msft,c,gs,ge', start='2010-01-01')
    # print data.head()

if __name__ == "__main__":
    main()