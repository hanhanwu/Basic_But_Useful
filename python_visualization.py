# Some tricks in using matplotlib: https://www.analyticsvidhya.com/blog/2020/05/10-matplotlib-tricks-data-visualization-python/?utm_source=feedburner&utm_medium=email&utm_campaign=Feed%3A+AnalyticsVidhya+%28Analytics+Vidhya%29
## You can create watermark with tricks here

# Time series plot
## Using ployly: https://nbviewer.jupyter.org/github/hanhanwu/Hanhan_Data_Science_Practice/blob/5b5c1f45383b405a894b57cee496d2b7a2655bad/sequencial_analysis/try_prophet.ipynb
## Using matplotlib: https://github.com/hanhanwu/Hanhan_Break_the_Limits/blob/master/Bank_Fantasy/Golden_Bridge/adjustable_forecasting.ipynb


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
