from StackMachine import StackOperations
from inputs import Inputs

#GATHERING INPUTS
myStack = StackOperations()
str = str.upper(input("enter your string here, separate your words using whitespace: "))
split = str.split()
print(str)

#OPERATIONAL FUNCTIONS
def pop():
    myStack.pop()
def sub():
    myStack.push(myStack.sub())
def dup():
    myStack.push(myStack.dup())
def add():
    myStack.push(myStack.add())

#CHECKLOOP
for item in split:
    try:
        int_value = int(item)
    except ValueError:
        if item=="DUP":
            dup()
            print( myStack.get_stack())
        elif item =="POP":
            pop()
            print( myStack.get_stack())
        elif item=="+":
            add()
            print( myStack.get_stack())
        elif item=="-":
            sub()
            print( myStack.get_stack())
        else :
            print("Your string of operations contain unknown please double check :" +item)
    else:
        myStack.push(item)
        print( myStack.get_stack())
print( myStack.get_stack())
