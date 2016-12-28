# here writeoff is the dependent variable, before reducing the levels, need to check the distribution
ggplot(origin_fact_data, aes(HasWriteOff, ..count..)) + geom_bar(aes(fill = Neighborhood), position = "dodge")

# # Neighborhood has hundreds of levels
tmp_dt <- data.table(table(origin_fact_data$Neighborhood))
head(tmp_dt)
top_cols <- tmp_dt[order(-rank(N))][1:11]$V1
origin_fact_data[, Neighborhood:=ifelse(is.na(Neighborhood), "MISSING", ifelse(Neighborhood %in% top_cols, Neighborhood, "Other"))]
origin_fact_data$Neighborhood <- as.factor(origin_fact_data$Neighborhood)
summary(origin_fact_data$Neighborhood)
