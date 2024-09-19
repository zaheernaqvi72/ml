import pandas as pd

a = [1, 2, 3, 4, 5]

s = pd.Series(a, index=['a', 'b', 'c', 'd', 'e'])
print(f"Series: \n {s}")

data_list = [10, 20, 30, 40, 50]
series1 = pd.Series(data_list)

print(f"Series from list: \n {series1}")

data_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
series2 = pd.Series(data_dict)

print(f"Series from index: \n {series2}")