summary(q1$HasWriteOff)
data_task <- makeClassifTask(data = q1, target = "HasWriteOff", positive = "1")
data_task <- removeConstantFeatures(data_task)
 
# Check Feature Importance with Information Gain
var_imp <- generateFilterValuesData(data_task, method = c("information.gain"))
plotFilterValues(var_imp, feat.type.cols = TRUE)
 
# Check Feature Importance with Random Forest
# This one takes very long time to run by default. May need to set parameter "more.args"
var_imp_rf <- generateFilterValuesData(data_task, method = c("rf.importance"))
plotFilterValues(var_imp, feat.type.cols = TRUE)
