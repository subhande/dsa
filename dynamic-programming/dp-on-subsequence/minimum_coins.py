# Minimum Coins

from typing import List

class Solution:
    # 1. Recursive Method
    # This function uses a recursive approach to find the minimum number of coins needed to make up the given amount.
    # It explores all possible combinations by subtracting each coin from the amount.
    def MinimumCoinsRecursive(self, coins, amount):
        def helper(coins, amount):
            if amount == 0:
                return 0
            if amount < 0:
                return float('inf')

            min_coins = float('inf')
            for coin in coins:
                result = helper(coins, amount - coin)
                if result != float('inf'):
                    min_coins = min(min_coins, result + 1)

            return min_coins

        result = helper(coins, amount)
        return result if result != float('inf') else -1

    def MinimumCoinsRecursiveHelper(self, index, coins, amount):
        if amount == 0:
            return 0
        if index == 0 and amount % coins[0] == 0:
            return amount // coins[0]
        if index == 0 or amount < 0:
            return float('inf')

        # Exclude the current coin
        exclude_current = self.MinimumCoinsRecursiveHelper(index - 1, coins, amount)

        # Include the current coin

        include_current = 0
        if coins[index] <= amount:
            result = self.MinimumCoinsRecursiveHelper(index, coins, amount - coins[index])
            if result != float('inf'):
                include_current = result + 1

        return min(exclude_current, include_current)

    # 2. Memoization
    # Memoization approach to optimize recursion by storing intermediate results.
    # This avoids redundant calculations and significantly improves performance.
    def MinimumCoinsMemoization(self, coins, amount):
        def helper(coins, amount, memo):
            if amount == 0:
                return 0
            if amount < 0:
                return float('inf')
            if amount in memo:
                return memo[amount]

            min_coins = float('inf')
            for coin in coins:
                result = helper(coins, amount - coin, memo)
                if result != float('inf'):
                    min_coins = min(min_coins, result + 1)

            memo[amount] = min_coins
            return min_coins

        result = helper(coins, amount, {})
        return result if result != float('inf') else -1

    # 3. Tabulation
    def MinimumCoinsTabular(self, coins, amount):
        n = len(coins)
        dp = [[float('inf')] * (amount + 1) for _ in range(n + 1)]

        # Base case: 0 coins needed to make amount 0
        for i in range(n + 1):
            dp[i][0] = 0

        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                if coins[i - 1] <= j:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - coins[i - 1]] + 1)
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n][amount] if dp[n][amount] != float('inf') else -1

    # 4. Space Optimization
    def MinimumCoinsSpaceOptimized(self, coins, amount):
        prev = [float('inf')] * (amount + 1)
        prev[0] = 0

        for i in range(1, amount + 1):
            current = float('inf')
            for coin in coins:
                if i - coin >= 0:
                    current = min(current, prev[i - coin] + 1)
            prev[i] = current

        return prev[amount] if prev[amount] != float('inf') else -1

    # 4. Space Optimization
    def coinChange(self, coins: List[int], amount: int) -> int | float:
        noOfCoins = [float('inf')] * (amount + 1)
        noOfCoins[0] = 0

        for coin in coins:
            for i in range(1, amount + 1):
                if i - coin >= 0:
                    noOfCoins[i] = min(noOfCoins[i], noOfCoins[i - coin] + 1)

        return noOfCoins[amount] if noOfCoins[amount] != float('inf') else -1

# Example usage
if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11
    solution = Solution()

    print("Recursive:", solution.MinimumCoinsRecursive(coins, amount))
    print("Memoization:", solution.MinimumCoinsMemoization(coins, amount))
    print("Tabular:", solution.MinimumCoinsTabular(coins, amount))
    print("Space Optimized:", solution.MinimumCoinsSpaceOptimized(coins, amount))
