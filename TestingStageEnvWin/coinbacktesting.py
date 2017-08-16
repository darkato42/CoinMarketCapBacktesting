import coinrepo
import bt

def main():
    '''entry point'''
    
    symbol_list = ['BTC', 'ETH']
    result = coinrepo.get_coinhistory(symbol_list)
    print result.head()
    
if __name__ == "__main__":
    main()