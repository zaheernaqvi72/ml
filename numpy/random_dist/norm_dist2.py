from numpy import random as rnd
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(rnd.normal(size=1000))

plt.show()