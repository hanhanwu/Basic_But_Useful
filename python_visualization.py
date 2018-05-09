
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
plt.xticks(x_pos, x_values)
plt.ylabel('Y')
plt.title('Edit Your Title')
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


# Change fiture size
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
