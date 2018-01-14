# With python pandas, dataframe can also do queries

# select 10% sample from each group
grouped_all_data = all_data.groupby(['col1', 'col2'])
sample_data = grouped_all_data.apply(lambda x:x.sample(frac=0.1))

# save dataframe to csv, without header
sample_data.to_csv('mysample.csv', sep=',', header=0)

# select data with condition
df1 = df.ix[(df['col1']>=777) 
            & (df['col2']<=999) 
            & (df['col3']>=410)]
result = df1.sort_values(['col1'], ascending=[1])[['col1', 'col2', 'col3']]  # finally sort results based on values

# join csv files
df1 = pd.read_csv('csv1')
df2 = pd.read_csv('csv2')
df = pd.merge(df1, df2, on='common_col', how='inner')
selected_cols = df.loc[:, ['col1', 'col2', 'col3']]
selected_cols.to_csv('output_file.csv')

# unique values in 1 column
df1['col1'].unique()

# select the first value in each group
## Here, df1 only has 2 columns (my_id, value), by doing this, you are choosing the first value for each my_id
df = df1.groupby('my_id').first().reset_index()

# Pandas UDF
# Apply the function to a column, to all rows: 
## http://jonathansoma.com/lede/foundations/classes/pandas%20columns%20and%20functions/apply-a-function-to-every-row-in-a-pandas-dataframe/

# Find names of all numerical columns
df.select_dtypes(include=['int64']).columns.tolist()
# Get numerical columns (including data)
df._get_numeric_data()
