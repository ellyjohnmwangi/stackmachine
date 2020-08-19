from StackMachine import StackOperations
from inputs import Inputs

#GATHERING INPUTS
myStack = StackOperations()
str = str.upper(input("enter your string here, separate your words using whitespace: "))
split = str.split()
print(str)
#TODO why do you have these functions redefined in this module while they already exist in StackMachine

#CHECKLOOP
for item in split:
    try:
        int_value = int(item)
    except ValueError:
        if item=="DUP":  #TODO are you considering case sensitivity in this comparision
            myStack.push(myStack.dup())

        elif item =="POP":
            myStack.pop()

        elif item=="+":
            myStack.push(myStack.add())

        elif item=="-":
            myStack.push(myStack.sub())

        else :
            print("Your string of operations contain unknown please double check :" +item)
    else:
        if int(item) >  2**(20-1):
            raise Exception('Sorry your input: '+item +' is above range.')
        myStack.push(item)

print( myStack.get_stack())
