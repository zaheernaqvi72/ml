import matplotlib.pyplot as plt
import numpy as np

x_points = np.array([1, 2, 3, 4, 5])
y_points = x_points ** 2

plt.plot(x_points, y_points, marker = 'o' , linestyle = 'none', color = 'red', label = 'y = x^2')
xlabel = plt.xlabel('x')
ylabel = plt.ylabel('y')
title = plt.title('y = x^2')
legend = plt.legend()

plt.show()