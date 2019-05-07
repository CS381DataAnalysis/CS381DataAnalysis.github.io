import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt
from sklearn.model_selection import KFold
from array import array
from sklearn import metrics

df = pd.read_csv('/Users/jc/Desktop/CS381DataAnalysis/data.csv')

y = df.Sales
x = df.drop('Sales', axis=1)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
print("\ndata:\n")
print(df.head())
print(df.shape)

print("\nx_train:\n")
print(x_train.head())
print(x_train.shape)

print("\nx_test:\n")
print(x_test.head())
print(x_test.shape)

lm = LinearRegression()
model = lm.fit(x_train, y_train)
predictions = lm.predict(x_test)

plt.scatter(y_test, predictions)
plt.xlabel('True Values')
plt.ylabel('Predictions')
# plt.show()

print('Some of predictions: ', predictions[0:5])
print('Model score: ', model.score(x_test,y_test))

scores = cross_val_score(model, df, y, cv=6)
print('Cross-validated scores', scores)

predictions = cross_val_predict(model, df, y, cv=6)
plt.scatter(y, predictions)
plt.show()

accuracy = metrics.r2_score(y, predictions)
print('Cross-Predicted Accuracy:', accuracy)