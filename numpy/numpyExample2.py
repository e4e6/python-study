import numpy as np
x = np.array([0,1,2])
y = np.array([1,2,3])
z = np.array([2,3])
print(x/y)
#print(x+z) # 두 배열의 원소의 수가 다르면 오류 발생 ValueError: operands could not be broadcast together with shapes (3,) (2,)

print(x/2)