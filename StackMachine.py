class StackOperations():
    def __init__(self):
        self.items = []
    def is_empty(self):
        if self.items == []:
            print('-1')
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def get_stack(self):
        return self.items
    def dup(self):
        if not self.is_empty():
            return self.items[-1]
    def add(self):
        return self.pop()+self.pop()
    def sub(self):
        return self.pop()-self.pop()


myStack = StackOperations()

# myStack.push(1)
# myStack.push(2)
# myStack.push(3)
# myStack.push(4)
# myStack.push(5)
# myStack.push(6)
# print("initial stack is:{}".format(myStack.get_stack()))
# myStack.push(myStack.dup())
# print("Stack after Dup func is called: {}".format(myStack.get_stack()))
# myStack.push(myStack.add())
# print("Stack after Add function:{}".format(myStack.get_stack()))
# myStack.push(myStack.sub())
# print("Stack after Sub function:{}".format(myStack.get_stack()))
# print(myStack.get_stack())
