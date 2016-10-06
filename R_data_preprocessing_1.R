# convert the data.frame/list into data.table
library(data.table)
require(data.table)
setDT(q1)

## NOTE: when R studio has started a new session, all the generated data may still there, but the previous data.table (q1 here) may become
## data.frame/list again, need to re-run the code above



## SEPERATE NUMERICAL AND CATEGORICAL DATA
mark_fact_cols <- sapply(q1, is.factor)
fact_data <- subset(q1, select = mark_fact_cols==T)
num_data <- subset( q1, select = mark_fact_cols==F)

summarizeColumns(num_data)
summarizeColumns(fact_data)



## MY LAZY FUNCTIONS
library(ggplot2)
# install.packages("plotly", type = "source")
library(plotly)

# CHECK DISTRIBUTION METHOD - NUMERIC DATA
num_distribution_plot <- function(a){
  ggplot(data = num_data, aes(x= a, y=..density..)) + geom_histogram(fill="blue",color="red",alpha = 0.5,bins =100) + geom_density()
  ggplotly()
}


# CHECK DISTRIBUTION METHOD - CATEGORICAL DATA
fact_distribution_plot <- function(a){
  counts <- table(a)
  barplot(counts)
}


# BIN NUMERICAL DATA TO CATEGORICAL DATA - QUANTILE BASED
bin_to_quantile <- function(a) {
  q <- quantile(a)
  q <- data.frame(q)
  q
  l1 <- paste(as.character(q$q[1]), as.character(q$q[2]), sep = " ~ ")
  l2 <- paste(as.character(q$q[2]), as.character(q$q[3]), sep = " ~ ")
  l3 <- paste(as.character(q$q[3]), as.character(q$q[4]), sep = " ~ ")
  l4 <- paste(as.character(q$q[4]), as.character(q$q[5]), sep = " ~ ")
  lbs <- c(l1, l2, l3, l4)
  return(cut(x = a,breaks = c(quantile(a)),include.lowest = TRUE,labels = lbs)) 
}

bin_to_triple <- function(a, v1, v2, lb1, lb2, lb3) {
  return (as.factor(ifelse(a == v1, lb1, ifelse(a <= v2, lb2, lb3))))
}

bin_to_double <- function(a, v, lb1, lb2) {
  return (as.factor(ifelse(a == v, lb1, lb2)))
}

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
## !!! For data with numerical ormat but categorical nature, convert them to factors first to deal with missing data,
## then, use category combine for those do have <= 5 categories, these variables won't use one-hot encoding later;
## for those have >= 6 categories, bin them, so that both label encoding or one-hot encoding should work.


num_distribution_plot(num_data$MemberShareBalance)
boxplot(num_data$MemberShareBalance)
num_data[,.N,MemberShareBalance][order(-N)]
length(which(num_data$MemberShareBalance == 5.00))/length(num_data$MemberShareBalance)*100   # 2.6%
num_data[,.N,MemberShareBalance][N >= 1000][order(-N)]
sum(num_data[,.N,MemberShareBalance][N >= 1000]$N)/length(num_data$MemberShareBalance)*100    # 8.7%
sum(num_data[,.N,MemberShareBalance][N <= 0]$N)/length(num_data$MemberShareBalance)*100    # 0
summary(num_data$MemberShareBalance) 
sum(num_data[,.N,MemberShareBalance][MemberShareBalance >= 50000]$N)/length(num_data$MemberShareBalance)*100   # 0.006678744
num_data[, MemberShareBalance := ifelse(MemberShareBalance>=50000, median(MemberShareBalance), MemberShareBalance)]
sum(num_data[,.N,MemberShareBalance][MemberShareBalance >= 10000]$N)/length(num_data$MemberShareBalance)*100      #1%
num_data[, MemberShareBalance := ifelse(MemberShareBalance>=10000, median(MemberShareBalance), MemberShareBalance)]
sum(num_data[,.N,MemberShareBalance][MemberShareBalance >= 1000]$N)/length(num_data$MemberShareBalance)*100   # 4.44%
num_data[, MemberShareBalance := ifelse(MemberShareBalance>=1000, median(MemberShareBalance), MemberShareBalance)]
sum(num_data[,.N,MemberShareBalance][MemberShareBalance >= 200]$N)/length(num_data$MemberShareBalance)*100   # >15%
summary(num_data$MemberShareBalance) 
boxplot(num_data$MemberShareBalance)
## !!! When dealing with outliers, when I don't know the reason for these outliers, I am using median/mean based on distribution.
## But if there are any other variable will directly influcen this variable, I would check which gruup in that variable directly influce the
## outliers and only use median/mean of that group
sum(num_data[,.N,MemberShareBalance][MemberShareBalance >= 110]$N)/length(num_data$MemberShareBalance)*100 # > 25%
boxplot(num_data$MemberShareBalance)
# Bining the data
num_data[, MemberShareBalance:= cut(x = MemberShareBalance,breaks = c(0,30,110,1000),include.lowest = TRUE,labels = c("LessThan30","30TO110","HigherThan110"))]
levels(num_data$MemberShareBalance)



# Methods for Bining Numerical Data
# 2 bins
num_distribution_plot(num_data$TermUnregisteredBalance)
boxplot(num_data$TermUnregisteredBalance)
num_data[,.N,TermUnregisteredBalance][order(-N)]
length(which(num_data$TermUnregisteredBalance >= 5000))/length(num_data$TermUnregisteredBalance)*100  # around 10%
length(which(num_data$TermUnregisteredBalance == 0))/length(num_data$TermUnregisteredBalance)*100    # > 84%
num_data[,TermUnregisteredBalance := ifelse(TermUnregisteredBalance == 0, "Zero", "MoreThanZero")][,TermUnregisteredBalance := as.factor(TermUnregisteredBalance)]
num_data[,.N,TermUnregisteredBalance][order(-N)]

# 3 bins
num_distribution_plot(num_data$NumberOfProducts)
boxplot(num_data$NumberOfProducts)
num_data[,.N,NumberOfProducts][order(-N)]
length(which(num_data$NumberOfProducts <= 4))/length(num_data$NumberOfProducts)*100   # >62%
length(which(num_data$NumberOfProducts >= 10))/length(num_data$NumberOfProducts)*100   
num_data[,NumberOfProducts := ifelse(NumberOfProducts <= 4, NumberOfProducts, ifelse(NumberOfProducts<=10, ">4,<=10", "MoreThan10"))][,NumberOfProducts := as.factor(NumberOfProducts)]
num_data[,.N,NumberOfProducts][order(-N)]

# [MORE FLAXIBLE], multiple bins by setting the threshold
sum(num_data[,.N,MemberShareBalance][MemberShareBalance >= 110]$N)/length(num_data$MemberShareBalance)*100 # > 25%
boxplot(num_data$MemberShareBalance)
# Bining the data
num_data[, MemberShareBalance:= cut(x = MemberShareBalance,breaks = c(0,30,110,1000),include.lowest = TRUE,labels = c("LessThan30","30TO110","HigherThan110"))]
levels(num_data$MemberShareBalance)

# When I know this variable won't be influenced by other variables, I didn't removing those outliers, but bin the data based on quantiles
num_distribution_plot(num_data$X)
boxplot(num_data$X)
num_data[,.N,X][order(-N)]
summary(num_data$X)
length(which(num_data$X >= 15))/length(num_data$X)*100      # > 77%
length(which(num_data$X >= 17760))/length(num_data$X)*100   # >25%
length(which(num_data$X <= 1948))/length(num_data$X)*100    # 50%
# bining the data
q <- quantile(num_data$X)
q <- data.frame(q)
q
l1 <- paste(as.character(q$q[1]), as.character(q$q[2]), sep = " ~ ")
l2 <- paste(as.character(q$q[2]), as.character(q$q[3]), sep = " ~ ")
l3 <- paste(as.character(q$q[3]), as.character(q$q[4]), sep = " ~ ")
l4 <- paste(as.character(q$q[4]), as.character(q$q[5]), sep = " ~ ")
lbs <- c(l1, l2, l3, l4)
num_data[, X:= cut(x = X,breaks = c(quantile(X)),include.lowest = TRUE,labels = lbs)]
summary(num_data$X)
levels(num_data$X)


num_distribution_plot(num_data$DemandUnregisteredBalance)
boxplot(num_data$DemandUnregisteredBalance)
num_data[,.N,DemandUnregisteredBalance][order(-N)]
summary(num_data$DemandUnregisteredBalance)
length(which(num_data$DemandUnregisteredBalance >= 15))/length(num_data$DemandUnregisteredBalance)*100    # >74%
length(which(num_data$DemandUnregisteredBalance == 0))/length(num_data$DemandUnregisteredBalance)*100    # 16%
# bining the data
## I got tired of modifying each line for so many columns, so created the general function to deal with them. And without hardcoding, code is more secure
## But need to check whether the data can be used with this method first. In this case, I need to bin them into 4 quantiles.
num_data$DemandUnregisteredBalance <- bin_to_quantile(num_data$DemandUnregisteredBalance)
summary(num_data$DemandUnregisteredBalance)
levels(num_data$DemandUnregisteredBalance)


# Customized Bins
num_distribution_plot(num_data$NumberOfIVRTransactions)
boxplot(num_data$NumberOfIVRTransactions)
num_data[,.N,NumberOfIVRTransactions][order(-N)]
length(which(num_data$NumberOfIVRTransactions == 0))/length(num_data$NumberOfIVRTransactions)*100  # > 98%
# 2 bins
num_data$NumberOfIVRTransactions <- bin_to_double(num_data$NumberOfIVRTransactions, 0, "Zero", "MoreThanZero")
num_data[,.N,NumberOfIVRTransactions][order(-N)]


num_distribution_plot(num_data$NumberOfWebTransactions)
boxplot(num_data$NumberOfWebTransactions)
num_data[,.N,NumberOfWebTransactions][order(-N)]
length(which(num_data$NumberOfWebTransactions == 0))/length(num_data$NumberOfWebTransactions)*100   # > 74%
length(which(num_data$NumberOfWebTransactions <= 4))/length(num_data$NumberOfWebTransactions)*100   # >88%
# 3 bins
num_data$NumberOfWebTransactions <- bin_to_triple(num_data$NumberOfWebTransactions, 0, 4, "Zero", "1 ~ 4", "4+")
num_data[,.N,NumberOfWebTransactions][order(-N)]





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


fact_distribution_plot(fact_data$MemberBranchNumber)
fact_data[,.N,MemberBranchNumber][order(-N)]
q <- quantile(table(as.numeric((levels(fact_data$MemberBranchNumber))[as.integer(fact_data$MemberBranchNumber)])), na.rm = T)
q <- data.frame(q)
q
df1 <- fact_data[,.N,MemberBranchNumber][N < q$q[2]]$MemberBranchNumber
df2 <- fact_data[,.N,MemberBranchNumber][N >= q$q[2] & N < q$q[3]]$MemberBranchNumber
df3 <- fact_data[,.N,MemberBranchNumber][N >= q$q[3] & N < q$q[4]]$MemberBranchNumber
df4 <- fact_data[,.N,MemberBranchNumber][N >= q$q[4]]$MemberBranchNumber
l1 <- paste(as.character(q$q[1]), as.character(q$q[2]), sep = " ~ ")
l2 <- paste(as.character(q$q[2]), as.character(q$q[3]), sep = " ~ ")
l3 <- paste(as.character(q$q[3]), as.character(q$q[4]), sep = " ~ ")
l4 <- paste(as.character(q$q[4]), as.character(q$q[5]), sep = " ~ ")
fact_data[, MemberBranchNumber := ifelse(MemberBranchNumber %in% df1, l1, ifelse(MemberBranchNumber %in% df2, l2, ifelse(MemberBranchNumber %in% df3, l3, l4)))]
setnames(fact_data, "MemberBranchNumber", "BranchNumber_MemberCount")
fact_data[,.N,BranchNumber_MemberCount][order(-N)]


fact_distribution_plot(fact_data$MemberJointNumber)
fact_data[,.N,MemberJointNumber][order(-N)]
fact_data[,.N,MemberJointNumber][MemberJointNumber=='0']$N/total_length*100    # 74%
fact_data[,.N,MemberJointNumber][MemberJointNumber=='1']$N/total_length*100    # 20%
quantile(table(as.numeric((levels(fact_data$MemberJointNumber))[as.integer(fact_data$MemberJointNumber)])))
median(table(as.numeric((levels(fact_data$MemberJointNumber))[as.integer(fact_data$MemberJointNumber)])), na.rm = T)
fact_data[,MemberJointNumber := ifelse(MemberJointNumber == '0', "Zero", ifelse(MemberJointNumber == '1', "One", "1+"))][,MemberJointNumber := as.factor(MemberJointNumber)]
fact_data[,.N,MemberJointNumber][order(-N)]


fact_distribution_plot(fact_data$City)
fact_data[,.N,City][order(-N)]
fact_data[,.N,City][City == 'Vancouver']$N/total_length*100   # 28%
sum(fact_data[,.N,City][N >= 22289]$N)/total_length*100    # >62%
median(fact_data[,.N,City]$N)      # median is 1, too diversified
quantile(fact_data[,.N,City]$N)
sum(fact_data[,.N,City][N >= 3]$N)/total_length*100    # >99%
od <- fact_data[,.N,City][order(-N)]
od <- data.frame(od)
od[1:10,]
# find total >75%
df<- fact_data[,.N,City][order(-N)]
df
st <- c()
ct <- 1
total_ct <- 0
for (i in df$City){
  total_ct = total_ct + df[ct]$N
  if (total_ct/total_length > 0.75) break
  st[[ct]] <- i
  ct = ct + 1
}
st <- data.frame(st)
st
fact_data[ !City %in% st, City := "Other" ]
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
