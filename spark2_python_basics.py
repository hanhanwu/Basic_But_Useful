"""
Useful links:

* PySpark Window functions: https://medium.com/expedia-group-tech/deep-dive-into-apache-spark-window-functions-7b4e39ad3c86
* Specify spark session: https://github.com/hanhanwu/Hanhan-Spark-Python/blob/master/Spark2.0/how_to_define_spark.py
* How to speed up pyspark join: https://towardsdatascience.com/the-art-of-joining-in-spark-dcbd33d693c
  * Also check whether join() is the most time consuming part in the whole pipeline, sometimes the most time consuming part is saving the data
"""

import pandas as pd
import numpy as np
from pyspark_dist_explore import hist
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

from pyspark.sql.functions import desc, row_number, monotonically_increasing_id, udf, sum, count, round, col, greatest
from pyspark.sql.window import Window
from pyspark.sql.types import IntegerType, StringType, DoubleType


# create database
%sql
CREATE DATABASE IF NOT EXISTS my_db;
# drop dtabase
DROP DATABASE IF EXISTS encrypted_data CASCADE; # drop all relevant tables
DROP DATABASE IF EXISTS encrypted_data RESTRICT; # if there is non-empty table in the DB, cannot drop the DB, this is by default
# Change table name
ALTER TABLE my_db.my_tb1 RENAME TO my_db.my_tb2;

# create table
%sql
CREATE TABLE IF NOT EXISTS my_db.my_tb as (SELECT...);

# date operations
%sql
select my_date, date_add(cast(my_date as DATE), 1) as next_date
from mydb.my_tb;


# Import data to Databricks and read
## Through the UI, you can choose to import data into notebook and specify the location, by default it's under /dbfs/FileStore/tables/
## you can also import as table, suggest to choose "infer schema" so that it can specify most of the columns' data types right
### If loaded into notebook
%fs ls /FileStore/tables/my_folder/
%fs ls dbfs:/FileStore/my_folder/
 
# Download files from DBFS FileStore/
* How to find instance name url (HOST), check this link: https://docs.databricks.com/workspace/workspace-details.html#workspace-url
* After the instance url, append "files/" + the file path under "FileStore", copy this link to the browser and the file will be downloaded automatically

import pandas as pd
df = pd.read_csv('/dbfs/FileStore/tables/my_folder/myfile.csv')
df.head()

### If loaded into table (Prefered method, cuz above method might have wrong data types)
sdf = spark.table(f'myfile')
sdf.dtypes

### Load dataframes from the query
sdf = spark.sql("SELECT * FROM forecast_exp.columns_metadata")
df = sdf.toPandas()


## Create sdf from scratch
df = spark.createDataFrame([
    ('A', '2020-11-09', -10, -10), ('A', '2020-11-16', None, None), ('A', '2020-11-23', 10, 10),
    ('B', '2020-11-10', 10, 10), ('B', '2020-11-17', 30, 10), ('B', '2020-11-24', 50, 20),
], ['col1', 'col2', 'col3', 'col3']).cache()
display(df)

## Create sdf from pandas df (schema is required when a column's type is hard to infer)
from pyspark.sql.types import StructType, StructField, DoubleType, StringType

pdf = pd.DataFrame({
                'col1': ['D', 'D', 'D'],
                'col2': ['2020-11-10', '2020-11-17', '2020-11-24'],
                'col3': [None, None, None],
                'col4': [10.0, 10.0, 20.0]
            })
schema = StructType([StructField('col1', StringType(), True), StructField('col2', StringType(), True), 
                     StructField('col3', DoubleType(), True), StructField('col4', DoubleType(), True)])
sdf = spark.createDataFrame(pdf, schema=schema).cache()
sdf.show()


# Databricks create and load widgets
dbutils.widgets.removeAll()
dbutils.widgets.text(name="text1", defaultValue="", label="text1")
text1 = dbutils.widgets.get('text1')


# Conditional withColumn
import org.apache.spark.sql.functions.when
mydf.withColumn("new_col", when(df.col1 > 3, col2*2).otherwise(0.0))


# Apply a function on multiple cols
## If only choose sub-cols
sdf = sdf.select([sha2(sdf[col], 256).alias(col) for col in cols if col in sdf_cols])
## If want to have all original cols
for col in cols:
  sdf = sdf.withColumn(mask_col, sha2(concat(lit(salt_sha2), mask_col), 256))
  sdf = sdf.withColumn(nullify_col, lit(None).cast('string'))  # cast to string so that it can be saved as parquet
    


# write and load parquet
## Better to reorder the data when reading, since the partition might changed the order, do this especially when you need to convert spark DF to pandas DF...
# write the data, overwrite if exists
# !!! Different format beyond parquet: https://spark.apache.org/docs/latest/sql-data-sources-load-save-functions.html
## Make sure there is no null type in the df
df.printSchema()
df.col.cast('string') # cast null type cols as other types

df.write.mode('overwrite').parquet(out_dir + 'input_df.parquet') # save as file
DB = 'my_DB'
tb = 'my_table'
sdf.write.mode("overwrite").saveAsTable(f'{DB}.{tb}') # save spark dataframe as table in DB, different save modes: https://spark.apache.org/docs/2.3.0/sql-programming-guide.html#save-modes

sdf.repartition('col1').write.mode("overwrite").partitionBy('col1').saveAsTable(f'{dest_db}.{tb}')  # repartion a giant table to reduce small files in order to speed up future queries

# read the data from DBFS
## More about databricks file system: https://docs.databricks.com/data/databricks-file-system.html
out_dir = '/dbfs/mnt/outputs/'
input_file = out_dir + 'input_df.parquet'  # it can also be a folder ended with "/" here
df_input = spark.read.parquet(input_file).orderBy(['rid', 'col1']).cache()


# When using where to find matched list, when there is data type mismatch
## Changing dataframe data type won't work, you have to change the datatype on the right side of the filtering
from pyspark.sql.functions import array, lit
df_rules.where(df_rules.consequent == array(lit(1L)))


# Insert rows for missing dates
## In this case, the time interval is 7 days
from datetime import date
import datetime
from pyspark.sql.window import Window
from pyspark.sql.types import DateType, ArrayType

winSpec = Window.partitionBy(['col1', 'col2']).orderBy("start_date")

test_df = sdf.withColumn('pre_end_date', F.lag('end_date', 1).over(winSpec))
test_df = test_df.withColumn('diff', F.datediff('start_date', 'pre_end_date'))\
                 .orderBy(['col1', 'col2', 'start_date'])

def _get_next_dates(start_date: date, diff: int, interval: int = 7) -> List[date]:
    return [start_date + datetime.timedelta(days=days) for days in range(0, diff, interval)]
get_next_dates_udf = udf(_get_next_dates, ArrayType(DateType()))
  
added_df = test_df.filter(F.col('diff') > 1).withColumn('_next_dates', get_next_dates_udf('pre_end_date', 'diff', F.lit(7))) \
          .withColumn('start_date', F.explode('_next_dates')) \
          .withColumn('end_date', F.col('start_date') + F.lit(7)) \
          .withColumn('col3', F.lit(0)) \
          .withColumn('col4', F.lit(0)) \
          .select(['col1', 'col2', 'start_date', 'end_date', 'col3', 'col4'])

test_df = test_df.select(['col1', 'col2', 'start_date', 'end_date', 'col3', 'col4'])\
                 .union(added_df).orderBy(['col1', 'col2', 'start_date'])
display(test_df)


# Plot histogram from spark dataframe
from pyspark_dist_explore import hist  # install library pyspark_dist_explore
import matplotlib.pyplot as plt

df = sqlContext.sql("""
select col from my_table
""").cache()

fig, ax = plt.subplots()
hist(ax, df, bins = 20, color=['green'])
display(fig)


# Get the distribution of a column
def get_percentile(col):
    result = {'min': np.nanpercentile(col, 0), '1%':np.nanpercentile(col, 1),
             '10%':np.nanpercentile(col, 10), '15%':np.nanpercentile(col, 15),
             '25%':np.nanpercentile(col, 25), '50%':np.nanpercentile(col, 50), '75%':np.nanpercentile(col, 75),
             '85%':np.nanpercentile(col, 85), '95%':np.nanpercentile(col, 95), '99%':np.nanpercentile(col, 99),
              'max':np.nanpercentile(col, 100)}
    return result

# convert a col to pandas list
print(get_percentile(list(df.select('ct').toPandas()['ct'])))


# Apply window function
# NOTE: Pandas rolling window is more complex to use in order to achieve the same results, check code here: 
## https://github.com/hanhanwu/Basic_But_Useful/blob/master/python_dataframe.py
my_udf = udf(lambda col: 'pink' if has_icecream else 'green', StringType())
df = df.withColumn('col1', my_udf('col'))

win_spec = Window.partitionBy([col2, col3]).orderBy('time').rowsBetween(-2, -1)  # the window is formed by the previous 2 records of the current record
df = df.withColumn('col_new', count('col1').over(win_spec))
# How to apply UDF with bounded window, need spark3+
## https://github.com/hanhanwu/Hanhan-Spark-Python/blob/master/Spark3%2B/spark_window.ipynb


# Add index to spark dataframe
df = df.select('*').withColumn('rid', row_number().over(Window.orderBy(monotonically_increasing_id())))


# Plot multiple lines 
import matplotlib.pyplot as plt
def plot_lines(df, xlabel, ylabel):
  plt.figure(figsize=(15,7))
  ax = plt.gca()
  ax.xaxis.set_major_locator(MaxNLocator(integer=True))  # make xticks as integers

  ax.plot(list(df.select('rid').toPandas()['rid']), 
          list(df.select('col1').toPandas()['col1']), label='col1', color='k')
  ax.plot(list(df.select('rid').toPandas()['rid']), 
          list(df.select('col2').toPandas()['col2']), label='col2', color='r', marker='*')
  ax.plot(list(df.select('rid').toPandas()['rid']), 
          list(df.select('col3').toPandas()['col3']), color='grey', label='col3', linestyle='--')  # define line style 

  plt.xticks(rotation='30', horizontalalignment="right")
  plt.legend()
  plt.xlabel=xlabel
  plt.ylabel=ylabel
  plt.title('plot multiple lines')
  display(ax)

    
 # Plot kernal density as a line
import seaborn as sns
sns.set(color_codes=True)
%matplotlib inline

plt.figure(figsize=(15,7))
ax = plt.gca()
sns.kdeplot(list(df.select(col).toPandas()[col]), label="col", color='green')
plt.legend()
plt.title('Distribution of Col')
display(ax)
