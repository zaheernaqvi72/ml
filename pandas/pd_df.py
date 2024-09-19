import pandas as pd

data_dict = {'Name': ['Tom', 'Nick', 'John', 'Smith'],
             'Age': [20, 21, 19, 18],
             'city': ['New York', 'New York', 'Los Angeles', 'Chicago'],
             'course': ['Python', 'Java', 'C++', 'C#'],
             'grade': ['A', 'A+', 'B', 'B+'],
             'score': [90, 95, 85, 80],
             'percentage': [90, 95, 85, 80]}

df_dict = pd.DataFrame(data_dict)

print(f"DataFrame from dict: \n {df_dict}")


data_list_dict = [{'Name': 'Tom', 'Age': 20, 'city': 'New York', 'course': 'Python', 'grade': 'A', 'score': 90, 'percentage': 90}, {'Name': 'Nick', 'Age': 21, 'city': 'New York', 'course': 'Java', 'grade': 'A+', 'score': 95, 'percentage': 95}, {'Name': 'John', 'Age': 19, 'city': 'Los Angeles', 'course': 'C++', 'grade': 'B', 'score': 85, 'percentage': 85}, {'Name': 'Smith', 'Age': 18, 'city': 'Chicago', 'course': 'C#', 'grade': 'B+', 'score': 80, 'percentage': 80}]

df_list_dict = pd.DataFrame(data_list_dict)

print(f"DataFrame from list of dict: \n {df_list_dict}")