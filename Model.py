import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt
from sklearn.metrics import mean_squared_error
from math import sqrt

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

linear = LinearRegression()
linear.fit(x_train, y_train)
predictions = linear.predict(x_test)

plt.scatter(y_test, predictions)
plt.plot(y_train, y_train, color = 'red')
plt.xlabel('True Values')
plt.ylabel('Predictions')
plt.show()

# get cross validation scores
y_predicted = linear.predict(x_train)
y_test_predicted = linear.predict(x_test)


def rmse(x, y):
    return sqrt(mean_squared_error(x, y))

print("Training Model Accuracy" , ":" , linear.score(x_train, y_train) , "," ,
      "Sample Test Model Accuracy" ,":" , linear.score(x_test, y_test))
print("Training RMSE", ":", rmse(y_train, y_predicted),
      "Testing RMSE", ":", rmse(y_test, y_test_predicted))
