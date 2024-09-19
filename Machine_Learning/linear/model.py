import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import root_mean_squared_error

# Load the medical charges dataset into a pandas DataFrame
Med_data = pd.read_csv('medical.csv')

# Extracting non-smoker data
non_smoker = Med_data[Med_data.smoker == 'no']
# Extracting age
ages = non_smoker.age
# Extracting charges
actual = non_smoker.charges
# w is the slope of the line and b is the y-intercept of the line
w, b = 320, -4200

# Linear regression model 
def pred_charge(age, w, b):
    return w * age + b

# Predicted charges
pred_value = pred_charge(ages, w, b)

# Plotting the linear regression model to compare with the actual data
def param():
    plt.plot(ages, pred_value, 'r', alpha=0.9)
    plt.scatter(ages, actual, s=8,alpha=0.8)
    plt.xlabel('Age')
    plt.ylabel('Charges')
    plt.legend(['Predicted', 'Actual'])
    plt.show()
    
param()

# Root Mean Squared Error calculation using numpy
def rmse(pred, actual):
    return np.sqrt(np.mean(np.square(pred - actual))).round(2)

print(f"Root Mean Squared Error: {rmse(pred_value, actual)}")

# Root Mean Squared Error using Scikit-Learn
rmse_sklearn = root_mean_squared_error(actual, pred_value).round(2)
print(f"Root Mean Squared Error using Scikit-Learn: {rmse_sklearn}")




