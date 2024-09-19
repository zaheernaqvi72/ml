dictionary = {'Sayed': 1, 'Ali': 2, 'Hassan': 3}

dictionary.update({'Sayed': 4, 'Ali': 5, 'Hassan': 6})

print(dictionary)
dictionary['John'] = 7
dictionary['Peter'] = 8

# Accessing dictionary elements
print(dictionary['Sayed'])  # Output: 4

# Updating dictionary elements
dictionary['Ali'] = 9
print(dictionary)  # Output: {'Sayed': 4, 'Ali': 9, 'Hassan': 6, 'John': 7, 'Peter': 8}

# Removing dictionary elements
del dictionary['Hassan']
print(dictionary)  # Output: {'Sayed': 4, 'Ali': 9, 'John': 7, 'Peter': 8}

# Checking if a key exists in the dictionary
print('John' in dictionary)  # Output: True
print('Hassan' in dictionary)  # Output: False

# Getting the number of key-value pairs in the dictionary
print(len(dictionary))  # Output: 4

# Getting a list of all keys in the dictionary
keys = list(dictionary.keys())
print(f"keys are: \n {keys}")  # Output: ['Sayed', 'Ali', 'John', 'Peter']

# Getting a list of all values in the dictionary
values = list(dictionary.values())
print(f"Values are: \n {values}")  # Output: [4, 9, 7, 8]

# Clearing the dictionary
# dictionary.clear()
# print(dictionary)  # Output: {}