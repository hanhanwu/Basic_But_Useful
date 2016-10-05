# convert the data.frame/list into data.table
library(data.table)
require(data.table)
setDT(q1)

## NOTE: when R studio has started a new session, all the generated data may still there, but the previous data.table (q1 here) may become
## data.frame/list again, need to re-run the code above



## SEPERATE NUMERICAL AND CATEGORICAL DATA
fact_data <- subset(q1, select = mark_fact_cols==T)
num_data <- subset( q1, select = mark_fact_cols==F)

summarizeColumns(num_data)
summarizeColumns(fact_data)



################# DATA CLEANING - NUMERIC DATA ########################

## Deal WITH MISSING DATA
table(is.na(num_data))
colSums(is.na(num_data))
num_missing <- sapply(num_data, function(x){sum(is.na(x))/length(x)})*100
num_missing    # only TenureMonth has 0.33% missing data
num_data$TenureMonth[is.na(num_data$TenureMonth)] <- median(num_data$TenureMonth, na.rm = T)   # based on the distribution plot below, median is better here
colSums(is.na(num_data))


## DEAL WITH OUTLIERS, DATA IMBALANCE
library(ggplot2)
install.packages("plotly", type = "source")
library(plotly)

num_distribution_plot <- function(a){
  ggplot(data = num_data, aes(x= a, y=..density..)) + geom_histogram(fill="blue",color="red",alpha = 0.5,bins =100) + geom_density()
  ggplotly()
}


num_distribution_plot(num_data$TenureMonth)
# num_distribution_plot(log(num_data$TenureMonth))
boxplot(num_data$TenureMonth)
length(which(num_data$TenureMonth >= 600))/length(num_data$TenureMonth)*100
num_data[, TenureMonth := ifelse(TenureMonth>=600, median(TenureMonth), TenureMonth)]
boxplot(num_data$TenureMonth)     # replace outliers with median


num_distribution_plot(num_data$MemberShareBalance)
boxplot(num_data$MemberShareBalance)
num_data[,.N,MemberShareBalance][order(-N)]
length(which(num_data$MemberShareBalance >= 7))/length(num_data$MemberShareBalance)*100   # too many individual values
## !!! for numerical data, if converting to factor data still have 10+ levels, 
## bin the numerical data first, then add to other factors data

num_distribution_plot(num_data$TermUnregisteredBalance)
boxplot(num_data$TermUnregisteredBalance)
num_data[,.N,TermUnregisteredBalance][order(-N)]
length(which(num_data$TermUnregisteredBalance >= 5000))/length(num_data$TermUnregisteredBalance)*100  # around 10%
length(which(num_data$TermUnregisteredBalance == 0))/length(num_data$TermUnregisteredBalance)*100    # > 84%
num_data[,TermUnregisteredBalance := ifelse(TermUnregisteredBalance == 0, "Zero", "MoreThanZero")][,TermUnregisteredBalance := as.factor(TermUnregisteredBalance)]
num_data[,.N,TermUnregisteredBalance][order(-N)]

num_distribution_plot(num_data$NumberOfProducts)
boxplot(num_data$NumberOfProducts)
num_data[,.N,NumberOfProducts][order(-N)]
length(which(num_data$NumberOfProducts <= 4))/length(num_data$NumberOfProducts)*100   # >62%
length(which(num_data$NumberOfProducts >= 10))/length(num_data$NumberOfProducts)*100   
num_data[,NumberOfProducts := ifelse(NumberOfProducts <= 4, NumberOfProducts, ifelse(NumberOfProducts<=10, ">4,<=10", "MoreThan10"))][,NumberOfProducts := as.factor(NumberOfProducts)]
num_data[,.N,NumberOfProducts][order(-N)]




################# DATA CLEANING - CATEGORICAL DATA ########################

## DEAL WITH MISSING DATA
colSums(is.na(fact_data))
fact_missing <- sapply(fact_data, function(x){sum(is.na(x))/length(x)})*100    
fact_missing                     # percentage of the missing data

# none of the columns has more than 2% missing data, so I will replace the missing data with median/mean based on the distribution

fact_distribution_plot <- function(a){
  counts <- table(a)
  barplot(counts)
}

fact_distribution_plot(fact_data$Gender)
levels(fact_data$Gender)                    # Gender should only have F or M
table(fact_data$Gender == "N")
table(is.na(fact_data$Gender))
levels(fact_data$Gender) <- c("F", "M", NA)
table(is.na(fact_data$Gender))
table((levels(fact_data$Gender)[as.integer(fact_data$Gender)]))
fact_data$Gender[is.na(fact_data$Gender)] <- "F"            # use mode here
table((levels(fact_data$Gender)[as.integer(fact_data$Gender)]))
colSums(is.na(fact_data))

fact_distribution_plot(fact_data$City)
levels(fact_data$City)
fact_data[,.N,City][order(-N)]
fact_data$City[is.na(fact_data$City)] <- "Vancouver"        # use mode here
colSums(is.na(fact_data))



## DEAL WITH DATA IMBALANCE, OUTLIERS
summarizeColumns(fact_data)
total_length <- dim(fact_data)[1]

fact_distribution_plot(fact_data$City)
fact_data[,.N,City][order(-N)]
sum(fact_data[,.N,City][N >= 22289]$N)/total_length*100    # >62%
median(fact_data[,.N,City][N >= 1]$N)      # median is 1, too diversified
df <- fact_data[,.N,City][N < 22289]$City
df
fact_data[ City %in% df, City := "Other" ]
fact_data[,.N,City][order(-N)]

fact_distribution_plot(fact_data$JoinDateKey)
fact_data[,.N,JoinDateKey][order(-N)]
# seperate JoinDateKey into JoinYear, JoinMonth
fact_data[, JoinYear := as.factor(substring(fact_data$JoinDateKey, 1,4))]
fact_data[, JoinMonth := as.factor(substring(fact_data$JoinDateKey, 5,6))]
str(fact_data$JoinYear)
str(fact_data$JoinMonth)
fact_data[, JoinDateKey := NULL]

fact_distribution_plot(fact_data$MemberShareLevelKey)
fact_data[,.N,MemberShareLevelKey][order(-N)]
md <- median(table(as.numeric((levels(fact_data$MemberShareLevelKey))[as.integer(fact_data$MemberShareLevelKey)])))
md
df <- fact_data[,.N,MemberShareLevelKey][N >= md]$MemberShareLevelKey
df
fact_data[!(MemberShareLevelKey %in% df), MemberShareLevelKey := "Other" ]
fact_data[,.N,MemberShareLevelKey][order(-N)]


# Label Encoding/One-hot, to convert categorical data into numerical data
summarizeColumns(fact_data)
summarizeColumns(num_data)

library(dplyr)
new_fact <- cbind(Filter(is.factor, num_data), Filter(is.factor, fact_data))
fact_data$Age <- as.numeric(fact_data$Age)
new_num <- cbind(Filter(is.numeric, num_data), Filter(is.numeric, fact_data))
rm(fact_data)
rm(num_data)


summarizeColumns(new_fact)
levels(new_fact$SWMRESPBalance)
new_fact[, SWMRESPBalance := NULL]
summarizeColumns(new_fact)


# Find all columns start with "Has", they all have 2 levels, convert "Y"/"N" to 1/2
selected_cols <- grepl( "Has" , names( new_fact ))
has_cols <- subset(new_fact, select = selected_cols==T)
names(has_cols)
summarizeColumns(has_cols)
new_fact <- subset(new_fact, select = !names(new_fact) %in% names(has_cols))   ## remove these columns from new_fact
has_cols <- has_cols[, names(has_cols) := lapply(.SD, as.numeric), .SDcols = names(has_cols)]    ## convert all the columns to numeric
summarizeColumns(has_cols)


## METHOD 1 - Label Encoding
lvs <- sapply(new_fact, levels)
lvs_length <- sapply(lvs, length)
lvs_length
low_level_cols <- subset(new_fact, select = lvs_length <= 10)
summarizeColumns(low_level_cols)

high_level_cols <- subset(new_fact, select = !names(new_fact) %in% names(low_level_cols))
low_level_cols <- low_level_cols[, names(low_level_cols) := lapply(.SD, as.numeric), .SDcols = names(low_level_cols)]    ## convert all the columns to numeric
summarizeColumns(low_level_cols)

test <- sapply(low_level_cols, unique)
test
