# Here, I am trying to group by TRUID and select the count of Neighborhood, the max frequency of Neighborhood

## group by and select count
dt1 <- data.table(TRUID=q4$TRUID, Neighborhood=q4$Neighborhood)
setkeyv(dt1, c("TRUID"))
dt1 <- dt1[, .(count=uniqueN(Neighborhood)), by=TRUID]
head(dt1)


## group by and select max frequency
dt2 <- data.table(TRUID=q4$TRUID, Neighborhood=q4$Neighborhood)
freq_dt <- data.table(table(q4$Neighborhood))
colnames(freq_dt)[1] <- "Neighborhood"
dt3 <- merge(x=dt2, y=freq_dt, by="Neighborhood")
setkeyv(dt3, c("TRUID"))
dt3 <- dt3[, .SD[which.max(N)], by=TRUID]
head(dt3)
rm(dt2)
rm(freq_dt)

## group by and put items in a list for each group
product_lst <- orders_prior[, .(current_order = list(product_id)), by=order_id]
