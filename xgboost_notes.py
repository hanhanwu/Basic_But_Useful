# Check feature names and feature orders used in saved pickle file
import pickle
xgb_model = pickle.load(open('xgb_pickle.sav', 'rb'))
print(xgb_model.feature_names)


# predict results with trained pickle file
from matplotlib import pylab as plt
import seaborn as sns
sns.set(color_codes=True)
import xgboost as xgb

y_pred_prob = xgb_model.predict(xgb.DMatrix(all_features), ntree_limit=592)
print(len(y_pred_prob))

## classification with threshold
threshold = 0.7
fraud_records = [prob for prob in y_pred_prob if prob >= threshold]
pred_fraud_perct = len(fraud_records)/len(y_pred_prob)*100
print(pred_fraud_perct, np.mean(fraud_records))

nonfraud_records = [prob for prob in y_pred_prob if prob < threshold]
pred_nonfraud_perct = len(nonfraud_records)/len(y_pred_prob)*100
print(pred_nonfraud_perct, np.mean(nonfraud_records))

## visualize predicted results
fig=plt.figure(figsize=(30,20))
sns.distplot(fraud_records, color='red', label='predicted_fraud')
sns.distplot(nonfraud_records, color='green', label='predicted_nonfraud')
plt.legend(loc='best', prop={'size': 40})
plt.title('XGB Predicted Results Distribution', size = 40)
plt.xlabel('Predicted Probability', size=40)
plt.ylabel('Percentage', size=40)
    
fig.tight_layout()
plt.show()
