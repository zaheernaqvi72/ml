import numpy as np

num_array = np.array([1, 2, 3, 4])

log_array = np.log(num_array).round(decimals=2)
print(f"Natural Logarithm: \n {log_array}")

expo_array = np.exp(num_array).round(decimals=2)
print(f"Exponential: \n {expo_array}")

log_base10_array = np.log10(num_array).round(decimals=2)
print(f"Logarithm Base 10: \n {log_base10_array}")