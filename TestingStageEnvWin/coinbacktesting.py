import coinrepo

def main():
    '''entry point'''
    
    symbol_list = ['BTC', 'ETH']
    result = coinrepo.get_coinhistory(symbol_list)
    print result
    
if __name__ == "__main__":
    main()