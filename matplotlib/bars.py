import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D', 'E']
values = [7, 13, 5, 17, 10]

plt.bar(categories, values, color = ['blue', 'green', 'orange', 'yellow', 'red'], edgecolor = 'black')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart')
plt.show()

