
# variance, standard deviation, mean, median, etc
from statistics import variance, stdev, mean, median
lst = [1,2,3,4]
my_variance = variance(lst)
my_sd = stdev(lst)
my_mean = mean(lst)
my_median = median(lst)


# normalize a list into [0,1]
## Method 1 - min, max
max_num = max(lst)
min_num = min(lst)
normalized_lst = [(x-min_num)/(max_num-min_num)]

## Method 2 - Normalize to Standard Gaussian Distribution
mean_num = mean(lst)
my_sd = stdev(lst)
normalized_lst = [(x-mean_num)/my_sd for x in lst]


# Compare 2 curves
## Method 1 - Kolmogorov–Smirnov test
from scipy.stats import ks_2samp
from numpy import array

pv = ks_2samp(num_lst1, num_lst2)
# if p-value smaller than the threshold, then reject null hypothesis, which means the 2 curves are not similar
