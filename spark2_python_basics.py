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
