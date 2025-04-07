# Circular Buffer

class CircularBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = [None] * size
        self.head = 0  # points to next element to read
        self.tail = 0  # points to next element to write
        self.count = 0

    def is_full(self):
        return self.count == self.size

    def is_empty(self):
        return self.count == 0

    def enqueue(self, item):
        if self.is_full():
            raise OverflowError("Circular buffer is full")
        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) % self.size
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Circular buffer is empty")
        item = self.buffer[self.head]
        self.buffer[self.head] = None  # Optional: clear the slot
        self.head = (self.head + 1) % self.size
        self.count -= 1
        return item

    def __repr__(self):
        return f"CircularBuffer({self.buffer}, head={self.head}, tail={self.tail}, count={self.count})"


if __name__ == "__main__":
    cb = CircularBuffer(3)

    cb.enqueue(10)
    cb.enqueue(20)
    cb.enqueue(30)

    print(cb)  # CircularBuffer([10, 20, 30], head=0, tail=0, count=3)

    try:
        cb.enqueue(40)  # should raise an OverflowError
    except OverflowError as e:
        print(e)

    print(cb.dequeue())  # 10
    print(cb.dequeue())  # 20

    cb.enqueue(40)
    print(cb)  # CircularBuffer([40, None, 30], head=2, tail=1, count=2)
