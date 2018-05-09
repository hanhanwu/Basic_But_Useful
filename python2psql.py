import pandas as pd
from sqlalchemy import create_engine

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



# truncate float without rounding
int(s* 100)/100.0  # keep 2 digits
int(s* 1000)/1000.0  # keep 3 digits
