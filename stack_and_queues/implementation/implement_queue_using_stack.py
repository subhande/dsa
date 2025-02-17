# Implement a queue using stacks

class StackQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        # stack 1: [1, 2, 3]
        # push 4
        # stack 2: [3, 2, 1]
        # stack 1: [4]
        # stack 2: [3, 2, 1]
        # stack 1: [4, 1, 2, 3]
        # pop: 3
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(x)
        while self.stack2:
            self.stack1.append(self.stack2.pop())


    def pop(self):
        if self.isEmpty():
            return -1
        return self.stack1.pop()


    def peek(self):
        if self.isEmpty():
            return -1
        return self.stack1[-1]


    def isEmpty(self):
        return len(self.stack1) == 0


if __name__ == '__main__':
    queue = StackQueue()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    print(queue.peek())
    queue.pop()
    print(queue.peek())
    queue.pop()
    print(queue.peek())
    queue.pop()
    print(queue.isEmpty())
    queue.push(1)
    print(queue.isEmpty())
    print(queue.peek())
    queue.pop()
    print(queue.isEmpty())
    print(queue.peek())
    queue.pop()
    print(queue.isEmpty())
    print(queue.peek())
