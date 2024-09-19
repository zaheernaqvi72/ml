import numpy as np

dec_array = np.array([1.13435, 2.36362, 3.33636, 4.43737])

rounded_array = np.round(dec_array, decimals=3)
print(f"Rounded Array: {rounded_array}")

arround_array = np.around(dec_array, decimals=2)
print(f"Arrounded Array: {arround_array}")

