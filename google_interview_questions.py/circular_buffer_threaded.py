# Circular Buffer with threading


import threading
import time

class ThreadSafeCircularBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = [None] * size
        self.head = 0
        self.tail = 0
        self.count = 0

        # Synchronization primitives
        self.lock = threading.Lock()
        self.not_full = threading.Condition(self.lock)
        self.not_empty = threading.Condition(self.lock)

    def enqueue(self, item):
        with self.not_full:
            while self.count == self.size:
                self.not_full.wait()  # Wait until buffer has space

            self.buffer[self.tail] = item
            self.tail = (self.tail + 1) % self.size
            self.count += 1

            # Notify waiting threads that buffer isn't empty anymore
            self.not_empty.notify()

    def dequeue(self):
        with self.not_empty:
            while self.count == 0:
                self.not_empty.wait()  # Wait until buffer has data

            item = self.buffer[self.head]
            self.buffer[self.head] = None  # Optional: clear slot
            self.head = (self.head + 1) % self.size
            self.count -= 1

            # Notify waiting threads that buffer has space now
            self.not_full.notify()

            return item

    def __repr__(self):
        with self.lock:
            return f"ThreadSafeCircularBuffer({self.buffer}, head={self.head}, tail={self.tail}, count={self.count})"


if __name__ == "__main__":



    def producer(cb, items):
        for item in items:
            cb.enqueue(item)
            print(f"Produced {item}")
            time.sleep(0.1)

    def consumer(cb, consume_count):
        for _ in range(consume_count):
            item = cb.dequeue()
            print(f"Consumed {item}")
            time.sleep(0.15)

    buffer = ThreadSafeCircularBuffer(5)

    producer_thread = threading.Thread(target=producer, args=(buffer, range(10)))
    consumer_thread = threading.Thread(target=consumer, args=(buffer, 10))

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()
