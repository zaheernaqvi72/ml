from sklearn.datasets import load_digits
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.decomposition import PCA

dataset = load_digits()

df = pd.DataFrame(dataset.data)

y = dataset.target

scaler = StandardScaler()

scaled_val = scaler.fit_transform(df)

X_train, X_test, y_train, y_test = train_test_split(scaled_val, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)
print(f"Train score: {model.score(X_train, y_train)}")


pca = PCA(n_components=10)
X_pca = pca.fit_transform(scaled_val)

pca_train, pca_test, y_train, y_test = train_test_split(X_pca, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(pca_train, y_train)
print(f"Train score after PCA: {model.score(pca_train, y_train)}")



