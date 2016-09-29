# convert the data.frame/list into data.table
library(data.table)
require(data.table)
setDT(q1)

## NOTE: when R studio has started a new session, all the generated data may still there, but the previous data.table (q1 here) may become
## data.frame/list again, need to re-run the code above
