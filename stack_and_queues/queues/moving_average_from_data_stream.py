# Moving average from data stream


class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = []

    def next(self, val: int) -> float:

        if len(self.queue) == self.size:
            self.queue.pop(0)

        self.queue.append(val)

        return sum(self.queue) / len(self.queue)
