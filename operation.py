from StackMachine import StackOperations
from inputs import Inputs

#TODO do not igore pep8 formatting warnings. there is a lot of warnings in your code on bad formatting

# GATHERING INPUTS
myStack = StackOperations()
str = str.upper(input("enter your string here, separate your words using whitespace: ")) #TODO str???
split = str.split()
print(str)

# CHECKLOOP
for item in split:
    try:
        int_value = int(item) #TODO where is this int_value being used?
    except ValueError:
        if item == "DUP":
            myStack.push(myStack.dup()) #TODO changes in

        elif item == "POP":
            myStack.pop()

        elif item == "+":
            myStack.push(myStack.add()) #TODO complex code

        elif item == "-":
            myStack.push(myStack.sub()) #TODO complex code

        else:
            print("Your string of operations contain unknown please double check :" + item)
    else:
        if int(item) > 2 ** (20 - 1): #TODO is this how you do power in python. do not reinvent wheel
            raise Exception('Sorry your input: ' + item + ' is above range.')
        myStack.push(item)

print(myStack.get_stack())
