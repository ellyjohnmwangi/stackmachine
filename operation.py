from StackMachine import StackOperations

# GATHERING INPUTS
myStack = StackOperations()
my_str = str.upper(input("enter your string here, separate your words using whitespace: "))
split = my_str.split()
print(my_str)

# CHECK LOOP
for item in split:
    try:
        int_value = int(item)
    except ValueError:
        if item == "DUP":
            myStack.push(myStack.dup())

        elif item == "POP":
            myStack.pop()

        elif item == "+":
            myStack.push(myStack.add())

        elif item == "-":
            myStack.push(myStack.sub())
        else:
            print("Your string of operations contain unknown please double check :" + item)
    else:
        if int(item) > 2**(20-1):
            raise Exception('Sorry your input: '+item + 'is above range.')
        myStack.push(item)

print(myStack.get_stack())
