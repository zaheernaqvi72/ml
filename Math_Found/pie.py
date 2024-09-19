import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15, 20, 30, 40, 25])
mylabels = ["Apples", "Bananas", "Cherries", "Dates", "Elderberries", "Figs", "Grapes", "Honeydew"]

plt.pie(y, labels = mylabels)
plt.show() 