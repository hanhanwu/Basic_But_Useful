# The file include those functions having different names as other programming languages, but serve for the same purpose

# replace, trim
df$Runtime <- gsub(" ", "", df$Runtime)  # trim the empty space
df$Runtime <- gsub(",", "", df$Runtime)  # replace ',' with ''
df$Genre<- gsub(",.*", "", df$Genre)     # Only use the first element before ','


# concatecate strings
'%&%' <- function(x, y)paste0(x,y)
x_path <- "/html/body/div[1]/div/div[4]/div[3]/div[1]/div/div/div[3]/div[" %&% rk %&% "]/div[3]/p[1]/span[1]"


# check whether a substring is in the string
grepl("min", df$Certificate) == T


# R percentile
boxplot(raw_data$mkeystrokeratemsrepeat)
quantile(raw_data$mkeystrokeratemsrepeat)
quantile(raw_data$mkeystrokeratemsrepeat, c(.0, .01, .05, .15, .25, .50,  .75, .80, .85, .90, .99))

# check data types of a data frame or data table
sapply(train, typeof)
