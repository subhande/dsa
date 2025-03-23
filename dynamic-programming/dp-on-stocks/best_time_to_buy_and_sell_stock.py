# Best Time To Buy And Sell Stock
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = 10**9
        maxProfit = 0
        for i in range(len(prices)):
            profit = prices[i] - minPrice
            maxProfit = max(maxProfit, profit)
            minPrice = min(minPrice, prices[i])
        return maxProfit
