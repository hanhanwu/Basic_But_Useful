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
