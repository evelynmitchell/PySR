import numpy as np
from pysr import pysr
X = np.random.randn(100, 5)

# Test 1
y = X[:, 0]
equations = pysr(X, y,
                 niterations=100)
print(equations)
assert equations.iloc[-1]['MSE'] < 1e-10

# Test 2
y = X[:, 0]**2
equations = pysr(X, y,
                 unary_operators=["square(x) = x^2"], binary_operators=["plus"],
                 niterations=100)
print(equations)
assert equations.iloc[-1]['MSE'] < 1e-10
