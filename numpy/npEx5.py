import numpy as np
A = np.array([[[1,1],[1,1],],[[2,2],[2,2],], [[3,3],[3,3],], [[4,4],[5,5],],])
B = np.array([1,-1])
print(A*B)

print("A[0]:\n", A[0])
print("A[0][1]:\n", A[0][1])
print("A[0][1][0]:\n", A[0][1][0])

print("for 1:")
for first in A:
    print(first)

print("for 2:")
for first,second in A:
    print(first,second)