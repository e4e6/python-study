def AND(x1,x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1*w1 + x2*w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1
    
def NAND(x1,x2):
    w1, w2, theta = -0.5, -0.5, -0.7
    tmp = x1*w1 + x2*w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1
def OR(x1,x2):
    w1, w2, theta = 0.7, 0.7, 0.5
    tmp = x1*w1 + x2*w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1
def XOR(x1,x2):
    w1, w2, theta = -0.7, -0.7, -0.5
    tmp = x1*w1 + x2*w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1

print("(0,0), (0,1), (1,1)")
print("AND",AND(0,0), AND(0,1), AND(1,1))
print("NAND",NAND(0,0), NAND(0,1), NAND(1,1))
print("OR",OR(0,0), OR(0,1), OR(1,1))
print("XOR",XOR(0,0), XOR(0,1), XOR(1,1))