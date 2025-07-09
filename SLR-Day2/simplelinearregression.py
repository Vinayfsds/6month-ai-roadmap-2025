import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


dataset = pd.read_csv(r'C:\Ml\Salary_Data.csv')

x = dataset.iloc[:, :-1]  
y = dataset.iloc[:, -1]

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=0)


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train) 

y_pred = regressor.predict(x_test)

# Compare predicted and actual salaries from the test set
comparison = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(comparison)

# Visualize the test set
plt.scatter(x_test, y_test, color='red') 
plt.plot(x_train, regressor.predict(x_train), color='blue')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

m_slope = regressor.coef_
print(m_slope)

c_intercept = regressor.intercept_
print(c_intercept)

#pred:1
y_12 = (m_slope*12) + c_intercept
print(y_12)


#pred:2
y_20 = (m_slope*20) + c_intercept
print(y_20)
 
#Mean

dataset.mean()

dataset['Salary'].mean()

dataset.median()

dataset['Salary'].median()

dataset['Salary'].mode()

dataset.var()

dataset['Salary'].var()

dataset.std()

dataset['Salary'].std()

#coefficient of variation
from scipy.stats import variation
variation(dataset.values)

variation(dataset['Salary'].values)

# Correlation

dataset.corr()

dataset['Salary'].corr(dataset['YearsExperience'])


#Skeweness

dataset.skew()


dataset['Salary'].skew()

#Standard Error

dataset.sem()


dataset['Salary'].sem()

# Z-score

import scipy.stats as stats

dataset.apply(stats.zscore)

stats.zscore(dataset['Salary'])

# Degree of Freedom

a= dataset.shape[0]
b = dataset.shape[1]

degree_of_freedom = a -b
print(degree_of_freedom)

#Sum of Squares Regression
y_mean = np.mean(y)
SSR = np.sum((y_pred-y_mean)**2)
print(SSR)

y=y[0:6]
SSE = np.sum((y-y_pred)**2)
print(SSE)

SST = SSR + SSE
print(SST)

# R- Square
r_square = 1- (SSR / SST)
print(r_square)

bias = regressor.score(x_test, y_test)
print(bias)

variance = regressor.score(x_test, y_test)
print(variance)


from sklearn.metrics import mean_squared_error
train_mse = mean_squared_error(y_train, regressor.predict(x_train))
test_mse = mean_squared_error(y_test, y_pred)

import pickle

#Save the trained model to disk
filename = 'linear_regression_model.pkl'

with open(filename, 'wb') as file:
    pickle.dump(regressor, file)
print("Model has been pickled and saved as linear_regression_model")

import os
os.getcwd()


