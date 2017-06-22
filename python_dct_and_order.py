# Python dictionary is randomly ordered
# 1. arrange keys in a dictionary in order
# 2. make a dictionary arranged in key order


# 1. arrange keys in a dictionary in order

from collections import OrderedDict
rich_dct[file_name] = OrderedDict([("Text Length", 0), ("Nouns", {"List":[], "Average SO":0}),
                                                   ("Verbs", {"List":[], "Average SO":0}),
                                                   ("Adjectives", {"List":[], "Average SO":0}),
                                                   ("Adverbs", {"List":[], "Average SO":0}), ("SO by Sentence",[]),
                                                   ("Total SO", 0)])
# Then just assign value to rich_dct like normal dictionary


# 2. make a dictionary arranged in key order
sorted_dict = OrderedDict(sorted(rich_dct.items(), key=lambda t: t[0]))
with open(richout_output, 'w') as richout:
    json.dump(sorted_dict, richout)

    
# 3. Python2 only, output a dictionary arranged in key order
for k, v in dct.iteritems:
  print k,v
