class stack_ops:
    def __init__(self):
        self.stack = []

    def append(self,val):
        self.stack.append(val)
    def pop(self):
        self.stack.pop()
    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        return self.stack[-1]
    def add(self):
        if not self.stack:
            add =  self.stack.pop() + self.stack.pop()
            print(add)
        else:
            print("Stack is empty")
    def divide(self):
        d = self.stack.pop() / self.stack.pop()
        print(d)
    
s = stack_ops()
s.append(2)
s.append(4)
s.add()
s.divide()


