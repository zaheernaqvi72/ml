import matplotlib.pyplot as plt

data = [60, 64, 57, 56, 62, 60, 60, 61, 60, 59, 63, 60, 60, 61]

plt.hist(data, edgecolor='y', color='g')
plt.title('Histogram of IQ')
plt.xlabel('IQ')
plt.ylabel('Frequency')
plt.show()