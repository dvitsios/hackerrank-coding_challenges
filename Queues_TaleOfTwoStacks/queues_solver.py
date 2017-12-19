class MyQueue(object):
    def __init__(self):
        self.inStack = []
        self.outStack = []
    
    def peek(self):
        if self.outStack:
            return self.outStack[-1]
        else:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
            return self.outStack[-1]
        
    def pop(self):
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        return self.outStack.pop()
        
    def put(self, value):
        self.inStack.append(value)
                
queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
        
