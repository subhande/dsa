# Best Time To Buy And Sell Stock III
from typing import List


class Solution:
    def maxProfitRecursive(self, ind, buy, cap, prices, memo):
        if ind == len(prices) or cap == 0:
            return 0

        if memo[ind][buy][cap] != -1:
            return memo[ind][buy][cap]

        profit = 0
        if buy == 0:
            profit = max(
                0 + self.maxProfitRecursive(ind+1, 0, cap, prices, memo),
                -prices[ind] + self.maxProfitRecursive(ind+1, 1, cap, prices, memo)
            )
        else:
            profit = max(
                0 + self.maxProfitRecursive(ind+1, 1, cap, prices, memo),
                prices[ind] + self.maxProfitRecursive(ind+1, 0, cap-1, prices, memo)
            )
        memo[ind][buy][cap] = profit
        return memo[ind][buy][cap]

    def maxProfitTabular(self, prices, max_cap):
        n = len(prices)
        dp = [[[0] * max_cap for _ in range(2)] for _ in range(n+1)]

        # Loop through the array in reverse order
        for ind in range(n - 1, -1, -1):
            for buy in range(2):
                for cap in range(1, max_cap):
                    profit = 0
                    # We can buy the stock
                    if buy == 0:
                        profit = max(0 + dp[ind + 1][0][cap], (-1)*prices[ind] + dp[ind + 1][1][cap])
                    # We can sell the stock
                    if buy == 1:
                        profit = max(0 + dp[ind + 1][1][cap], prices[ind] + dp[ind + 1][0][cap-1])
                    dp[ind][buy][cap] = profit

        return dp[0][0][max_cap-1]


    def maxProfitTabularSpaceOptimized(self, prices, max_cap):
        n = len(prices)
        ahead = [[0] * max_cap for _ in range(2)]
        curr = [[0] * max_cap for _ in range(2)]

        for ind in range(n - 1, -1, -1):
            for buy in range(2):
                for cap in range(1, max_cap):
                    if buy == 0:
                        curr[buy][cap] = max(0 + curr[0][cap], (-1)*prices[ind] + curr[1][cap])
                    if buy == 1:
                        curr[buy][cap] = max(0 + curr[1][cap], prices[ind] + curr[0][cap-1])
            ahead = [row[:] for row in curr]

        return ahead[0][max_cap-1]


    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        cap = 3
        memo = [[[-1] * cap for _ in range(2)] for _ in range(n)]
        # return self.maxProfitRecursive(0, 0, cap-1, prices, memo)
        # return self.maxProfitTabular(prices, cap)
        return self.maxProfitTabularSpaceOptimized(prices, cap)
