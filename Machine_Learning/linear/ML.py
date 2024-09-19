# from urllib.request import urlretrieve
import pandas as pd
import plotly.express as px
import matplotlib
# import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd
# %matplotlib inline

# for downloading the dataset
'''
medical_charges_url = 'https://raw.githubusercontent.com/JovianML/opendatasets/master/data/medical-charges.csv'

urlretrieve(medical_charges_url, 'medical.csv')
# Load the pandas library for data manipulation and analysis
'''
# Load the medical charges dataset into a pandas DataFrame
medical = pd.read_csv('medical.csv')

# Display information about the dataset, such as column names and data types
medical.info()

# Print descriptive statistics of the dataset, such as count, mean, min, max, etc.
print(medical.describe())

# Set the style of seaborn plots to 'darkgrid'
sns.set_style('darkgrid')

# Set the font size of matplotlib plots to 14
matplotlib.rcParams['font.size'] = 14

# Set the figure size of matplotlib plots to (10, 6)
matplotlib.rcParams['figure.figsize'] = (10, 6)

# Set the facecolor of matplotlib figures to transparent
matplotlib.rcParams['figure.facecolor'] = '#00000000'

# Create a histogram plot of the distribution of age
fig = px.histogram(medical, 
                   x='age', 
                   marginal='box', 
                   nbins=47, 
                   title='Distribution of Age')
fig.update_layout(bargap=0.1)
fig.show()

# Create a histogram plot of the distribution of BMI (Body Mass Index)
fig = px.histogram(medical, 
                   x='bmi', 
                   marginal='box', 
                   color_discrete_sequence=['red'], 
                   title='Distribution of BMI (Body Mass Index)')
fig.update_layout(bargap=0.1)
fig.show()

# Create a histogram plot of the annual medical charges with smoker information
fig = px.histogram(medical, 
                   x='charges', 
                   marginal='box', 
                   color='smoker', 
                   color_discrete_sequence=['green', 'grey'], 
                   title='Annual Medical Charges (with Smoker)')
fig.update_layout(bargap=0.1)
fig.show()

# Create a histogram plot of the smoker information
fig = px.histogram(medical, x='smoker', color='sex', title='Smoker')
fig.show()

# Create a histogram plot of the annual medical charges with sex information
fig = px.histogram(medical, 
                   x='charges', 
                   marginal='box', 
                   color='sex', 
                   color_discrete_sequence=['green', 'grey'], 
                   title='Annual Medical Charges with Sex')
fig.update_layout(bargap=0.1)
fig.show()

# Create a histogram plot of the annual medical charges with region information
fig = px.histogram(medical, 
                   x='charges', 
                   marginal='box', 
                   color='region', 
                   color_discrete_sequence=['green', 'grey'], 
                   title='Annual Medical Charges with region')
fig.update_layout(bargap=0.1)
fig.show()

fig = px.scatter(medical, 
                 x='age', 
                 y='charges', 
                 color='smoker', 
                 opacity=0.8, 
                 hover_data=['sex'], 
                 title='Age vs. Charges')
fig.update_traces(marker_size=5)

fig.show()

fig = px.scatter(medical, 
                 x='bmi', 
                 y='charges', 
                 color='smoker', 
                 opacity=0.8, 
                 hover_data=['sex'], 
                 title='BMI vs. Charges')
fig.update_traces(marker_size=5)
fig.show()


data = pd.read_csv('medical.csv')

correl = data.age.corr(data.charges)
print(f"Correlation between age and charges: {correl}")

# To compute the correlation for categorical columns, they must first be converted into numeric columns. 

smoker_values = {'no': 0, 'yes': 1}
smoker_numeric = data.smoker.map(smoker_values)
correl2 = data.charges.corr(smoker_numeric)
print(f"Correlation between smoker and charges: {correl2}")

correl3 = data.age.corr(data.bmi)
print(f"Correlation between age and BMI: {correl3}")

'''
Strength: The greater the absolute value of the correlation coefficient, the stronger the relationship.

1. The extreme values of -1 and 1 indicate a perfectly linear relationship where a change in one variable is accompanied by a perfectly consistent change in the other. For these relationships, all of the data points fall on a line. In practice, you won’t see either type of perfect relationship.

2. A coefficient of zero represents no linear relationship. As one variable increases, there is no tendency in the other variable to either increase or decrease.

3. When the value is in-between 0 and +1/-1, there is a relationship, but the points don’t all fall on a line. As r approaches -1 or 1, the strength of the relationship increases and the data points tend to fall closer to a line.

Direction: The sign of the correlation coefficient represents the direction of the relationship.

Positive coefficients indicate that when the value of one variable increases, the value of the other variable also tends to increase. Positive relationships produce an upward slope on a scatterplot.

Negative coefficients represent cases when the value of one variable increases, the value of the other variable tends to decrease. Negative relationships produce a downward slope.

Here's the same relationship expressed visually (source):

alt
The correlation coefficient has the following formula:

alt
'''

