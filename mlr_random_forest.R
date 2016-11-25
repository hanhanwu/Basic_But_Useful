# This example include what to be noted when useing R Random Forest, especially the one in mlr package

test_train <- train_data
test_test <- test_data
 
# Newest R Random Forest can no longer handle ordered Factor variables, convert them to numerical data
fact_cols <- lapply(test_test, is.factor)
fc <- colnames(subset(test_test, select = fact_cols == T))
test_test[,(fc) := lapply(.SD, as.numeric), .SDcols = fc]
summarizeColumns(test_test)
 
fact_cols <- lapply(test_train, is.factor)
fc <- colnames(subset(test_train, select = fact_cols == T))
test_train[,(fc) := lapply(.SD, as.numeric), .SDcols = fc]
summarizeColumns(test_train)
 
# But the label still has to be Factor variable when the predict.type is "response"
test_test$HasWriteOff <- as.factor(test_test$HasWriteOff)
test_train$HasWriteOff <- as.factor(test_train$HasWriteOff)
 
# Here I'm using minority class as the Positive Class
summary(train_data$HasWriteOff)
train_task <- makeClassifTask(data=data.frame(train_data), target = "HasWriteOff", positive = "2")
test_task <- makeClassifTask(data=data.frame(test_data), target = "HasWriteOff", positive = "2")
 
set.seed(410)
getParamSet("classif.randomForest")
rf_learner <- makeLearner("classif.randomForest", predict.type = "response", par.vals = list(ntree = 200, mtry = 3))
rf_learner$par.vals <- list(importance = TRUE)
rf_param <- makeParamSet(
  makeIntegerParam("ntree",lower = 50, upper = 500),
  makeIntegerParam("mtry", lower = 3, upper = 10),
  makeIntegerParam("nodesize", lower = 10, upper = 50)
)
 
rancontrol <- makeTuneControlRandom(maxit = 50L)
cv_rf <- makeResampleDesc("CV",iters = 3L)
rf_tune <- tuneParams(learner = rf_learner, resampling = cv_rf, task = train_task, par.set = rf_param, control = rancontrol, measures = acc)
rf_tune$x
rf_tune$y
rf.tree <- setHyperPars(rf_learner, par.vals = rf_tune$x)
rf_model <- mlr::train(learner=rf.tree, task=train_task)    # when multiple packages have the same method name, use PackageName::MethodName
getLearnerModel(rf_model)
rfpredict <- predict(rf_model, test_task)

# detailed measures to check the accuracy for both Positive and Negative classes
## Majorly check Balanced Accuracy, Sensitivity and Specificity
nb_prediction <- nb_predict$data$response
dCM <- confusionMatrix(d_test$income_level, nb_prediction, positive = "2")    # set Positive Class the same as the tasks above
dCM
