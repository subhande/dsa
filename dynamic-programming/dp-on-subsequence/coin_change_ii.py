"""
Coin change II

Give an array coins of n integers representing different coin denominations. Your task is to find the number of distinct combinations that sum up to a specified amount of money. If it's impossible to achieve the exact amount with any combination of coins, return 0. Single coin can be used any number of times. Return your answer with modulo 10^9+7.

-------------------------------------------------------------

Examples:
Input: coins = [2, 4,10], amount = 10
Output: 4
Explanation: The four combinations are:

10 = 10
10 = 4 + 4 + 2
10 = 4 + 2 + 2 + 2
10 = 2 + 2 + 2 + 2 + 2


Input: coins = [5], amount = 5
Output: 1
Explanation: There is one combination: 5 = 5.


Constraints:
1 <= n, coins[i], amount <= 10^3

"""


class Solution:

    ################################
    # Recursive Approach
    ################################

    def countRecursiveHelper(self, coins, index, remainingAmount):
        # Base case: If the remaining amount is zero, we've found a valid combination
        if remainingAmount == 0:
            return 1

        # Base case: If there is only one coin left
        if index == 0:
            return 1 if remainingAmount % coins[0] == 0 else 0

        # Exclude the current coin
        exclude_current = self.countRecursiveHelper(coins, index - 1, remainingAmount)

        # Include the current coin (if it's not larger than the remaining amount)
        include_current = 0
        if coins[index] <= remainingAmount:
            include_current = self.countRecursiveHelper(coins, index, remainingAmount - coins[index])

        return include_current + exclude_current

    def countRecursive(self, coins, numCoins, totalAmount):
        return self.countRecursiveHelper(coins, numCoins - 1, totalAmount)

    ################################
    # Memoization Approach
    ################################

    def countMemoizationHelper(self, coins, index, remainingAmount, memo):
        # Base case: If the remaining amount is zero, we've found a valid combination
        if remainingAmount == 0:
            return 1

        # Base case: If there is only one coin left
        if index == 0:
            return 1 if remainingAmount % coins[0] == 0 else 0

        # Check memoization table
        if memo[index][remainingAmount] != -1:
            return memo[index][remainingAmount]

        # Exclude the current coin
        exclude_current = self.countMemoizationHelper(coins, index - 1, remainingAmount, memo)

        # Include the current coin (if it's not larger than the remaining amount)
        include_current = 0
        if coins[index] <= remainingAmount:
            include_current = self.countMemoizationHelper(coins, index, remainingAmount - coins[index], memo)

        memo[index][remainingAmount] = include_current + exclude_current

        return memo[index][remainingAmount]

    def countMemoization(self, coins, numCoins, totalAmount):
        # Initialize memoization table with -1
        memo = [[-1] * (totalAmount + 1) for _ in range(numCoins)]
        return self.countMemoizationHelper(coins, numCoins - 1, totalAmount, memo)

    ################################
    # Tabulation Approach
    ################################

    def countTabulation(self, coins, numCoins, totalAmount):
        # Initialize DP table
        dp = [[0] * (totalAmount + 1) for _ in range(numCoins)]

        # Base case: Fill the first row
        for amount in range(totalAmount + 1):
            if amount % coins[0] == 0:
                dp[0][amount] = 1

        # Fill the DP table
        for index in range(1, numCoins):
            for amount in range(totalAmount + 1):
                # Exclude the current coin
                exclude_current = dp[index - 1][amount]

                # Include the current coin (if it's not larger than the amount)
                include_current = 0
                if coins[index] <= amount:
                    include_current = dp[index][amount - coins[index]]

                dp[index][amount] = include_current + exclude_current

        return dp[numCoins - 1][totalAmount]

    ################################
    # Tabulation Space Optimized Approach
    ################################

    def countTabulationSpaceOptimized(self, coins, numCoins, totalAmount):
        # Initialize previous row (1D array)
        prev = [0] * (totalAmount + 1)

        # Base case: Fill the first row
        for amount in range(totalAmount + 1):
            if amount % coins[0] == 0:
                prev[amount] = 1

        # Iterate over remaining coins
        for index in range(1, numCoins):
            curr = [0] * (totalAmount + 1)  # Current row
            for amount in range(totalAmount + 1):
                # Exclude the current coin
                exclude_current = prev[amount]

                # Include the current coin (if it's not larger than the amount)
                include_current = 0
                if coins[index] <= amount:
                    include_current = curr[amount - coins[index]]

                curr[amount] = include_current + exclude_current

            prev = curr[:]  # Update previous row

        return prev[totalAmount]


if __name__ == "__main__":

    # Create an instance of Solution class
    sol = Solution()

    # Test cases
    test_cases = [
        {"coins": [2, 4, 10], "amount": 10, "output": 4},
        {"coins": [1, 2, 3], "amount": 4, "output": 4},
    ]

    for test_case in test_cases:
        coins = test_case["coins"]
        amount = test_case["amount"]
        numCoins = len(coins)
        print("=" * 50)
        print(f"For coins = {coins} and amount = {amount}")
        print("The total number of ways (Recursive) is:", sol.countRecursive(coins, numCoins, amount))
        print("The total number of ways (Memoization) is:", sol.countMemoization(coins, numCoins, amount))
        print("The total number of ways (Tabulation) is:", sol.countTabulation(coins, numCoins, amount))
        print("The total number of ways (Space Optimized) is:", sol.countTabulationSpaceOptimized(coins, numCoins, amount))
        print("Expected output is:", test_case["output"])
        print()
