import pyodbc
import pandas as pd

def get_db_cursor():
    server = 'tcp:coin.database.windows.net,1433'
    database = 'MyCoinDb_test'
    username = 'testuser_readonly'
    password = 'CLd6bZTK'
    driver= '{ODBC Driver 13 for SQL Server}'
    cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    return cursor

def get_allcoinsymbols():
    sql = """\
        SELECT  Id,
                symbol,
                ticker,
                history,
                last14Days FROM dbo.CoinMktCapSymbol
    """
    cursor = get_db_cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    columnnames = [column[0] for column in cursor.description]
    df = pd.DataFrame.from_records(rows, columns=columnnames)
    return df

def db_connect_test():
    '''Use this method to test connection with SQL DB and getting symbols returned'''
    testresult = get_allcoinsymbols()
    print testresult