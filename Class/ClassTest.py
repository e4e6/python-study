class ClassNum :
    # 생성자 : __init__ 객체 : self
    def __init__ (self, one : str = "zero"): 
        self.one = one
    def print(self):
        print(self.one)
    def printTwo():
        print("two")

classOne = ClassNum("one")


ClassNum().print()
classOne.print()
ClassNum.printTwo()

# classOne.printTwo()
#TypeError: ClassNum.printTwo() takes 0 positional arguments but 1 was given
# ClassNum.print()
#TypeError: ClassNum.print() missing 1 required positional argument: 'self'