import numpy as np
from scipy import constants, special

result_add = np.add(1, 2)
result_exp = np.exp(2)
result_pi = constants.pi
result_jn = special.jn(2, 3)

print(f"Addition: {result_add}")
print(f"Exponential: {result_exp}")
print(f"Pi: {result_pi}")
print(f"Bessel function: {result_jn}")

