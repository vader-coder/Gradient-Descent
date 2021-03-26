import function
import math
function = function.function
import numpy as np

#we are going to try descent with f(x, y) = x^2 + y^2
#only minimum that should work is (0, 0)

def magnitude(vector):
    count = 0
    for entry in vector:
        count += (entry*entry)
    return math.sqrt(count)

def getUnitVector(vector):
    mag = magnitude(vector)
    for i in range(len(vector)):
        vector[i] /= mag
    return vector

#might be better to use a vector type.

func = function([1, 1], [2, 2])
gradient = func.gradient(True)
testVector = [1, 1]
pointGradient = np.array(gradient.evaluate(testVector))
#problem; this is a scalar valued function. how do we step in direction from its output.
print(gradient.evaluate([1, 1]))
print(pointGradient)
unitvector = pointGradient / np.linalg.norm(pointGradient)
# getUnitVector(pointGradient)
print(unitvector)

