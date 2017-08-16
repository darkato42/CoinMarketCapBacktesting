import coinrepo
import bt

def main():
    '''entry point'''
    
    symbol_list = ['BTC', 'ETH']
    result = coinrepo.get_coinhistory(symbol_list)
    plot = result.plot(figsize=(15,5))

    # Test bt framework installed properly
    #data = bt.get('aapl,msft,c,gs,ge', start='2010-01-01')
    #print data.head()

if __name__ == "__main__":
    main()