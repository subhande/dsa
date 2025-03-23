# Best Time To Buy And Sell Stock With Transaction Fee
from typing import List


class Solution:
    def maxProfitRecursive(self, ind, buy, prices, memo, fee):
        if ind == len(prices):
            return 0

        if memo[ind][buy] != -1:
            return memo[ind][buy]

        profit = 0
        if buy == 0:
            profit = max(
                0 + self.maxProfitRecursive(ind+1, 0, prices, memo, fee),
                -prices[ind] + self.maxProfitRecursive(ind+1, 1, prices, memo, fee)
            )
        else:
            profit = max(
                0 + self.maxProfitRecursive(ind+1, 1, prices, memo, fee),
                prices[ind]-fee + self.maxProfitRecursive(ind+1, 0, prices, memo, fee)
            )
        memo[ind][buy] = profit
        return memo[ind][buy]

    def maxProfitTabular(self, prices, fee):
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
                    profit = max(0 + dp[ind + 1][1], prices[ind] - fee + dp[ind + 1][0])

                dp[ind][buy] = profit

        return dp[0][0]

    def maxProfitOptimal(self, prices: List[int], fee) -> int:
        profit = 0
        n = len(prices)
        for i in range(1, n):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1] - fee
        return profit


    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        memo = [[-1, -1] for i in range(n)]
        return self.maxProfitRecursive(0, 0, prices, memo, fee)
        return self.maxProfitTabular(prices, fee)
        return self.maxProfitOptimal(prices, fee)
