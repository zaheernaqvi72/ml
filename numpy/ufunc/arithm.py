import numpy

ar1 = numpy.array([1, 2, 3, 4])
ar2 = numpy.array([5, 6, 7, 8])


add = numpy.add(ar1, ar2)
print(f"Addition: {add}")

subt = numpy.subtract(ar1, ar2)
print(f"Subtraction: {subt}")

mult = numpy.multiply(ar1, ar2)
print(f"Multiplication: {mult}")

div = numpy.divide(ar1, ar2)
print(f"Division: {div}")

scalar_mult = numpy.multiply(ar1, 2)
print(f"Scalar Multiplication: {scalar_mult}")