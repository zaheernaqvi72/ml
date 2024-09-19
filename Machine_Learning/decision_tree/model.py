import os
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.tree import DecisionTreeClassifier
# import opendatasets as od

# url = 'https://www.kaggle.com/jsphyg/weather-dataset-rattle-package'
# od.download(url)

# List the files in the input directory
os.listdir('weather-dataset-rattle-package')

# Load the raw dataset
raw_df = pd.read_csv('weather-dataset-rattle-package/weatherAUS.csv')

# print(raw_df.info())

# Drop rows with missing target value (RainTomorrow) and irrelevant columns for the model 
raw_df.dropna(subset=['RainToday', 'RainTomorrow'], inplace=True)


# Split the raw dataset into training/validation and test sets
# 'test_size=0.2' means 20% of the data will be used for testing
# 'random_state=42' ensures reproducibility of the split
train_val_df, test_df = train_test_split(raw_df, test_size=0.2, random_state=42)

# Further split the training/validation set into training and validation sets
# 'test_size=0.25' means 25% of the train_val_df will be used for validation
# This results in 20% test, 60% training, and 20% validation of the original data
# 'random_state=42' ensures reproducibility of the split
train_df, val_df = train_test_split(train_val_df, test_size=0.25, random_state=42)

# print(f"Train shape: {train_df.shape}, Val shape: {val_df.shape}, Test shape: {test_df.shape}")

'''
plt.title('No of rows per year')
sns.countplot(x=pd.to_datetime(raw_df.Date).dt.year)   
plt.show()

'''

# Convert the 'Date' column in raw_df to datetime format and extract the year
year = pd.to_datetime(raw_df.Date).dt.year

# Create the training dataset with rows where the year is less than 2015
train_df = raw_df[year < 2015]

# Create the validation dataset with rows where the year is equal to 2015
val_df = raw_df[year == 2015]

# Create the test dataset with rows where the year is greater than 2015
test_df = raw_df[year > 2015]

# print('train_df.shape :', train_df.shape)
# print('val_df.shape :', val_df.shape)
# print('test_df.shape :', test_df.shape)

# print(f"Train : \n {train_df},\n Val : \n {val_df},\n Test : \n {test_df}")

# Excluding 'Date' and 'RainTomorrow' columns
input = list(train_df.columns)[1:-1]    
target = 'RainTomorrow'

# print(f"Input features: {input}")

train_inputs = train_df[input].copy()
train_targets = train_df[target].copy()

val_inputs = val_df[input].copy()
val_targets = val_df[target].copy()

test_inputs = test_df[input].copy()
test_targets = test_df[target].copy()
 
# Select columns with numeric data types from train_inputs and convert them to a list
numeric_cols = train_inputs.select_dtypes(include=np.number).columns.tolist()

# Select columns with categorical data types (object) from train_inputs and convert them to a list
categorical_cols = train_inputs.select_dtypes('object').columns.tolist()

'''
print(f"Numeric columns: {train_inputs[numeric_cols].describe()}")

print(f"Categorical columns: {train_inputs[categorical_cols].nunique()}")
'''

# Create an imputer object with the strategy to replace missing values with the mean
imputer = SimpleImputer(strategy='mean').fit(raw_df[numeric_cols])

# Print the statistics (mean values) computed by the imputer for each numeric column
# print(imputer.statistics_)

# Apply the imputer to the training data to replace missing values with the mean
train_inputs[numeric_cols] = imputer.transform(train_inputs[numeric_cols])

# Apply the imputer to the validation data to replace missing values with the mean
val_inputs[numeric_cols] = imputer.transform(val_inputs[numeric_cols])

# Apply the imputer to the test data to replace missing values with the mean
test_inputs[numeric_cols] = imputer.transform(test_inputs[numeric_cols])

'''
# Check for missing values in the training data
print(f"Train inputs: {train_inputs[numeric_cols].isnull().sum()} missing values")
'''

# Initialize and fit the MinMaxScaler on the numeric columns of raw_df
scaler = MinMaxScaler().fit(raw_df[numeric_cols])

# Apply the scaler to the numeric columns of the training data
train_inputs[numeric_cols] = scaler.transform(train_inputs[numeric_cols])

# Apply the scaler to the numeric columns of the validation data
val_inputs[numeric_cols] = scaler.transform(val_inputs[numeric_cols])

# Apply the scaler to the numeric columns of the test data
test_inputs[numeric_cols] = scaler.transform(test_inputs[numeric_cols])

'''
print(f"Train inputs: {train_inputs[numeric_cols].describe().T}")
print(f"Val inputs: {val_inputs[numeric_cols].describe().T}")
print(f"Test inputs: {test_inputs[numeric_cols].describe().T}")
'''

# Initialize and fit the OneHotEncoder on the categorical columns of raw_df
encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore').fit(raw_df[categorical_cols])

# print(f"Categories: {encoder.categories_}")

# Get the feature names after one-hot encoding the categorical columns
encoded_cols = list(encoder.get_feature_names_out(categorical_cols))

# Transform and concatenate for train_inputs
train_transformed = pd.DataFrame(encoder.transform(train_inputs[categorical_cols]), columns=encoded_cols, index=train_inputs.index)
train_inputs = pd.concat([train_inputs, train_transformed], axis=1)

# Transform and concatenate for val_inputs
val_transformed = pd.DataFrame(encoder.transform(val_inputs[categorical_cols]), columns=encoded_cols, index=val_inputs.index)
val_inputs = pd.concat([val_inputs, val_transformed], axis=1)

# Transform and concatenate for test_inputs
test_transformed = pd.DataFrame(encoder.transform(test_inputs[categorical_cols]), columns=encoded_cols, index=test_inputs.index)
test_inputs = pd.concat([test_inputs, test_transformed], axis=1)



print(f"Train inputs: \n {train_inputs[encoded_cols]}")
print(f"Val inputs: \n {val_inputs[encoded_cols]}") 
print(f"Test inputs: \n {test_inputs[encoded_cols]}")


help(DecisionTreeClassifier)
