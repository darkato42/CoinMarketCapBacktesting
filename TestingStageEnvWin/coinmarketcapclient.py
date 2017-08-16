import json
import requests
import pandas as pd
import numpy as np

def get_full_history(coin_symbol):
    '''Get a full history of coin history'''
    request_url = 'http://coinmarketcap.northpole.ro/api/v6/history/' + coin_symbol + '_2016.json'
    response = requests.get(request_url)
    history2016 = json.loads(response.text)
    request_url = 'http://coinmarketcap.northpole.ro/api/v6/history/' + coin_symbol + '_2017.json'
    response = requests.get(request_url)
    history2017 = json.loads(response.text)

    ifValidFullHistory = ('error' not in history2016) and ('error' not in history2017) and ('history' in history2016) and ('history' in history2017)
    ifValid2016History = (not ifValidFullHistory) and ('history' in history2016)
    ifValid2017History = (not ifValidFullHistory) and ('history' in history2017)
    if ifValidFullHistory:
        history = {'symbol': coin_symbol, 'history': history2016['history'].items() + history2017['history'].items()}
    elif ifValid2016History:
        history = {'symbol': coin_symbol, 'history': history2016['history'].items()}
        print coin_symbol + " 2016Only"
    elif ifValid2017History:
        history = {'symbol': coin_symbol, 'history': history2017['history'].items()}
        print coin_symbol + " 2017Only"
    else:
        print coin_symbol + " failed"
        return
    return history

def get_df_full_history_usd(coin_symbol):
    '''Only select USD as price currency into pandas DataFrame'''
    coin_history = get_full_history(coin_symbol)
    if not coin_history:
        return
    column_names = ["position",
        "name",
        "symbol",
        "category",
        "marketCap",
        "price",
        "availableSupply",
        "volume24",
        "change1h",
        "change24h",
        "change7d",
        "timestamp"]

    data = []
    for date in coin_history['history']:
        if date[1]['marketCap'] and 'usd' in date[1]['marketCap']:
            date[1]['marketCap'] = date[1]['marketCap']['usd']
        else:
            date[1]['marketCap'] = None

        if date[1]['price'] and 'usd' in date[1]['price']:
            date[1]['price'] = date[1]['price']['usd']
        else:
            date[1]['price'] = None

        if date[1]['volume24'] and 'usd' in date[1]['volume24']:
            date[1]['volume24'] = date[1]['volume24']['usd']
        else:
            date[1]['volume24'] = None

        selected_row = []
        selected_row.append(date[0])
        for item in column_names:
            selected_row.append(date[1][item])
        data.append(selected_row)

    df = pd.DataFrame(data, columns = ["date"] + column_names)
    df['date'] = pd.to_datetime(df['date'], dayfirst='true')
    df['marketCap'] = df['marketCap'].astype('float64')
    df['price'] = df['marketCap'].astype('float64')
    df['volume24'] = df['marketCap'].astype('float64')
    df['availableSupply'] = df['availableSupply'].astype('float64')
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
    df = df.sort_values(by='date')
    del df['timestamp']
    df = df.where(pd.notnull(df), None)
    return df
