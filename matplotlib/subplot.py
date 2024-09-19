import matplotlib.pyplot as plt

plt.subplot(2,2,1)
plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25])
plt.title('First Plot')

plt.subplot(2,2,2)
plt.plot([5, 4, 3, 2, 1], [1, 4, 9, 16, 25], color = 'g')
plt.title('Second Plot')

plt.subplot(2,2,3)
plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25], color = 'r')
plt.title('Third Plot')

plt.subplot(2,2,4)
plt.plot([5, 4, 3, 2, 1], [1, 4, 9, 16, 25], color = 'purple')  
plt.title('Fourth Plot')

plt.show()