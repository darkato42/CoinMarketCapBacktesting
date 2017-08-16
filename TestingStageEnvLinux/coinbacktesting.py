import coinrepo
import bt

def main():
    '''entry point'''
    
    # Test MyCoin DB connection
    symbol_list = ['BTC', 'ETH']
    result = coinrepo.get_coinhistory(symbol_list)
    print result.head()
    
    # Test bt framework installed properly
    data = bt.get('aapl,msft,c,gs,ge', start='2010-01-01')
    print data.head()

if __name__ == "__main__":
    main()