import numpy as np

x = np.array([[1,2],[3,5]])
y = np.array([[4,5],[6,7]])

print("x: \n", x)
print(x.shape)
print(x.dtype)

print("y: \n", y)
print(y.shape)
print(y.dtype)

print("x-10: \n", x-10)
print((x-10).shape)
print((x-10).dtype)

print("x+y: \n", x+y)
print((x+y).shape)
print((x+y).dtype)

print("x*y: \n", x*y)
print((x*y).shape)
print((x*y).dtype)