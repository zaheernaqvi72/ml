import matplotlib.pyplot as plt

x = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
y = [1, 9, 2, 8, 3, 7, 4, 6, 5, 5]

plt.scatter(x, y, label = 'Data 1', color = 'r', s = 10, marker = "o", edgecolors='k')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Scatter Plot')
plt.legend()
plt.show()