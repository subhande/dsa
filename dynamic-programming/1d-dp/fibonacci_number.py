# Fibonacci Number
# https://leetcode.com/problems/fibonacci-number/description/


class Solution:
    def fib(self, n: int, dp={}) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if dp.get(n) is not None:
            return dp[n]
        return self.fib(n-1, dp) + self.fib(n-2, dp)
