# Initial list of integers and characters
lis = [1,2,3,4,5,6,7,8,9,10, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
lis2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# Removing the first element (0th index) from the list 'lis' would be done with:
# del lis[0]  # Uncomment to remove the first element.

# Adding an element to the end of 'lis'
lis.append(11)
print(lis)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 11]

# Inserting an element at the beginning (0th index) of 'lis'
lis.insert(0, 0)
print(lis)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 11]

# Extending 'lis' by appending all elements of 'lis2'
lis.extend(lis2)
print(lis)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# Sorting 'lis2' in ascending order
lis2.sort()
print(lis2)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Creating a copy of 'lis2'
list3 = lis2.copy()
print(list3)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Sorting 'lis2' in descending order
lis2.sort(reverse=True)
print(lis2)  # Output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# List of fruits
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# List comprehension to filter fruits containing the letter 'a'
newlist = [x for x in fruits if "a" in x]
print(newlist)  # Output: ['apple', 'banana', 'mango']

# Reversing the order of elements in 'lis2'
lis2.reverse()
print(lis2)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Removing and returning the last item of the list
last_item = lis.pop()
print(last_item)  # Output: 1 (last item before removal)
print(lis)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

# Removing the first occurrence of the value 4 from the list
lis.remove(4)
print(lis)  # Output: [0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 11, 10, 9, 8, 7, 6, 5, 3, 2]

# Getting the index of the first occurrence of the value 6
index_of_6 = lis.index(6)
print(index_of_6)  # Output: 5 (position of value 6 in the list)

# Counting the number of occurrences of the value 10 in the list
count_10 = lis.count(10)
print(count_10)  # Output: 2 (number of times 10 appears in the list)

# Clearing all elements from the list
lis.clear()
print(lis)  # Output: []

# Adding elements to the list again for demonstration
lis = [1, 2, 3]
print(lis)  # Output: [1, 2, 3]
