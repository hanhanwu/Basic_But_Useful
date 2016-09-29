# convert the data.frame/list into data.table
library(data.table)
require(data.table)
setDT(q1)

## NOTE: when R studio has started a new session, all the generated data may still there, but the previous data.table (q1 here) may become
## data.frame/list again, need to re-run the code above




################# DATA CLEANING BEFORE CHECKING CORRELATION - NUMERIC DATA ########################

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
length(which(num_data$MemberShareBalance >= 7))/length(num_data$MemberShareBalance)*100   # too many individual values, it's better to categorize this column

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
