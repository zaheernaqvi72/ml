import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Load the medical charges dataset into a pandas DataFrame
Med_data = pd.read_csv('medical.csv')

non_smoker = Med_data[Med_data.smoker == 'no']
plt.title('Age vs. Charges')
sns.scatterplot(data=non_smoker, x='age', y='charges', alpha=0.7, s=15)
plt.show()

fig = px.violin(Med_data, x='children', y='charges')
fig.show()