from numpy import random as rd
import matplotlib.pyplot as plt
import seaborn as sns


sns.distplot(rd.uniform(size=1000), hist=False, label='normal')
sns.distplot(rd.binomial(n=1000, p=0.01, size=1000), hist=False, label='binomial')
sns.distplot(rd.normal(size=1000), hist=False, label='normal')
plt.show()