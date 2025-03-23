# Best Time To Buy And Sell Stock II
from typing import List


class Solution:
    def maxProfitRecursive(self, ind, buy, prices, memo):
        if ind == len(prices):
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
                prices[ind] + self.maxProfitRecursive(ind+1, 0, prices, memo)
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
                    profit = max(0 + dp[ind + 1][1], prices[ind] + dp[ind + 1][0])

                dp[ind][buy] = profit

        return dp[0][0]

    def maxProfitTabularForward(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        dp = [[0, 0] for _ in range(n)]
        dp[0][0] = 0           # No stock held on day 0
        dp[0][1] = -prices[0]  # Bought stock on day 0

        for ind in range(1, n):
            # Maximum profit if not holding a stock today:
            dp[ind][0] = max(
                0 + dp[ind-1][0],
                prices[ind] + dp[ind-1][1]
            )
            # Maximum profit if holding a stock today:
            dp[ind][1] = max(
                0 + dp[ind-1][1],
                (-1) * prices[ind] + dp[ind-1][0]
            )

        return dp[n-1][0]

    def maxProfitOptimal(self, prices: List[int]) -> int:
        profit = 0
        n = len(prices)
        for i in range(1, n):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit


    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = [[-1, -1] for i in range(n)]
        return self.maxProfitRecursive(0, 0, prices, memo)
        return self.maxProfitTabular(prices)
        return self.maxProfitTabularForward(prices)
        return self.maxProfitOptimal(prices)
