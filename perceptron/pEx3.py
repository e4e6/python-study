import numpy as np

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
    
def XOR(x1,x2) :
    x = np.array([x1,x2])
    w = np.array([-0.5,-0.5])
    b = 0.3

    if np.sum(x*w)+b <= 0:
        return 0
    else: 
        return 1

print(NAND(1,1), NAND(1,0))
print(OR(1,1), OR(1,0), OR(0,0))
print(XOR(1,1), XOR(1,0), XOR(0,0))