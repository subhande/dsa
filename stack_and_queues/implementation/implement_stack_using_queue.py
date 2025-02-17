from queue import Queue

class QueueStack:
    def __init__(self):
        self.queue = Queue()

    def push(self, x):
        self.queue.put(x)
        for _ in range(self.queue.qsize() - 1):
            self.queue.put(self.queue.get())

    def pop(self):
        if self.isEmpty():
            return -1
        return self.queue.get()

    def top(self):
        if self.isEmpty():
            return -1
        return self.queue.queue[0]

    def isEmpty(self):
        return self.queue.empty()


if __name__ == '__main__':
    stack = QueueStack()
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
