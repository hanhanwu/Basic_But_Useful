# Ignore warnings
import warnings
warnings.filterwarnings("ignore")

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
>>> ua_string = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.104 Safari/537.36'
>>> import re
>>> lst = [elem.strip() for elem in re.split('[()]',ua_string)]
>>> lst
['Mozilla/5.0', 'Macintosh; Intel Mac OS X 10_9_4', 'AppleWebKit/537.36', 'KHTML, like Gecko', 'Chrome/41.0.2272.104 Safari/537.36']
