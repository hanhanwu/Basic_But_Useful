# When there are so many feature, but if there is one feature has zero variance, you cannot use R built in functions 
# to find the correlation between features, because it will just return an error saying "zero stadard deviation"

# So, before checking the correlation between many features, we need to remove those columns with 0 variance

## The Function to Check Zero Variance
has_zero_variance <- function(dt) {
  out <- lapply(dt, function(x) length(unique(x)))
  want <- which(!out > 1)
  unlist(want)
}


## Columns Need to be Removed
zero_variance_list <- has_zero_variance(num_data)
zero_variance_list

## Check Correlation after Removing the Columns above
## In fact, the results in ax are columns have high correlations with others and should also be removed later
ax <-findCorrelation(x = cor(data.frame(num_data)), cutoff = 0.7)
