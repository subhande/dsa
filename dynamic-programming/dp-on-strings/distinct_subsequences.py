"""
## Distinct subsequences

Given two strings s and t, return the number of distinct subsequences of s that equal t.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters. For example, "ace" is a subsequence of "abcde" while "aec" is not.

The task is to count how many different ways we can form t from s by deleting some (or no) characters from s. Return the result modulo 10^9+7.

------------------------------------------------------------
Examples:
Input: s = "axbxax", t = "axa"

Output: 2
Explanation: In the string "axbxax", there are two distinct subsequences "axa":

(a)(x)bx(a)x
(a)xb(x)(a)x
------------------------------------------------------------
Input: s = "babgbag", t = "bag"
Output: 5

Explanation: In the string "babgbag", there are five distinct subsequences "bag":

(ba)(b)(ga)(g)
(ba)(bg)(ag)
(bab)(ga)(g)
(bab)(g)(ag)
(babg)(a)(g)

------------------------------------------------------------
Constraints:
1 <= s.length, t.length <= 1000
"""


"""
Solution:
--------------

"""

class Solution:

    ################################
    # Recursion Approach
    ################################

    def distinctSubsequencesRecursionHelper(self, s, t, i, j):
        if j < 0:
            return 1
        if i < 0:
            return 0

        if s[i] == t[j]:
            return self.distinctSubsequencesRecursionHelper(s, t, i - 1, j - 1) + self.distinctSubsequencesRecursionHelper(s, t, i - 1, j)
        return self.distinctSubsequencesRecursionHelper(s, t, i - 1, j)

    def distinctSubsequencesRecursion(self, s, t):
        return self.distinctSubsequencesRecursionHelper(s, t, len(s) - 1, len(t) - 1) % (10**9 + 7)


    ################################
    # Recursion with Memoization Approach
    ################################

    def distinctSubsequencesRecursionMemoizationHelper(self, s, t, i, j, dp):
        if j < 0:
            return 1
        if i < 0:
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        if s[i] == t[j]:
            dp[i][j] = self.distinctSubsequencesRecursionMemoizationHelper(s, t, i - 1, j - 1, dp) + self.distinctSubsequencesRecursionMemoizationHelper(s, t, i - 1, j, dp)
        else:
            dp[i][j] = self.distinctSubsequencesRecursionMemoizationHelper(s, t, i - 1, j, dp)
        return dp[i][j] % (10**9 + 7)

    def distinctSubsequencesRecursionMemoization(self, s, t):
        dp = [[-1 for _ in range(len(t))] for _ in range(len(s))]
        return self.distinctSubsequencesRecursionMemoizationHelper(s, t, len(s) - 1, len(t) - 1, dp)

    ################################
    # Tabulation Approach
    ################################

    def distinctSubsequencesTabulation(self, s, t):
        n, m = len(s), len(t)
        # Declare a 2D DP array to store the number of distinct subsequences
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # Initialize the first row: empty string t can be matched with any non-empty s in one way
        for i in range(n + 1):
            dp[i][0] = 1

        # Initialize the first column: s can't match any non-empty t
        for i in range(1, m + 1):
            dp[0][i] = 0

        # Fill in the DP array
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n][m] % (10**9 + 7)




    ################################
    # Tabulation Space Optimized Approach
    ################################

    def distinctSubsequencesTabulationSpaceOptimized(self, s, t):
        n, m = len(s), len(t)

        # Declare a 1D DP array to store the number of distinct subsequences
        prev = [0] * (m + 1)
        curr = [0] * (m + 1)

        # Initialize the count for an empty string (base case)
        prev[0] = 1
        curr[0] = 1

        # Fill in the DP array
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s[i - 1] == t[j - 1]:
                    curr[j] = prev[j - 1] + prev[j]
                else:
                    curr[j] = prev[j]
            prev = curr[:]
        return prev[m] % (10**9 + 7)





if __name__ == "__main__":
    distinctSubsequences = Solution()

    test_cases = [
        {
            "s": "axbxax",
            "t": "axa",
            "output": 2
        },
        {
            "s": "babgbag",
            "t": "bag",
            "output": 5
        },
        {
            "s": "abcde",
            "t": "ace",
            "output": 1
        },
    ]

    for i, test_case in enumerate(test_cases):
        print("==================================")
        print(f"Test case {i+1}")
        outputRecursive = distinctSubsequences.distinctSubsequencesRecursion(test_case["s"], test_case["t"])
        print(f"Output (Recursion): {outputRecursive}")

        outputRecursiveMemoization = distinctSubsequences.distinctSubsequencesRecursionMemoization(test_case["s"], test_case["t"])
        print(f"Output (Recursion with Memoization): {outputRecursiveMemoization}")

        outputTabulation = distinctSubsequences.distinctSubsequencesTabulation(test_case["s"], test_case["t"])
        print(f"Output (Tabulation): {outputTabulation}")

        outputTabulationSpaceOptimized = distinctSubsequences.distinctSubsequencesTabulationSpaceOptimized(test_case["s"], test_case["t"])
        print(f"Output (Tabulation Space Optimized): {outputTabulationSpaceOptimized}")

        # assert outputTabulation == test_case["output"]
        # assert outputTabulationSpaceOptimized == test_case["output"]
