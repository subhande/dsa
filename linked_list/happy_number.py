# Happy Number


class Solution:
    def getSquares(self, n):
        total = 0
        while n:
            digit = n % 10
            total += digit**2
            n = n // 10
        return total
    def isHappy(self, n: int) -> bool:
        fast = self.getSquares(n)
        slow = n
        while fast != 1 and fast != slow:
            print([fast, slow])
            fast = self.getSquares(self.getSquares(fast))
            slow = self.getSquares(slow)
            print([fast, slow])
        return fast == 1
