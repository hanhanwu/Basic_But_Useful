# Some tricks in using matplotlib: https://www.analyticsvidhya.com/blog/2020/05/10-matplotlib-tricks-data-visualization-python/?utm_source=feedburner&utm_medium=email&utm_campaign=Feed%3A+AnalyticsVidhya+%28Analytics+Vidhya%29
## You can create watermark with tricks here

# Time series plot
## Using matplotlib: https://github.com/hanhanwu/Hanhan_Break_the_Limits/blob/master/Bank_Fantasy/Golden_Bridge/adjustable_forecasting.ipynb

# Change bar chart to lollipop chart
## https://www.analyticsvidhya.com/blog/2021/06/lollipop-charts-advanced-data-visualization-in-python/?utm_source=feedburner&utm_medium=email&utm_campaign=Feed%3A+AnalyticsVidhya+%28Analytics+Vidhya%29

# Plotly charts: https://www.analyticsvidhya.com/blog/2021/12/12-data-plot-types-for-visualization/?utm_source=feedburner&utm_medium=email
  ## Different bar charts, line charts, pie charts, box plot, spline plot, radar chart, pictogram graph, bubble chart, scatter plot, histogram
# Plotly charts: https://www.analyticsvidhya.com/blog/2021/06/tricks-for-data-visualization-plotly-library/?utm_source=feedburner&utm_medium=email&utm_campaign=Feed%3A+AnalyticsVidhya+%28Analytics+Vidhya%29
  ## Stacked Histogram; Funnel Chart
# Plotly interactive charts: https://www.analyticsvidhya.com/blog/2021/07/interactive-data-visualization-plots-with-plotly-and-cufflinks/?utm_source=feedburner&utm_medium=email&utm_campaign=Feed%3A+AnalyticsVidhya+%28Analytics+Vidhya%29

# Altair, a library can create interactive plots too: https://www.analyticsvidhya.com/blog/2021/10/exploring-data-visualization-in-altair-an-interesting-alternative-to-seaborn/?utm_source=feedburner&utm_medium=email&utm_campaign=Feed%3A+AnalyticsVidhya+%28Analytics+Vidhya%29

# Cute charts plot (really cute)
## https://www.analyticsvidhya.com/blog/2021/09/hand-made-visualizations-in-python-using-cutecharts-library/?utm_source=feedburner&utm_medium=email&utm_campaign=Feed%3A+AnalyticsVidhya+%28Analytics+Vidhya%29

# Subplots using `plt.subplot(411)`
def plot_ts_outliers(ts, title, outliers, decomp='additive'):
    outliers_x = [str(outlier).split()[0] for outlier in outliers[0]]
    outliers_y = ts.iloc[ts.index.isin(outliers_x)]
    
    plt.figure(figsize=(20,10))
    plt.subplot(411)
    fig = plt.plot(ts, label='original ts', color='blue')
    plt.scatter(outliers_x, outliers_y, c='red', marker='*')
    plt.legend(loc='best')
    
    plt.subplot(412)
    decomposition = seasonal_decompose(ts, model=decomp)
    residual = decomposition.resid
    fig = plt.plot(residual, label='residuals', color='purple')
    outliers_y_res = residual.iloc[residual.index.isin(outliers_x)]
    plt.scatter(outliers_x, outliers_y_res, c='red', marker='*')
    plt.legend(loc='best')
    
    plt.title(title)
    plt.tight_layout()
    plt.show()
    
    
# Subplots using ax
fig, ax = plt.subplots(figsize=(25,8), nrows=1, ncols=2)
df1.reset_index().plot(x='Date', y='Daily_Sales', ax=ax[0], color='orange', marker='o', label='original ts')
df2.plot(x='time', y='y_0', ax= ax[0], color='green', label='outlier removed ts')
ax[0].set_title("Outliers Removed Subset: No interpolation")

df1.reset_index().plot(x='Date', y='Daily_Sales', ax=ax[1], color='orange', marker='o', label='original ts')
df3.plot(x = 'time',y = 'y_0', ax= ax[1], color='green', label='outlier interpolated ts')
ax[1].set_title("Outliers Removed Subset: With interpolation")
plt.show()



# Control subsets, different plot types per row
def plot_multi_subplots(df, feature_lst):
  
  for feature in feature_lst:
    f, ax = plt.subplots(1,3,figsize=(40,5))  # `subplots()` adds a new sub, first 2 params are the number of rows, cols within the sub
    ax1, ax2, ax3 = ax[0], ax[1], ax[2]
    
    ax1.plot(df.index, df[col1], 
            label=col1, color='brown', marker='*')
    ax1.plot(df.index, np.zeros(len(df.index)), color='grey', linestyle='--')
    ax1.set_xticklabels(df.index, rotation='30', fontsize=10, horizontalalignment="right")
    ax1.set_xlabel(feature)
    ax1.set_ylabel('y_label')

    ax2.bar(df.index, df[col2], 
            label=f'{feature} bar plot', color='orange')
    ax2.set_xticklabels(df.index, rotation='30', fontsize=10, horizontalalignment="right")
    ax2.set_xlabel(feature)
    ax2.set_ylabel('y_label')

    ax3.plot(df.index, df[col3], 
            label=f'{feature}', color='purple', marker='*')
    ax3.plot(df.index, np.zeros(len(df.index)), color='grey', linestyle='--')
    ax3.set_xticklabels(df.index, rotation='30', fontsize=10, horizontalalignment="right")
    ax3.set_xlabel(feature)
    ax3.set_ylabel('y_label')

    
# Plot multiple lines
def plot_lines(lines_dct, col, title, x_axis, y_axis):
  plt.figure(figsize=(15,7))
  ax = plt.gca()
  ax.xaxis.set_major_locator(MaxNLocator(integer=True))
  
  for label, df_dct in lines_dct.items():
    df = df_dct['df']
    ax.plot(list(df.select('rid').toPandas()['rid']), 
            list(df.select(col).toPandas()[col]), label=label, color=df_dct['color'], linestyle=df_dct['linestyle'], marker=df_dct['marker'])
    
  leg = plt.legend()
  leg.get_frame().set_alpha(0.7)  # set legend's transparency
  plt.xlabel(x_axis)
  plt.ylabel(y_axis)
  plt.title(title)
  display(ax)
  
lines_dct = {'line1': {'df': df1, 'linestyle':None, 'marker':None, 'color':'black'},
            'line2': {'df': df2, 'linestyle':'--', 'marker':'*', 'color':'brown'},
            'line3': {'df': df3, 'linestyle':None, 'marker':None, 'color':'pink'}}
plot_lines(lines_dct, col='col1', title='multiple lines')


# plot line with anchor text and annotate text
def plot_performance_lst(performance_lst, y_label, title):
    plt.figure(figsize=(15,7))
    ax = plt.gca()
    ax.set_ylim([0, 1]) # set y-axis range
    
    x = [i+1 for i in range(len(performance_lst))]
    y = performance_lst
    
    ax.plot(x, y, color='g')
    
    # anchor text to show text in the plot
    anchored_text = AnchoredText(f'Average {y_label} is {round(np.mean(performance_lst), 4)}', loc=3, prop={'size': 12})  # the location code: https://matplotlib.org/3.1.0/api/offsetbox_api.html
    ax.add_artist(anchored_text)  
    
    # annotate y_value along the line
    for i,j in zip(x,y):
        ax.annotate(str(round(j, 4)),xy=(i,j))  
    
    plt.xlabel('epoch #')
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()


# plot multiple lines in each subplot
df_lst = [df1, df2, df3]
title_lst = ['t1', 't2', 't3']

fig = plt.figure(figsize=(25,13))
plt.title('Multiple Lines', fontsize=12)
plt.xticks([])

for i in range(len(df_lst)):
  ax=fig.add_subplot(2,2,i+1)
  df = df_lst[i]
  ax.plot(df['col'], df['col1'], label='col1', color='purple')
  ax.plot(df['col'], df['col2'], label='col2', color='red')
  ax.plot(df['col'], df['col3'], label='col3', color='g')
  # ax.plot(df['BRAND'], df['baseline_forecast'], label='FORECAST Without Apply CUT', color='grey', linestyle='--')
  ax.legend()
  ax.set_xticklabels(df['col'].values, rotation='30', fontsize=10, horizontalalignment="right")
  plt.title(title_lst[i] + ' Plot', fontsize=10)
  
display(fig)


# Plot a line and thresholds
plt.figure(figsize=(25,7))
ax = plt.gca()

upper_threshold = 100
lower_threshold = -100

ax.plot(df['x'].values, [upper_threshold]*len(df['x'].values), color='grey', linestyle='--')
ax.plot(df['x'].values, df['y'].values, label='y', color='purple', marker='o')
ax.plot(df['x'].values, [lower_threshold]*len(df['x'].values), color='grey', linestyle='--')

for i, v in enumerate(bias_df['median_bias'].values):
    ax.text(x=bias_df['type'].values[i], y=v, s=str(round(v, 4)), ha="right", va="top", color='green')

leg = plt.legend()
plt.title('Median Biad for Different Forecasting Target')
plt.xticks(fontsize = 12)
plt.ylabel('bias value')
display(ax)


# Plot kernel dentisy per segment (seaborn >= 0.11.2)
## without setting `kind` it can show both kde and histogram
sns.set(font_scale=7)
fig = sns.displot(sales_df, x='x_col', hue='hue_col', kind='kde', 
                  height=25, aspect=7, linewidth = 7.5, palette='tab10')


# Plot kernel density
import seaborn as sns
sns.set(color_codes=True)

fig = plt.figure(figsize=(15,5))
sns.kdeplot(df['col1'], label="col1", color='green')
sns.kdeplot(df['col2'], label="col2", color='orange')
plt.legend()
plt.title('kernel density')
plt.xlabel('x')
plt.ylabel('Perct')
display(fig)


# Single time series plot
ts_df.plot(x='Date', y='Daily_Sales', figsize=(22,5), color='g')
plt.ylabel('Daily Sales')

# Plot time series line charts
import matplotlib.pyplot as plt
import seaborn as sns

def ts_plot_ip_yfixed(data, ip_lst):
    plt.figure(figsize=(15,4))
    axes = plt.gca()
    axes.set_ylim([0, 1]) # set y-axis range if needs to be fixed
    
    for ip in ip_lst:
        _data = data[data["ip"] == ip].sort_values(by="requesttime")
        std = round(volatility_df.loc[(volatility_df['ip']==ip)]['prediction_prob_std'].values[0], 4)
        sns.lineplot(x=_data["requesttime"], y=_data["prediction_prob"], label=ip + ' (std=' +str(std) + ')')

# Bar chart for segments, with y value on the top of the bar
## make sure matplotlib>=3.4.2
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(15, 7))
ax=sns.barplot(x='x', hue='kind', y='count', data=df)
for container in ax.containers:  # put y value on top of the bar
    ax.bar_label(container)
plt.show()

# Bar Chart
import numpy as np
import matplotlib.pyplot as plt

axes = plt.gca()
axes.set_xlim([xmin,xmax]) # set x-axis range
axes.set_ylim([ymin,ymax]) # set y-axis range
x_values = ['A', 'B', 'C', 'D']
x_pos = np.arange(len(x_values))
y_values = [10, 20, 30, 40]
plt.bar(x_pos, y_values, align='center', alpha=0.5)
plt.xticks(x_pos, x_values, rotation='30', fontsize=14, horizontalalignment="right")
plt.ylabel('Y')
plt.title('Edit Your Title')
plt.show()

# Bar chart to show each x value with specified colors
plot_df = pd.DataFrame(oao_df['isfraud'].value_counts(), index=[0,1])
plot_df.reset_index(level=0, inplace=True)
plot_df.columns = ['class', 'count']
## plot_df looks like
# 	class	count
# 0	0	43381
# 1	1	743

ind = np.arange(2) 
width = 1

plt.bar(ind-width, plot_df.iloc[0].values, width/2, label='non-Fraud', color='green')
plt.bar(ind, plot_df.iloc[1].values, width/2,label='Fraud', color='red')

plt.ylabel('Count')
plt.xlabel('Class')
plt.title('Label Distribution')

axes = plt.gca()
rects = axes.patches

plt.xticks(ind, (0, 1))
plt.legend(loc='best')
plt.show()


# Bar chart with y values above the bar
import numpy as np
import matplotlib.pyplot as plt

axes = plt.gca()
axes.set_xlim([-1,9]) # set x-axis range
axes.set_ylim([0,112]) # set y-axis range
x_values = ['1%', '5%', '10%', '25%', '50%', '75%', '90%', '95%', '99%']
x_pos = np.arange(len(x_values))
y_values = [0.34305317324185200, 1.09289617486338700, 2.12765957446808500, 8.33333333333333300,
            25.00000000000000000, 50.00000000000000000, 50.00000000000000000, 50.00000000000000000,
            100.00000000000000000]
plt.bar(x_pos, y_values, align='center', alpha=0.6)
plt.xticks(x_pos, x_values)
plt.xlabel('Percentile')
plt.ylabel('Change Frequency')
plt.title('bi_flash_flag')

rects = axes.patches

for rect, label in zip(rects, y_values):
    height = rect.get_height()
    axes.text(rect.get_x() + rect.get_width() / 2, height, str(round(label, 2))+'%',
            ha='center', va='bottom')
plt.show()


# Horizontal Bar chat
import numpy as np
import matplotlib.pyplot as plt

imp_df = pd.DataFrame(agg_shap_values[idx]).T
imp_df.columns = agg_X_test.columns

plt.figure(figsize=(15,7))
y_values = imp_df.columns
y_pos = np.arange(len(y_values))
x_values = abs(imp_df.values[0])
plt.barh(y_pos, x_values, align='center', alpha=0.7, color='r')
plt.yticks(y_pos, y_values, rotation='30', fontsize=14, horizontalalignment="right")
plt.xlabel('Feature Importance')
plt.title('Feature Importance')
plt.show()


# Change figure size
import matplotlib.pyplot as plt
plt.figure(figsize=(3,4))


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

            
# Plot multiple histogram
from matplotlib import pylab as plt
from matplotlib.offsetbox import AnchoredText
plt.rcParams.update({'font.size': 20})

features = feature_df.columns
print(len(features))
n_rows = 4
n_cols = 4

i = 0
fig=plt.figure(figsize=(40,40))
for feature in features:
    if feature == 'id' or feature == 'label':
        continue
    i += 1
    ax=fig.add_subplot(n_rows,n_cols,i) 
    bins = np.linspace(min(feature_df[feature]), max(feature_df[feature]), 100)
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    plt.hist(fraud_df[feature],
                bins, alpha=0.75, label='FRAUD', color = 'r', edgecolor = 'k', weights=np.zeros_like(fraud_df[feature]) + 1. / fraud_df[feature].shape[0])
    plt.hist(nonfraud_df[feature],
                bins, alpha=0.5, label='NON-FRAUD', color = 'b', edgecolor = 'k', weights=np.zeros_like(nonfraud_df[feature]) + 1. / nonfraud_df[feature].shape[0])
    plt.legend(loc='best', prop={'size': 20})
    plt.title('Feature: ' + feature)
    plt.xlabel('Feature Values')
    plt.ylabel('Percentage')
    anchored_text = AnchoredText('Here to put the text', loc=7, prop={'size': 20})  # the location code: https://matplotlib.org/3.1.0/api/offsetbox_api.html
    ax.add_artist(anchored_text)
fig.tight_layout()
plt.show()


# plot multiple scatter plot
from matplotlib import pylab as plt

n_rows = 4
n_cols = 3
y = 'Item_Outlet_Sales'

def multi_scatter_plot(n_rows, n_cols, sample_data, y):
    area = np.pi*3
    colors = (0,0,0)

    i = 0
    fig=plt.figure(figsize=(40,40))
    for feature in sample_data.columns:
        i += 1
        ax=fig.add_subplot(n_rows,n_cols,i)

        plt.scatter(sample_data[feature], sample_data[y], s=area, c=colors, alpha=0.5)
        plt.title('Feature & Label Relationships', fontsize=30)
        plt.xlabel(feature, fontsize=30)
        plt.ylabel(y, fontsize=30)
    fig.tight_layout()
    plt.show()
    
multi_scatter_plot(n_rows, n_cols, sample_data, y)


# multiple plot by specifiying the matrix dimensions
## Plot each class in different color when you have 2D (x,y) values
from matplotlib import pyplot
from sklearn.datasets import make_circles
from numpy import where

def scatter_plot_circles_problem(n_samples, noise_value=0.1):
    # generate circles
    X, y = make_circles(n_samples=n_samples, noise=noise_value, random_state=1)
    # select indices of points with each class label
    zero_ix, one_ix = where(y == 0), where(y == 1)  # get the index list of each class
    # points for class zero
    pyplot.scatter(X[zero_ix, 0], X[zero_ix, 1], color='red')
    # points for class one
    pyplot.scatter(X[one_ix, 0], X[one_ix, 1], color='blue')
            
values = [50, 100, 500, 1000]
for i in range(len(values)):
    value = 220 + (i+1)  # 220 here means 2x2 matrix
    pyplot.subplot(value)
    scatter_plot_circles_problem(values[i])
pyplot.show()


# Show kernel density distribution, calculate K-L score to show difference between the 2 probability distributions
import numpy as np
from scipy.stats import gaussian_kde
from scipy.stats import entropy
import seaborn as sns
from matplotlib import pylab as plt
sns.set(color_codes=True)
sns.set(style="ticks", rc={"lines.linewidth": 0.7})  # set linewidth
sns.set(font_scale=1.5)
sns.set_style("whitegrid")  # add grid in the plot

def calc_kl_score(x1, x2):
    """
    Fits a gaussian distribution to x1 and x2 and calculates the K-L score
    between x1 and x2.
     
    :param x1: list. Contains float / integers representing a feature.
    :param x2: list. Contains float / integers representing a different feature.
    :return float
    """
    positions = np.linspace(0,1,1000) # (Optional) If plotting, you can increase this number to generate a smoother KDE plot
    kernel = gaussian_kde(x1)
    values_prod = kernel(positions)
    kernel = gaussian_kde(x2)
    values_dev = kernel(positions)
    return entropy(values_dev,values_prod)

features = df1.columns
print(len(features))
n_rows = 2
n_cols = 4

i = 0
fig=plt.figure(figsize=(20,10))
for feature in features:
    if feature == 'id':
        continue
    i += 1
    ax=fig.add_subplot(n_rows,n_cols,i) 
    bins = np.linspace(min(df2[feature]), max(df2[feature]), 100)
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    sns.histplot(df1.loc[df1[feature].isnull()==False][feature], color='green', label='df1')
    sns.histplot(df2.loc[df2[feature].isnull()==False][feature], color='purple', label='df2')
    kl_score = calc_kl_score(df1.loc[df1[feature].isnull()==False][feature],
             df2.loc[df2[feature].isnull()==False][feature])
    plt.legend(loc='best', fontsize=25))
    plt.title('Feature: ' + feature + ', K-L Score:' + str(round(kl_score, 4)), fontsize=25))
    plt.xlabel('Feature Values', fontsize=25))
    plt.ylabel('Percentage', fontsize=25))
fig.tight_layout()
plt.show()
