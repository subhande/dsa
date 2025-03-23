# Best Time To Buy And Sell Stock With Cooldown
from typing import List


class Solution:
    def maxProfitRecursive(self, ind, buy, prices, memo):
        if ind >= len(prices):
            return 0

        if memo[ind][buy] != -1:
            return memo[ind][buy]

        profit = 0
        if buy == 0:
            profit = max(
                0 + self.maxProfitRecursive(ind+1, 0, prices, memo),
                -prices[ind] + self.maxProfitRecursive(ind+1, 1, prices, memo)
            )
        else:
            profit = max(
                0 + self.maxProfitRecursive(ind+1, 1, prices, memo),
                prices[ind] + self.maxProfitRecursive(ind+2, 0, prices, memo)
            )
        memo[ind][buy] = profit
        return memo[ind][buy]

    def maxProfitTabular(self, prices):
        n = len(prices)
        dp = [[-1, -1] for i in range(n+1)]
        dp[n][0] = dp[n][1] = 0

        # Loop through the array in reverse order
        for ind in range(n - 1, -1, -1):
            for buy in range(2):
                profit = 0
                # We can buy the stock
                if buy == 0:
                    profit = max(0 + dp[ind + 1][0], (-1)*prices[ind] + dp[ind + 1][1])

                # We can sell the stock
                if buy == 1:
                    if ind > n - 2:
                        profit = max(0 + dp[ind + 1][1], prices[ind])
                    else:
                        profit = max(0 + dp[ind + 1][1], prices[ind] + dp[ind + 2][0])

                dp[ind][buy] = profit

        return dp[0][0]
    def maxProfit(self, prices: List[int]) -> int:
        return self.maxProfitTabular(prices)
        n = len(prices)
        memo = [[-1, -1] for i in range(n)]
        return self.maxProfitRecursive(0, 0, prices, memo)
