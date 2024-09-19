from sklearn.datasets import load_digits
import pandas as pd

data = load_digits()
target = pd.Series(data.target)

print(target)