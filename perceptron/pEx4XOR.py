import numpy as np

def AND(x1,x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1*w1 + x2*w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1
    
def NAND(x1,x2) :
    x = np.array([x1,x2])
    w = np.array([-0.5,-0.5])
    b = 0.8

    if np.sum(x*w)+b <= 0:
        return 0
    else: 
        return 1

def OR(x1,x2) :
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.3

    if np.sum(x*w)+b <= 0:
        return 0
    else: 
        return 1
    
def XOR(x1, x2):
    return AND(OR(x1,x2),NAND(x1,x2))

print(XOR(1,1), XOR(1,0), XOR(0,1), XOR(0,0))