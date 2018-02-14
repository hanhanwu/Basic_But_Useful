# With python pandas, dataframe can also do queries

# select 10% sample from each group
grouped_all_data = all_data.groupby(['col1', 'col2'])
sample_data = grouped_all_data.apply(lambda x:x.sample(frac=0.1))  # apply is like udf, but can be used on rows or columns


# use apply on each column
## divide 15% to 85% into bin_num-2 groups, 15-% as a group, 85+% as a group
def create_feature_bins(feature_values):  
    bin_num=7  # Change bin_num here if necessary
    value15 = np.percentile(feature_values, 15)  # python percentile, get the value at 15%
    value85 = np.percentile(feature_values, 85)
    bins = []
    min_value = min(feature_values)
    max_value = max(feature_values)
    bins.append([min_value,value15])
    
    interval = (value85 - value15)/(bin_num-2)
    last_max = value15
    for i in range(bin_num-2):
        current_min = last_max
        if i == bin_num-3:
            current_max = value85
        else:
            current_max = current_min + interval
        bins.append([current_min, current_max])
        last_max = current_max
    
    bins.append([value85, max_value])
    return bins

test_bins = num_cols.apply(lambda col: create_feature_bins(col)) # apply the function on each bin


# apply user defined function on each column in each group
from statistics import mean, median, pstdev

def dist_scaled_manhattan(group_values):
    mdn = group_values.median()
    result = sum(abs(group_values-mdn))/(len(group_values)-1)  # with transform, this will use each individual value in a group to subtract the median of the group
    return result

sub_df = sub_df.set_index('myid')
dist_grouped_df = sub_df.groupby(level='myid').transform(dist_scaled_manhattan)
dist_grouped_df = dist_grouped_df.drop_duplicates()
print(dist_grouped_df.shape)



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


# select multiple non-continuous columns
my_csv = pd.read_csv(csv_path)
cols_idx = [7,9]
cols_idx.extend(range(77,99))
selected_cols = my_csv.iloc[:,cols_idx]


# count records in each group, sort by counts
## in this case, group by food_name, count the records in each food_name, 
## finally select food_names that have [20, 30) records
df_count = selected_features[['food_name', 'flavor']]\
          .groupby(['food_name'])['flavor']\
          .agg(['count'])\
          .sort_values(['count'], ascending=False)
selected_sample = df_count[(df_count['count'] >= 20) & (df_count['count'] < 30)]
selected_sample
selected_foodnames = selected_sample.index.values  # food_name has become the index value
print(selected_foodnames)


# plot 2 groups of data
idx_control = 7  # change this to check a specific food_name
ct = 0

for sample_foodname in selected_foodnames:
    icecream_rows = df[(df['food_name'] == sample_foodname) & 
                                         (df['category'] == 'Ice-cream')].iloc[:,2:]
    chocolate_rows = df[(df['food_name'] == sample_foodname) & 
                                         (df['category'] == 'Chocolate')].iloc[:,2:]
    icecream_lsts = icecream_rows.values.tolist()
    chocolate_lsts = chocolate_rows.values.tolist()
    
    if ct == idx_control:
        print(sample_foodname)
        print(icecream_rows.columns.values)
        
        ct1, ct2 = 0, 0
        plt.figure(figsize=(9,7))
        for icecream_lst in icecream_lsts:
            if ct1 == 0:
                plt.plot(icecream_lst, '-o', label="Ice-cream", color='green')
            else:
                plt.plot(icecream_lst, '-o', color='green')
            ct1 += 1
        for chocolate_lst in chocolate_lsts:
            if ct2 == 0:
                plt.plot(chocolate_lst, '-o', label="Chocolate", color='pink')
            else:
                plt.plot(chocolate_lst, '-o', color='pink')
            ct2 += 1
        plt.legend()
        break
    ct += 1
    

# Plot to compare a row of data and its previous 10 rows
idx_control = 0
ct = 0

for sample_foodname in selected_foodnames:
    if ct == idx_control:
        print(sample_foodname)
        icecream_rows = df[(df['food_name'] == sample_foodname) & 
                                         (df['food_name'] == 'Ice-cream')].iloc[:,2:]
        icecream_idx_lst = icecream_rows.index.values  # get index of icecream rows
        print(icecream_idx_lst)
        
        tmp_ct = 0
        target_idx = 0  # change this value if want to check a specific icecream row
        for icecream_idx in icecream_idx_lst:
            if target_idx == tmp_ct:
                previous10_lst = []
                for i in list(reversed(range(1,11))):  # previous 10 rows
                    previous10_lst.append(df.iloc[icecream_idx-i,2:].values.tolist())

                icecream_lst = df.iloc[icecream_idx,2:].values.tolist()
                
                ct1 = 0
                plt.figure(figsize=(9,7))
                for pre_lst in previous10_lst:
                    if ct1 == 0:
                        plt.plot(pre_lst, '-o', label="Pre10", color='green')
                    else:
                        plt.plot(pre_lst, '-o', color='green')
                    ct1 += 1
                plt.plot(icecream_lst, '-o', label="Ice-cream", color='pink')
                plt.legend()
                if tmp_ct == target_idx:
                    break
            tmp_ct += 1
        break
    ct += 1
