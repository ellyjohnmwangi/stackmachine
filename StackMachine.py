# THIS CLASS INITIATES THE STACK AND THE OPERATIONS ARE DEFINED
class StackOperations:

    def __init__(self):
        self.items = []

    def is_empty(self):
        if not self.items:
            print('-1')

    def get_stack(self):
        return self.items[-1]

    def push(self, item):
        self.items.append(item)

    def error(self):
        self.push(-1)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            self.error()

    def dup(self):
        try:
            return self.push(self.items[-1])
        except IndexError:
            self.error()

    def add(self):
        if self.is_empty() is True:
            self.error()
        else:
            try:
                return self.push(int(self.pop())+int(self.pop()))
            except TypeError:
                exit()

    def sub(self):
        if self.is_empty() is True:
            self.error()
        else:
            try:
                if int(self.pop()) - int(self.pop()) < 0:
                    self.error()
                else:
                    self.push(int(self.pop())-int(self.pop()))
            except TypeError:
                exit()

