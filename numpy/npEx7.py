import numpy as np

A = np.array([[[1,1],[2,2],],[[3,3],[4,4],], [[5,5],[6,6],], [[7,7],[8,8],],])
print("A:\n", A)
print("A>2:\n",A>2)
print("A[A>2]:\n",A[A>2])