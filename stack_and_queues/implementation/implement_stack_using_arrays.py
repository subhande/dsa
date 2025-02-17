
# Implement a stack using arrays.

class ArrayStack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)


    def pop(self):
        if self.isEmpty():
            return -1
        return self.stack.pop()


    def top(self):
        if self.isEmpty():
            return -1
        return self.stack[-1]


    def isEmpty(self):
        return len(self.stack) == 0


if __name__ == '__main__':
    stack = ArrayStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.top())
    stack.pop()
    print(stack.top())
    stack.pop()
    print(stack.top())
    stack.pop()
    print(stack.isEmpty())
    stack.push(1)
    print(stack.isEmpty())
    print(stack.top())
    stack.pop()
    print(stack.isEmpty())
    print(stack.top())
    stack.pop()
    print(stack.isEmpty())
    print(stack.top())
