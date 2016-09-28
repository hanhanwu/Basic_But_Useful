## q1 is the original data.frame here


# convert the data.frame/list into data.table
library(data.table)
require(data.table)
setDT(q1)


library(mlr)
summarizeColumns(q1)

##SEPERATE DATA COLUMNS BASED ON DATA TYPE
# find all factor columns generate fact_data that stores all these factor columns
mark_fact_cols <- sapply(q1, is.factor)
table(mark_fact_cols)
factcols <- c()
fact_ct <- 1

for (i in names(mark_fact_cols)) {
  mk <- mark_fact_cols[[i]]
  if (mk == TRUE) {
    factcols[[fact_ct]] <- i
    fact_ct <- fact_ct + 1
  }
}

fact_data <- q1[, factcols, with=F]
dim(fact_data)
str(fact_data)



### Or, collect both factor columns and numeric & interger columns at the same time
##SEPERATE DATA COLUMNS BASED ON DATA TYPE
# find all factor columns generate fact_data that stores all these factor columns, other columns (numeric or integer columns) go to another list
mark_fact_cols <- sapply(q1, is.factor)
table(mark_fact_cols)
factcols <- c()
numcols <- c()
fact_ct <- 1
num_ct <- 1

for (i in names(mark_fact_cols)) {
  mk <- mark_fact_cols[[i]]
  if (mk == TRUE) {
    factcols[[fact_ct]] <- i
    fact_ct <- fact_ct + 1
  }
  else {
    numcols[[num_ct]] <- i
    num_ct <- num_ct + 1
  }
}

fact_data <- q1[, factcols, with=F]
dim(fact_data)
str(fact_data)

num_data <- q1[, numcols, with=F]
dim(num_data)
str(num_data)
