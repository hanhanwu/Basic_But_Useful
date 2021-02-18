"""
Useful links:

PySpark Window functions: https://medium.com/expedia-group-tech/deep-dive-into-apache-spark-window-functions-7b4e39ad3c86

"""


import pandas as pd
import numpy as np
from pyspark_dist_explore import hist
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

from pyspark.sql.functions import desc, row_number, monotonically_increasing_id, udf, sum, count, round, col, greatest
from pyspark.sql.window import Window
from pyspark.sql.types import IntegerType, StringType, DoubleType


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
    result = {'min': np.percentile(col, 0), '1%':np.percentile(col, 1),
             '10%':np.percentile(col, 10), '15%':np.percentile(col, 15),
             '25%':np.percentile(col, 25), '50%':np.percentile(col, 50), '75%':np.percentile(col, 75),
             '85%':np.percentile(col, 85), '95%':np.percentile(col, 95), '99%':np.percentile(col, 99),
              'max':np.percentile(col, 100)}
    return result

# convert a col to pandas list
print(get_percentile(list(df.select('ct').toPandas()['ct'])))


# Apply window function
my_udf = udf(lambda col: 'pink' if has_icecream else 'green', StringType())
df = df.withColumn('col1', my_udf('col'))

win_spec = Window.partitionBy([col2, col3]).orderBy('time').rowsBetween(-2, -1)  # the window is formed by the previous 2 records of the current record
df = df.withColumn('col_new', count('col1').over(win_spec))


# Add index to spark dataframe
df = df.select('*').withColumn('rid', row_number().over(Window.orderBy(monotonically_increasing_id())))


# Plot multiple lines 
def plot_adjusted_targets(df):
  plt.figure(figsize=(15,7))
  ax = plt.gca()
  ax.xaxis.set_major_locator(MaxNLocator(integer=True))  # make xticks as integers


  ax.plot(list(df.select('rid').toPandas()['rid']), 
          list(df.select('col1').toPandas()['col1']), label='col1', color='k')
  ax.plot(list(df.select('rid').toPandas()['rid']), 
          list(df.select('col2').toPandas()[col2']), label='col2', color='r')
  ax.plot(list(df.select('rid').toPandas()['rid']), 
          list(df.select('col3').toPandas()['col3']), color='grey', label='col3', linestyle='--')  # define line style 

  plt.xticks(rotation='30', horizontalalignment="right")
  plt.legend()
  plt.title('plot multiple lines')
  display(ax)
