from scipy.optimize import minimize_scalar as ms
from scipy.optimize import differential_evolution as de

def quadratic(x):
    return x**2 + 5

result = ms(quadratic)

print(f"Minimum value of the function: {result.fun}")
print("Minimum value of x: ", result.x)


def global_objective(x):
    return x[0]**2 + x[1]**2

result2 = de(global_objective, [(-5, 5), (-5, 5)])

print(f"Minimum value of the function: {result2.fun}")
print("Minimum value of x: ", result2.x)