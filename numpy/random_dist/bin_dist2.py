from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# Normal Distribution is a continuous probability distribution.
sns.distplot(random.normal(loc= 50, scale=5, size = 1000), label="Normal", hist=False)

# Binomial Distribution is a discrete probability distribution.
sns.distplot(random.binomial(n= 100, p=0.5, size=1000), label="Binomial", hist=False)

plt.show()