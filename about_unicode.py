# There are so many ways to deal with unicode in python, different situation use different methods.
# I have already tried many methods, however, each time, in different situations, I had to find new solutions again
# Python version, IDE, data source, etc. will all influence the output
# so, I's better reocrd my solutions each time here to save my future time


# Sample 1: <p>...the police investigations into the women\u2019s disappearances,\u201d Mr. Oppal writes.</p>
## I etracted the data from HTML directly, when I used str(), I got these characters: \u201d, \u2019
## This works for me in python 3
import unidecode
text = ["<p>"+str(unidecode.unidecode(t.text))+"</p>" for t in content.findAll('p', {"class":''})]


# Sample 2: could\xe2\x80\x99t  (means couldn't)
import unidecode
word_lst = [str(unidecode.unidecode(w.decode('utf-8'))) for w in text.split()]
