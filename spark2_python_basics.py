# When using where to find matched list, when there is data type mismatch
## Changing dataframe data type won't work, you have to change the datatype on the right side of the filtering
from pyspark.sql.functions import array, lit
df_rules.where(df_rules.consequent == array(lit(1L)))
