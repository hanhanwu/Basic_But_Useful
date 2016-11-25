# check all information about learners in MLR, such as their parameter values
listLearners()

# check all packages can be used in MLR
listLearners()[c("class","package")]

# show all classifications can be used in mlr
listLearners("classif", check.packages = F)[c("class","package")]
 
# show all INSTALLED classifications can be used in mlrl
istLearners("classif", check.packages = T)[c("class","package")]


# can classification learnners that can handle missing values
listLearners("classif", check.packages = F, properties = "missings")[c("class","package")]
 
# can handle multiclass or probabilities as output
listLearners("classif", check.packages = F, properties = c("multiclass", "prob"))[c("class","package")]
 

 

 
 
