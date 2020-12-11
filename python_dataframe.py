# Some quick methods in pandas
## https://www.analyticsvidhya.com/blog/2016/01/12-pandas-techniques-python-data-manipulation/?utm_content=bufferfa8d9&utm_medium=social&utm_source=facebook.com&utm_campaign=buffer
  ### pivot table - generate aggregate results for multiple columns
  ### multi-indexing - using the values of multiple columns as the index to locate
  ### cross-tab - this can be used to check whether a feature affects the label with percentage value
  ### cut - binning
# How to build pivot table with pandas
## https://www.analyticsvidhya.com/blog/2020/03/pivot-table-pandas-python/?utm_source=feedburner&utm_medium=email&utm_campaign=Feed%3A+AnalyticsVidhya+%28Analytics+Vidhya%29

# Pandas 1.0
## https://www.analyticsvidhya.com/blog/2020/01/pandas-version-1-top-4-features/?utm_source=feedburner&utm_medium=email&utm_campaign=Feed%3A+AnalyticsVidhya+%28Analytics+Vidhya%29
### data type "string"
### pd.NA
### data.info (data summary)
### markdown format

# remove the last x records
df = df.head(n-x) # this is faster than drop()


# When data file is huge and python always exit because of the lack of memory, use Dask
## But dask dataframe do not have much functions as pandas dataframe, with `compute()` after loading data, you can use the
## data as pandas dataframe
import dask.dataframe as dd

df = dd.read_csv('my_csv.csv').compute()

# multiprocessing
import multiprocessing as mp
pool = mp.Pool(processes = (mp.cpu_count() - 1))
answer = pool.map(my_function, my_data)
pool.close()
pool.join()

# With python pandas, dataframe can also do queries
# count distinct values in a column
df.col.value_counts()

# Assign value at a cell with specified index & column name
df.at[7, 'col'] = 10

# convert dictionary to dataframe without having index as the dictionary key
my_df = pd.DataFrame.from_dict(my_dct, orient='index', columns=['ct']).reset_index()

# Replace the header with the first row in pandas
new_header = df.iloc[0] #grab the first row for the header
df = df[1:] #take the data less the header row
df.columns = new_header #set the header row as the df header

# COMMONLY USED PREPROCESSING METHODS
df.isnull().sum()  ## check all missing values
df.col1 = df.col1.fillna("MISSING")  # fill NA
df.loc[(df.col1 != 'A') & (df.col1 != '2')\
        & (df.col1 != 'MISSING'), 'col1'] = 'OTHER'  # replace some rows in a column (this method will avoid warnings)
df.loc[df['col'].notnull()]  # select those records with 'col' not null
df.loc[df['col'].isnull()]  # select those records with 'col' is null

# To deal with np.nan related error
df = df.astype(np.float64).replace(np.nan, 'None')

# get days difference from 2 datetime columns
df['days_diff'] = (df['max_time'] - df['min_time']).dt.days
# get hours difference from 2 datetime columns
df['hours_diff'] = (df['max_time'] - df['min_time']).dt.components['hours']

# extract date from datetime string
## check those symbols: https://docs.python.org/2/library/datetime.html
my_date = datetime.datetime.strptime(my_datetime_str, "%Y-%m-%d %H:%M:%S").date()
## extract year_month
df['month'] = df['my_datetime'].apply(lambda v: v.to_period('M'))
## extract date from datetime
df['date'] = sample_df['my_datetime'].dt.date

# count duplicated rows
df.duplicated().sum()
# count duplicated rows based on s subset of columns
df.duplicated(subset=['col1', 'col2', 'col3']).sum()
# drop all duplicates, set keep=False
df.drop_duplicates(subset=['col1', 'col2', 'col3'], keep=False, inplace=True)

# min max scaler and skip NULL
for col in df.columns:
    df[col] = df[col].sub(df[col].min()).div((df[col].max() - df[col].min()))

# get 99 percentile value of each column
high = 0.99
quant_df = filt_df.quantile([high])
quant_df2.index = [0.99]
quant_df
# set min, max value based on condition
for col in df.columns:
    if col == 'id' or col == 'label':
        continue
    df.loc[df[col] > quant_df[col].values[0], col] = quant_df[col].values[0] # larger than 99 percentile
    df.loc[df[col] < 0, col] = 0 # negative value
        
# a fast way to get distribution for a list of values
pd.Series(my_lst).describe()  # but this one may not return the all percentile you want
## to get a certain percentile from a list
pd.Series(my_lst).quantile(q=0.9)  # 90th percentile

# drop highly correlated features
import numpy as np
## Create correlation matrix
corr_matrix = df.corr().abs()
## Select upper triangle of correlation matrix
upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(np.bool))
## Find features with correlation greater than 0.95
to_drop = [column for column in upper.columns if any(upper[column] > 0.95)]
## Drop features 
df.drop(df.columns[to_drop], axis=1)

# convert dataframe to numpy 2D array
X_train = X_train.as_matrix()

# replace numpy nan to None
df['col] = df['col].replace({np.nan:None})

# select 10% sample from each group
grouped_all_data = all_data.groupby(['col1', 'col2'])
sample_data = grouped_all_data.apply(lambda x:x.sample(frac=0.1))  # apply is like udf, but can be used on rows or columns

# convert numpy matrix to dataframe
np_df = pd.DataFrame(np_matrix)
np_df.columns = df1.columns ## use existing columns to replace the column names

# convert dictionary to dataframe, without index
## python 3.* needs list(), python 2.* doesn't need list()
feature_importance_df = pd.DataFrame(list(dict(zip(X_train.columns, m.feature_importances_)).items()), 
                                     columns=['Feature', 'Importance'])
feature_importance_df.sort_values('Importance', ascending=False).head(n=10)

# rename df column
df = df.rename(index=str, columns={'old_column_name': 'new_column_name'})
# rename header
df.columns = ['col1', 'col2']

# change column order
df = df[['col7', 'col9', 'col4', 'col10']]

# dictionary to dataframe, transpose the dataframe (reverse row and column)
pd.DataFrame(my_dct).T

# Give index name, and make index the same level as other columns
df.index.name = 'new_idx_name'
df.reset_index(level=0, inplace=True)

# insert pandas dataframe into Redshift (Using AWS S3 copy is much faster for larger files)
## create schema first (psql)
Drop table if exists ngram_metrics_iter1;
create table ngram_metrics_iter1
(col VARCHAR(200), col1 TIMESTAMP, col2 VARCHAR(128), col3 VARCHAR(max));
## python pandas insertion
from sqlalchemy import create_engine
import pandas as pd

read_user_name = "[YOUR USERNAME]"
read_passwd = "[YOUR PASSWORD]"
read_host_name = "[YOUR HOST NAME]"

connection = 'postgresql://' + read_user_name + ':' + read_passwd + '@' + read_host_name + ':[PORT]/[DATABASE NAME]'
engine = create_engine(connection)

df.to_sql('ngram_metrics_iter1', engine, index = False, if_exists = 'append')  # using 'append' you can insert new data
df.to_sql('ngram_metrics_iter1', engine, index = False, if_exists = 'replace') # using 'replace' you can replace the table 

# use apply and assign generated values to another dataframe
df2['col'] = df1.apply(lambda r: my_function(r['col1']), axis=1).values # without "values", you may get NaN

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

# NOTE: When there are nan in the list, np.percentile won't work. Use np.nanpercentile(lst)

# use apply on multiple columns for each row
cols_ct = len(dist_grouped_df.columns)
scored_df = dist_grouped_df.apply(lambda r: cols_ct/sum(r), axis=1)
scored_df.head()


# apply user defined function on each column in each group
## apply() can be used on cols, rows, 
## but if you have operations on each group, use transform
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

# join df through index
joined_df = pd.merge(df1, df2, left_index=True, right_index=True)

# find columns in df1 but not in df2
df = pd.merge(df1, df2, on='common_col', how='inner')
df1[~df1['id'].isin(df['id'])]

# join df and keep both duplicated columns
## pandas has merge, join and concat, but only concat can do this, join and merge will just keep 1 column which means,
## for the same columns, you cannot see which has null if one of the column has unique values
## But for columns only exists in one of the dataframe, concat won't keep these columns, join/merge will
## If you don't want to join by index, use "merge" don't use join
## concat will join by index automatically, if you didn't set index, it will use default index in a dataframe. Therefore, also
## need to note, you may need df.set_index(drop=True, inplace=True) before using concat, in case some operation such as
## train-test-split will shuffle the index
joined_df = pd.concat([df1, df2], axis=1)  # what made a differnce is "axis=1" here
## later if you want to join the overlapped columns with null
joined_df.dropna(axis='columns', inplace=True)

# Add a column with specified condition
def add_col(r):
    if pd.isnull(r['rid']):
        val = 'has_null'
    else:
        val = 'no_null'
    return val
df['new_col'] = df.apply(add_col, axis=1)


# list unique values in 1 column
df1['col1'].unique()
## count each unique values in a column
df.groupby('col_you_want2count')['ID'].nunique()


# select the first value in each group
## Here, df1 only has 2 columns (my_id, value), by doing this, you are choosing the first value for each my_id
df = df1.groupby('my_id').first().reset_index()

# rank for group
merchant_weekly_df['weekly_rank'] = merchant_weekly_df.groupby('week_number')['rating'].rank('dense', ascending=False)
# cumlative sum for each group
merchant_weekly_df['cum_rating'] = merchant_weekly_df.groupby(['merchant'])['rating'].cumsum()

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

# with Grouper, no need to reset index in groupby
df['date'] = pd.to_datetime(df['date'])
df.groupby(['name', pd.Grouper(key='date', freq='M')])['ext price'].sum()  # group by name and month
# df.set_index('date').groupby('name')["ext price"].resample("M").sum()  # by comparison
df.groupby([pd.Grouper(key='date', freq='M')])['ext price'].sum()  # group by month

# group by, to form a list of the same group
order_prodlst_df = all_order_train.groupby('order_id')['product_id'].apply(list).reset_index(name='prod_lst')

#group by, count distinct
## in this case, group by food_name, count the number of flavors in each food_name
## if "foodx_name" is a list, needs to use `astype('str')`
## if using agg('count') can guarantee all column names at the same level, but brings in extra index column
df_count = selected_features[['food_name', 'flavor']].astype('str').drop_duplicates()\
          .groupby(['food_name'], as_index=False)['flavor']\
          .agg(['count']).reset_index()\
          .sort_values(['count'], ascending=False)

# better way to do group by, more flexibility, less code
## More examples: https://www.shanelynn.ie/summarising-aggregation-and-grouping-data-in-python-pandas/
agg_rating_df = user_rating_df[['buz_name', 'rating', 'review_count', 'review_sentiment']]\
          .groupby('buz_name', as_index=False)\
          .agg({'rating':'mean', 'review_count':'mean', 'review_sentiment':'mean'})


# count records in each group, sort by counts
## in this case, group by food_name, count the number of flavors in each food_name, 
## finally select food_names that have [20, 30) records
df_count = selected_features[['food_name', 'flavor']]\
          .groupby(['food_name'])['flavor']\
          .agg(['count'])\
          .sort_values(['count'], ascending=False)
selected_sample = df_count[(df_count['count'] >= 20) & (df_count['count'] < 30)]
selected_sample
selected_foodnames = selected_sample.index.values  # food_name has become the index value
print(selected_foodnames)

# you may need to drop level naming so that you can call the column name
df_count = selected_features[['food_name', 'flavor']]\
          .groupby(['food_name'])['flavor']\
          .agg(['count'])
df_count.columns = df_count.columns.droplevel(0)
selected_sample = df_count[(df_count['count'] >= 20) & (df_count['count'] < 30)]

# drop index/column level
## After you used pandas group by, the original columns used for group by will become the index of the new df,
## here's how to make index to the column level
agg_rating_df = user_rating_df[['buz_name', 'review_count', 'rating']]\
          .groupby(['buz_name', 'review_count'])['rating']\
          .agg(['mean'])
agg_rating_df.reset_index(level=['buz_name', 'review_count'], inplace=True)  # reset index to column level
agg_rating_df = agg_rating_df.rename(index=str, columns={'mean': 'avg_rating'})
agg_rating_df.head()

## groupby & transform is easier
# Reference: https://www.analyticsvidhya.com/blog/2020/03/understanding-transform-function-python/?utm_source=feedburner&utm_medium=email&utm_campaign=Feed%3A+AnalyticsVidhya+%28Analytics+Vidhya%29
agg_rating_df = user_rating_df[['buz_name', 'review_count', 'rating']]\
          .groupby(['buz_name', 'review_count'])['rating'].transform('mean')
agg_rating_df.head()


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

    
# Data Explore & Data Preprocessing Methods
## check percentile for each colummn
def get_percentile(col):
    result = {'min': np.percentile(col, 0), '1%':np.percentile(col, 1),
             '5%':np.percentile(col, 5), '15%':np.percentile(col, 15),
             '25%':np.percentile(col, 25), '50%':np.percentile(col, 50), '75%':np.percentile(col, 75),
             '85%':np.percentile(col, 85), '95%':np.percentile(col, 95), '99%':np.percentile(col, 99),
              'max':np.percentile(col, 100)}
    return result
    
df = df.set_index('accountid')
percentile_df = df.apply(get_percentile)  # apply function to all the columns
pd.set_option('max_colwidth', 800)
pd.DataFrame(percentile_df)

### another get percentile function
def get_percentile(df):
    dist_dct = {}
    idx = 0
    
    for col in df.columns:
        tmp_dct = {'col': col, 'min': np.percentile(df[col], 0), '1%':np.percentile(df[col], 1),
             '5%':np.percentile(df[col], 5), '15%':np.percentile(df[col], 15),
             '25%':np.percentile(df[col], 25), '35%':np.percentile(df[col], 35),
            '50%':np.percentile(df[col], 50), '75%':np.percentile(df[col], 75),
             '85%':np.percentile(df[col], 85), '95%':np.percentile(df[col], 95), '99%':np.percentile(df[col], 99),
              'max':np.percentile(df[col], 100)}
        dist_dct[idx] = tmp_dct
        idx += 1
    result = pd.DataFrame(dist_dct).T
    result = result[['col', 'min', '1%', '5%', '15%', '25%', '35%', '50%', '75%', '85%', '95%', '99%', 'max']]
    return result

## Remove values out of percentile range
num_cols = [col for col in df.columns if df[col].dtypes != 'O' 
            and col != 'col1' and col != 'col2']  # select specific columns
filt_df = df[num_cols]
high = 0.99
quant_df = filt_df.quantile([high]) # this df list all the 99% value of each column
quant_df
filt_df = filt_df.apply(lambda x: x[(x < quant_df.loc[high,x.name])], axis=0)
filt_df.shape
filt_df = pd.concat([df.loc[:,'col1'], filt_df], axis=1)  # add col1 back
filt_df.head()
### removed values will become NULL, you can use different methods to drop na
filt_df = filt_df.dropna()  # I tried thresh=16, there are 2601 records with all had > 99% outliers
filt_df.shape


## apply log2 to a column
import math
df['col1'] = df['col2'].apply(math.log, 2)

## put outliers at start and end points, then get percentile
### Here, k is not 1.5, since sometimes, 1.5*IQR can remove too much outliers
def impute_outliers_percentile(col):
    k = 2.0
    q1 = np.percentile(col, 25)
    q3 = np.percentile(col, 75)
    iqr = q3-q1
    new_col = []
    if iqr==0:
        new_col = col  # deal with cols that are close to uniform
    else:
        for e in col:
            if e < 0:  # special case: features here should all >= 0
                new_col.append(0.0)
            elif e >= (q1-k*iqr) and e <= (q3+k*iqr):
                new_col.append(e)
            elif e < (q1-k*iqr):
                new_col.append(q1-k*iqr)
            else:
                new_col.append(q3+k*iqr)
    
    result = {'1%':np.percentile(new_col, 1),
             '5%':np.percentile(new_col, 5), '10%':np.percentile(new_col, 10), '15%':np.percentile(new_col, 15),
             '25%':np.percentile(new_col, 25), '50%':np.percentile(new_col, 50), '75%':np.percentile(new_col, 75),
             '85%':np.percentile(new_col, 85), '95%':np.percentile(new_col, 95), '99%':np.percentile(new_col, 99),
              '100%':np.percentile(new_col, 100)}
    return result
    
df = df.set_index('accountid')
percentile_df = df.apply(impute_outliers_percentile)
pd.set_option('max_colwidth', 800)
pd.DataFrame(percentile_df)

## deal with outliers (put them at the edges), normalize each column into [0,1] range
def impute_outliers(col):
    k = 2.0
    q1 = np.percentile(col, 25)
    q3 = np.percentile(col, 75)
    iqr = q3-q1
    new_col = []
    if iqr==0:
        new_col = col  # deal with cols that are close to uniform
    else:
        for e in col:
            if e < 0:  # special case: features here should all >= 0
                new_col.append(0.0)
            elif e >= (q1-k*iqr) and e <= (q3+k*iqr):
                new_col.append(e)
            elif e < (q1-k*iqr):
                new_col.append(q1-k*iqr)
            else:
                new_col.append(q3+k*iqr)
    return new_col

def normalize_cols(col):
    min_v = min(col)
    max_v = max(col)
    normalized_col = [(v-min_v)/(max_v-min_v) for v in col]
    return normalized_col
# impute outliers
df = df.set_index('accountid')
imputed_df = df.apply(impute_outliers)
# normalize each col into [0,1]
normalized_df = imputed_df.apply(normalize_cols)

## count NA in each column
df.isnull().sum()

## where clause (df here has 1 index, the other column is the value column)
df.where(df >= 410).dropna()
### When you have multiple conditions, using () for each condition is required:
df.where((df >= 77) & (df <= 99)).dropna()
### When you just want to drop rows have NA on specific cols
df.where(df >= 410).dropna(subset=['col1', 'col2'])
### only drop when all rows are NA
df.where(df >= 410).dropna(how='all')

## to filter rows through column condition
df2 = df[df['col'] > 410]

## get rows based on index value
normalized_df.loc['this_is_index_value'].head()

## different distance methods in Scipy
## https://docs.scipy.org/doc/scipy-0.15.1/reference/generated/scipy.spatial.distance.cdist.html
### Here, calculate the distance between individual value in each column and the column median
def get_scaled_dist(group_values, dist_name='cityblock'):
    lst = [[e] for e in group_values]
    mdn = group_values.median()
    dist_sum = sum(distance.cdist(np.array(lst), np.array([[mdn]]), dist_name))[0]
    dist = dist_sum/(len(group_values)-1)
    return dist

dist_name = 'cityblock'
df = df.set_index('accountid')
df = df.groupby(level='id').transform(get_scaled_dist,dist_name)
df = df.drop_duplicates()

# Createa histogram from dataframe or numpy histogram
# Check https://github.com/hanhanwu/Hanhan_Data_Science_Practice/blob/master/Applied_Statistics/thinkstats_chapter2.ipynb


# load Chinese characters
df = pd.read_csv('my_file.csv', encoding="GBK")
