# Ignore warnings
import warnings
warnings.filterwarnings("ignore")

# json.loads() vs ast.literal_eval()
## json.loads() works better when the nested situation is more complex in a dictionary, 
## ast.literal_eval() sometimes may report an error.

# find common elements in multiple lists
set.intersection(*[set(list) for list in p])

# temporary list append elements in iteration
## I just found something weird with python, that is even if in each iteration, 
## I assigned the original list to the temporary list, and then tried to append new elements in this temporary list,
## its values will be brought to the next iteration. I have to initialize this temporary as empty in each iteration, like this
for i in range(10):
  tmp_lst = []
  tmp_lst.append(elem)
  tmp_lst.extend(origin_lst)

  
# generate all the combinations of list elements
import itertools

lst = ['a', 'b', 'c', 'd']
for L in range(0, len(lst)+1):  # length of the sets
    for subset in itertools.combinations(lst, L):
        print(subset)

# useragent parser
## There is a specific python library for parsing useragent: https://github.com/ua-parser/uap-python
## but I could not get what I want from there, since all what I wanted was to get each element first
## Here's my version:
ua_string = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.104 Safari/537.36'
import re
lst = [elem.strip() for elem in re.split('[()]',ua_string)]
lst
# Output:
['Mozilla/5.0', 'Macintosh; Intel Mac OS X 10_9_4', 'AppleWebKit/537.36', 'KHTML, like Gecko', 'Chrome/41.0.2272.104 Safari/537.36']


# read and show plot color image in IPython
%pylab inline
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('test_plot.png', cv2.IMREAD_COLOR)
plt.figure(figsize = (10,10))
pylab.imshow(img)
pylab.axis('off')
pylab.show()


# Methods to generate random numbers
## `ramdom` lirbary: https://docs.python.org/3/library/random.html
## numpy `random` library: https://docs.scipy.org/doc/numpy-1.14.0/reference/routines.random.html
## Both of them have random number generated from different distributions.
## `random` has choices() which can randomly select multiple numbers from a list, 
### you can also add weights, higer weight higher chance to select that number.
