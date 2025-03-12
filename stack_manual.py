class stack:
    def __init__(self):
        self.stack = []
    def append(self,val):
        self.stack.append(val)
    def pop(self):
        if not self.is_empty():
            self.stack.pop()
        return "stack empty"
    def peep(self):
        if not self.stack.is_empty():
            self.stack[-1]
    def size(self):
        return len(self.stack)
    def is_empty(self):
        return len(self.stack) == 0
    

s = stack()
s.append(1)
s.append(23)
print(s.stack)