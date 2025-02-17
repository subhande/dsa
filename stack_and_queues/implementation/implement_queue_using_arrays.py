# Implement Queue using arrays.

class ArrayQueue:
    def __init__(self):
        self.queue = []

    def push(self, x):
        self.queue.append(x)

    def pop(self):
        if self.isEmpty():
            return -1
        return self.queue.pop(0)


    def peek(self):
        if self.isEmpty():
            return -1
        return self.queue[0]


    def isEmpty(self):
        return len(self.queue) == 0

if __name__ == '__main__':
    queue = ArrayQueue()
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
