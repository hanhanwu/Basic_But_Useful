# The file include those functions having different names as other programming languages, but serve for the same purpose
# More earlier time R practices: https://github.com/hanhanwu/Hanhan_Data_Science_Practice

# R basics: https://github.com/hanhanwu/Hanhan_Data_Science_Practice/blob/master/R_Basics.R
# R data.table Basics: https://github.com/hanhanwu/Hanhan_Data_Science_Practice/blob/master/R_data.table_basics.R

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

# Plot histogram of each numerical variable
options(repr.plot.width=20, repr.plot.height=10) # this increase the image size in jupyter
par(mfrow=c(2,2), cex=1.5)  # cex scales all the fonts 150 percent
for(i in names(iris)[1:4]){hist(iris[,i], xlab=i, main="")}

# Plot mutliple density plots, each density plots shows the distribution of each category
p1 <- ggdensity(iris, x = "Sepal.Length",
   add = "mean", rug = TRUE,
   color = "Species", fill = "Species",
   font.label = list(size = 20, color = "black"))

p2 <- ggdensity(iris, x = "Sepal.Width",
   add = "mean", rug = TRUE,
   color = "Species", fill = "Species",
   font.label = list(size = 20, color = "black"))

p3 <- ggdensity(iris, x = "Petal.Length",
   add = "mean", rug = TRUE,
   color = "Species", fill = "Species",
   font.label = list(size = 20, color = "black"))

p4 <- ggdensity(iris, x = "Petal.Width",
   add = "mean", rug = TRUE,
   color = "Species", fill = "Species",
   font.label = list(size = 20, color = "black"))

plot_grid(p1, p2, p3, p4,
      labels="auto",
      ncol=2, nrow=2)


# R different apply functions: 
## https://www.analyticsvidhya.com/blog/2021/02/the-ultimate-swiss-army-knife-of-apply-family-in-r/?utm_source=feedburner&utm_medium=email&utm_campaign=Feed%3A+AnalyticsVidhya+%28Analytics+Vidhya%29
## apply(), lapply(), sapply(), vapply(), tapply(), mapply()
# vapply() to operate on 1+ columns regardless the data type
# tapply() applies 1+ aggregated functions
# mapply() allows to do DIY operations on 2+ cols
