# Stock Spanner



class StockSpanner:

    def __init__(self):
        self.stack = []
        self.index = 0

    def next(self, price: int) -> int:
        if not self.stack:
            self.stack.append((price, self.index))
            days = self.index + 1
            self.index += 1
            return days
        else:
            while self.stack and self.stack[-1][0] <= price:
                self.stack.pop()

            days = self.index+1 if not self.stack else self.index - self.stack[-1][1]

            self.stack.append((price, self.index))
            self.index += 1
            return days
