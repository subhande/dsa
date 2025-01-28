"""
Rod cutting problem
----------------------
Given a rod of length N inches and an array price[] where price[i] denotes the value of a piece of rod of length i inches (1-based indexing). Determine the maximum value obtainable by cutting up the rod and selling the pieces. Make any number of cuts, or none at all, and sell the resulting pieces.


Examples:
Input: price = [1, 6, 8, 9, 10, 19, 7, 20], N = 8
Output: 25

Explanation: Cut the rod into lengths of 2 and 6 for a total price of 6 + 19= 25.

-------------------------------------------------------------
Input: price = [1, 5, 8, 9], N = 4
Output: 10

Explanation: Cut the rod into lengths of 2 and 2 for a total price of 5 + 5 = 10.


Constraints:
1 ≤ N ≤ 1000
1 ≤ price[i] ≤ 10^5

"""

class Solution:

    ################################
    # Recursive Approach
    ################################

    def rodCuttingRecursiveHelper(self, price, ind, N):
        if ind == 0:
            return price[0] * N

        notTaken = self.rodCuttingRecursiveHelper(price, ind - 1, N)

        rodLength = ind + 1
        taken = float("-inf")

        if rodLength <= N:
            taken = price[ind] + self.rodCuttingRecursiveHelper(price, ind, N - rodLength)

        return max(taken, notTaken)

    def rodCuttingRecursive(self, price, n):
        return self.rodCuttingRecursiveHelper(price, n-1, n)

    ################################
    # Memoization Approach
    ################################

    def rodCuttingMemoizationHelper(self, price, ind, N, memo):
        if ind == 0:
            return price[0] * N

        if memo[ind][N] != 0:
            return memo[ind][N]

        notTaken = self.rodCuttingRecursiveHelper(price, ind - 1, N)

        rodLength = ind + 1
        taken = float("-inf")

        if rodLength <= N:
            taken = price[ind] + self.rodCuttingRecursiveHelper(price, ind, N - rodLength)

        return max(taken, notTaken)

    def rodCuttingMemoization(self, price, n):
        memo = [[0] * (n + 1) for _ in range(n + 1)]

        return self.rodCuttingMemoizationHelper(price, n-1, n, memo)

    ################################
    # Tabulation Approach
    ################################

    def rodCuttingTabulation(self, price, n):
        memo = [[0] * (n + 1) for _ in range(n)]

        for length in range(n+1):
            memo[0][length] = price[0] * length

        for ind in range(1, n):
            for length in range(1, n + 1):
                notTaken = memo[ind - 1][length]
                rodLength = ind + 1
                taken = float("-inf")
                if rodLength <= length:
                    taken = price[ind] + memo[ind][length - rodLength]

                memo[ind][length] = max(taken, notTaken)

        return memo[n-1][n]

    ################################
    # Tabulation Space Optimized Approach
    ################################

    def rodCuttingTabulationSpaceOptimized(self, price, n):
        prev = [0] * (n + 1)
        cur = [0] * (n + 1)

        for length in range(n+1):
            prev[length] = price[0] * length

        for ind in range(1, n):
            for length in range(1, n + 1):
                notTaken = prev[length]
                rodLength = ind + 1
                taken = float("-inf")
                if rodLength <= length:
                    taken = price[ind] + cur[length - rodLength]

                cur[length] = max(taken, notTaken)
            prev = cur[:]
        return prev[n]


if __name__ == "__main__":
    # Create an instance of Solution class
    sol = Solution()

    # Test cases
    test_cases = [
        {"price": [1, 6, 8, 9, 10, 19, 7, 20], "N": 8, "expected": 25},
        {"price": [1, 5, 8, 9], "N": 4, "expected": 8},
        {"price": [5, 5, 8, 9, 10, 17, 17, 20], "N": 8, "expected": 40},
    ]

    for test in test_cases:
        price = test["price"]
        N = test["N"]

        print("="*50)

        print("The maximum value is (Recursive):", sol.rodCuttingRecursive(price, N))

        print("The maximum value is (Memoization):", sol.rodCuttingMemoization(price, N))

        print("The maximum value is (Tabulation):", sol.rodCuttingTabulation(price, N))

        print("The maximum value is (Tabulation Space Optimized):", sol.rodCuttingTabulationSpaceOptimized(price, N))
