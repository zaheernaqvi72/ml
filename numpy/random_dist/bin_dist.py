import numpy as np
import matplotlib.pyplot as plt

n, p, size = 100, 0.5, 1000
binom = np.random.binomial(n, p, size)

count, bins, ignored = plt.hist(binom, bins=20, density=True)
plt.show()