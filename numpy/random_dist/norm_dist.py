import numpy as np

import matplotlib.pyplot as plt

# Generate random data from a normal distribution
mean = 0
std_dev = 1
size = 1000
data = np.random.normal(mean, std_dev, size)

# Plot the histogram of the data
plt.hist(data, bins=30, density=True, alpha=0.7)

# Plot the probability density function (PDF) of the normal distribution
x = np.linspace(-4, 4, 100)
pdf = (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std_dev) ** 2)
plt.plot(x, pdf, color='red', linewidth=2)

# Set plot labels and title
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.title('Normal Distribution')

# Show the plot
plt.show()