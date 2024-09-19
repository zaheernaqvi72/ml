from sklearn.metrics import mean_absolute_error, mean_squared_error
y_true = [25, 15, 20, 30, 40]
y_pred = [28, 14, 22, 29, 38]
mae = mean_absolute_error(y_true, y_pred)
print(f"Mean Absolute Error: {mae}")

mse = mean_squared_error(y_true, y_pred)
print(f"Mean Squared Error: {mse}")