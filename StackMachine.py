# THIS CLASS INITIATES THE STACK AND THE OPERATIONS ARE DEFINED
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
        return int(self.pop())+int(self.pop())
    def sub(self):
        return int(self.pop())-int(self.pop())
