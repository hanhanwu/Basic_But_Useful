"""
Useful links:

* PySpark Window functions: https://medium.com/expedia-group-tech/deep-dive-into-apache-spark-window-functions-7b4e39ad3c86
* Specify spark session: https://github.com/hanhanwu/Hanhan-Spark-Python/blob/master/Spark2.0/how_to_define_spark.py

"""


import pandas as pd
import numpy as np
from pyspark_dist_explore import hist
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

from pyspark.sql.functions import desc, row_number, monotonically_increasing_id, udf, sum, count, round, col, greatest
from pyspark.sql.window import Window
from pyspark.sql.types import IntegerType, StringType, DoubleType


# write and load parquet
## Better to reorder the data when reading, since the partition might changed the order, do this especially when you need to convert spark DF to pandas DF...
# write the data, overwrite if exists
# !!! Different format beyond parquet: https://spark.apache.org/docs/latest/sql-data-sources-load-save-functions.html
df.write.mode('overwrite').parquet(out_dir + 'input_df.parquet')
# read the data
out_dir = '/dbfs/mnt/outputs/'
input_file = out_dir + 'input_df.parquet'
df_input = spark.read.parquet(input_file).orderBy(['rid', 'col1']).cache()


# When using where to find matched list, when there is data type mismatch
## Changing dataframe data type won't work, you have to change the datatype on the right side of the filtering
from pyspark.sql.functions import array, lit
df_rules.where(df_rules.consequent == array(lit(1L)))


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


# Add index to spark dataframe
df = df.select('*').withColumn('rid', row_number().over(Window.orderBy(monotonically_increasing_id())))


# Plot multiple lines 
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
