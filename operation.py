from StackMachine import StackOperations

<<<<<<< HEAD
# GATHERING INPUTS
myStack = StackOperations()
my_str = str.upper(input("enter your string here, separate your words using whitespace: "))
split = my_str.split()
print(my_str)

# CHECK LOOP
=======
#TODO do not igore pep8 formatting warnings. there is a lot of warnings in your code on bad formatting

# GATHERING INPUTS
myStack = StackOperations()
str = str.upper(input("enter your string here, separate your words using whitespace: ")) #TODO str???
split = str.split()
print(str)

# CHECKLOOP
>>>>>>> 7bb4ff408fa444e378fc9997c6bd48558562f722
for item in split:
    try:
        int_value = int(item) #TODO where is this int_value being used?
    except ValueError:
        if item == "DUP":
<<<<<<< HEAD
            myStack.push(myStack.dup())
=======
            myStack.push(myStack.dup()) #TODO changes in
>>>>>>> 7bb4ff408fa444e378fc9997c6bd48558562f722

        elif item == "POP":
            myStack.pop()

        elif item == "+":
<<<<<<< HEAD
            myStack.push(myStack.add())

        elif item == "-":
            myStack.push(myStack.sub())
        else:
            print("Your string of operations contain unknown please double check :" + item)
    else:
        if int(item) > 2**(20-1):
            raise Exception('Sorry your input: '+item + 'is above range.')
=======
            myStack.push(myStack.add()) #TODO complex code

        elif item == "-":
            myStack.push(myStack.sub()) #TODO complex code

        else:
            print("Your string of operations contain unknown please double check :" + item)
    else:
        if int(item) > 2 ** (20 - 1): #TODO is this how you do power in python. do not reinvent wheel
            raise Exception('Sorry your input: ' + item + ' is above range.')
>>>>>>> 7bb4ff408fa444e378fc9997c6bd48558562f722
        myStack.push(item)

print(myStack.get_stack())
