from StackMachine import StackOperations
from inputs import Inputs

#GATHERING INPUTS
myStack = StackOperations()
myoperations = Inputs()
str = input("enter your string here, separate your words using whitespace: ")
split = str.split()


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
        if item=="dup":
            dup()
        elif item =="pop":
            pop()
        # elif item=="+":
        #     myStack.push(pop()+pop())

        #     add()
        # elif item=="-":
            # myStack.sub()
        else :
            print("Your string of operations contain unknown {}: ")
    else:
        myStack.push(item)
for word in str:
    if word == "add":
        add()
    elif word == "sub":
        sub()


print(myStack.get_stack())

# for item in myoperations.get_inputs():
#     if
#     if pushUp:
#         myStack.push(word)
#         pushUp = False
#     elif word == "push":
#         pushUp= True
#     else:
#        try:
#             operation[word]()
#        except KeyError:
#             continue
