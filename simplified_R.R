# If there are existing libraries or functions, just use them

# count each categorical value in a column
## similar to python pandas value_counts()
library(plyr)
count(dt, 'col')  # dt is a data.table

# set path on windows
path <- "C:/Users/your_name/Desktop/"
