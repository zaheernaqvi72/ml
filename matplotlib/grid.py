import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y)
plt.grid(color='r', linestyle='--', linewidth=0.5)
plt.show()

plt.subplot(1,2,1)
plt.plot(x, y)
plt.grid(color='r', linestyle='--', linewidth=0.5)

plt.subplot(1,2,2)
plt.plot(x, [i**2 for i in y])
plt.grid(color='b', linestyle='-', linewidth=0.5)
plt.show()