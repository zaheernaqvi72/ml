from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

med_data = pd.read_csv('medical.csv')
# Extracting non-smoker data
no_smoker = med_data[med_data.smoker == 'no']

# Extracting age and charges
ages, targets = no_smoker[['age']],no_smoker.charges

# Create a linear regression model and fit it to the data
model = LinearRegression().fit(ages, targets)

# Predict the charges using the model 
prediction = model.predict(ages)
# print(f"Predicted charges: \n {prediction}")

# Root Mean Squared Error calculation using numpy
def rmse(pred, actual):
    return np.sqrt(np.mean(np.square(pred - actual))) 

final = rmse(prediction, targets).round(2)
print(f"Root Mean Squared Error using numpy: {final}")

# Root Mean Squared Error using Scikit-Learn
rmse_sklearn = root_mean_squared_error(prediction, targets).round(2)
print(f"Root Mean Squared Error using Scikit-Learn: {rmse_sklearn}")


# Plotting the linear regression model to compare with the actual data
def param():
    plt.plot(ages, prediction, 'r', alpha=0.9)
    plt.scatter(ages, targets, s=8,alpha=0.8)
    plt.xlabel('Age')
    plt.ylabel('Charges')
    plt.legend(['Predicted', 'Actual'])
    plt.show()
    
param()

# print(f"Model Coefficient: {model.coef_}")

# print(f"Model Intercept: {model.intercept_}")

# print(f"Model Score: {model.score(ages, targets)}")

# print(f"Model Prediction for age 22: {model.predict([[22]])}")

# Statnardization of the data
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(ages)
ages_scaled = scaler.transform(ages)
print(f"Standardized ages: \n {ages_scaled}")

