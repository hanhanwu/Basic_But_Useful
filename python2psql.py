import pandas as pd
from sqlalchemy import create_engine

# Better way for DB connection
## this can be used for not only Redshift data reading, but also shcema creation, AWS copy command, etc.
def read_rs_data(query, credential_file, db, has_return_results):
    """
    Connect to the specified database and execute the query.
    :param query: The query you need to execute
    :param db: choose a db used as the key in crednetials file, so that you can load credentials for that DB
    :return: Query results as a dataframe
    """
    username, pwd, host, database, port = generate_db_conn(credential_file, db)
    
    if has_return_results:
        conn = 'postgresql://' + username + ':' + pwd + '@' + host + ':' + port + '/' + database
        print(conn)
        engine = create_engine(conn)
        df = pd.read_sql(query, engine, coerce_float=True, params=None,
                      parse_dates=None, columns=None, chunksize=None)
        return df
    else:
        conn_string = "dbname=%s host=%s port=%s user=%s password=%s" % (database, host, port, username, pwd)
        with psycopg2.connect(conn_string) as conn:
            with conn.cursor() as curs:
                curs.execute(query)
                curs.close()
            conn.commit()

# Connect to Redshift and run query
# Get credentials for database access
read_user_name = "[USERNAME]"
read_passwd = "[PSWD]"
read_host_name = "[HOST]"

# Set connection to DB
connection = 'postgresql://' + read_user_name + ':' + read_passwd + '@' + read_host_name + ':[PORT]/[db]'
engine = create_engine(connection)

query = """
        select * from TEST_TABLE
        limit 7
        """

test = pd.read_sql(query, engine, index_col=None, coerce_float=True, params=None,
                      parse_dates=None, columns=None, chunksize=None)

print test.T.to_dict().values()


# when query has %, when using python, instead of using %, you need to use %%
query = """
        select * from TEST_TABLE
        where col1 like 'abc%%'
        limit 7
        """


# truncate float without rounding
int(s* 100)/100.0  # keep 2 digits
int(s* 1000)/1000.0  # keep 3 digits


# Get all the columns from each table
for ds_tb in ds_tablelst:
    print(ds_tb)
    query = """
        SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS
        WHERE table_catalog = 'my_catalog'
        AND table_schema = 'my_DB'
        and table_name ='""" + ds_tb + """'"""
    
    col_lst = pd.read_sql(query, engine, index_col=None, coerce_float=True, params=None,
                      parse_dates=None, columns=None, chunksize=None).values
    
    for col in col_lst:
        col_set.add(col[0])
