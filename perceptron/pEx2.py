import numpy as np 

x = np.array([0,1])
w = np.array([0.5,0.5])
b = -0.7 # b = bias = -1 * theta
print("x,w,b:",x,w,b)
print("x*w:",x*w)
print("np.sum(x*w):",np.sum(x*w)+b)
