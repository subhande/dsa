"""
## Longest common substring

Given two strings str1 and str2, find the length of their longest common substring.

A substring is a contiguous sequence of characters within a string.

------------------------------------------------------------
Examples:
Input: str1 = "abcde", str2 = "abfce"

Output: 2
Explanation: The longest common substring is "ab", which has a length of 2.
------------------------------------------------------------
Input: str1 = "abcdxyz", str2 = "xyzabcd"

Output: 4
Explanation: The longest common substring is "abcd", which has a length of 4.
------------------------------------------------------------
Constraints:
- n=str1.length
- m=str2.length
- 1<= n, m <=103
- str1 and str2 are in lowercase alphabet

"""

class Solution:

    ################################
    # Recursive Approach
    ################################

    def longestCommonSubstrRecursiveHelper(self, str1, str2, ind1, ind2, currentSubstrLen):
        if ind1 == -1 or ind2 == -1:
            return currentSubstrLen

        if str1[ind1] == str2[ind2]:
            return self.longestCommonSubstrRecursiveHelper(str1, str2, ind1 - 1, ind2 - 1, currentSubstrLen + 1)

        return max(currentSubstrLen, max(self.longestCommonSubstrRecursiveHelper(str1, str2, ind1 - 1, ind2, 0), self.longestCommonSubstrRecursiveHelper(str1, str2, ind1, ind2 - 1, 0)))

    def longestCommonSubstrRecursive(self, str1, str2):
        return self.longestCommonSubstrRecursiveHelper(str1, str2, len(str1) - 1, len(str2) - 1, 0)

    ################################
    # Memoization Approach
    ################################
    def longestCommonSubstrMemoizationHelper(self, str1, str2, i, j, memo):
        """
        Returns the length of the longest common substring ENDING at str1[i] and str2[j].
        """
        # Base conditions: if out of range, no substring
        if i < 0 or j < 0:
            return 0

        # If already computed, return cached value
        if memo[i][j] != -1:
            return memo[i][j]

        # If characters match, 1 + best we can do ending at (i-1, j-1)
        if str1[i] == str2[j]:
            memo[i][j] = 1 + self.longestCommonSubstrMemoizationHelper(str1, str2, i - 1, j - 1, memo)
        else:
            # Mismatch → The common substring ending exactly at (i, j) is 0
            memo[i][j] = 0

        return memo[i][j]

    def longestCommonSubstrMemoization(self, str1, str2):
        n, m = len(str1), len(str2)
        # memo[i][j] = length of LCS *ending* at (i, j)
        memo = [[-1] * m for _ in range(n)]

        max_len = 0
        # We compute the helper for every pair (i, j) to ensure we do not miss any possible matching position.
        for i in range(n):
            for j in range(m):
                length_ending_here = self.longestCommonSubstrMemoizationHelper(str1, str2, i, j, memo)
                max_len = max(max_len, length_ending_here)

        return max_len

    ################################
    # Tabulation Approach
    ################################

    def longestCommonSubstrTabulation(self, str1, str2):
        # Initialize a 2D DP table with dimensions (n+1) x (m+1)
        # dp[i][j] = length of the longest common substring ending at str1[i-1] and str2[j-1]
        # dp[i][j] = 0 if str1[i-1] != str2[j-1]
        # dp[i][j] = 1 + dp[i-1][j-1] if str1[i-1] == str2[j-1]
        # The answer is the maximum value in the table


        n, m = len(str1), len(str2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        max_len = 0

        for i in range(1, n + 1):
            for j in range(1, m + 1):

                if str1[i-1] == str2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                    max_len = max(max_len, dp[i][j])
                else:
                    dp[i][j] = 0

        return max_len

    ################################
    # Tabulation Space Optimized Approach
    ################################

    def longestCommonSubstrTabulationSpaceOptimized(self, str1, str2):
        # Initialize two 1D arrays for storing the previous and current rows of the DP table
        # prevRow[j] = dp[i-1][j]
        # currentRow[j] = dp[i][j]
        # dp[i][j] = length of the longest common substring ending at str1[i-1] and str2[j-1]
        # dp[i][j] = 0 if str1[i-1] != str2[j-1]
        # dp[i][j] = 1 + dp[i-1][j-1] if str1[i-1] == str2[j-1]
        # The answer is the maximum value in the prevRow array
        n, m = len(str1), len(str2)
        prevRow = [0] * (m + 1)
        currentRow = [0] * (m + 1)

        max_len = 0

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if str1[i-1] == str2[j-1]:
                    currentRow[j] = 1 + prevRow[j-1]
                    max_len = max(max_len, currentRow[j])
                else:
                    currentRow[j] = 0
            prevRow = currentRow[:]
        return max_len


if __name__ == "__main__":
    longestCommonSubstr = Solution()

    test_cases = [
        {
            "str1": "abcde",
            "str2": "abfce",
            "output": 2
        },
        {
            "str1": "abcdxyz",
            "str2": "xyzabcd",
            "output": 4
        },
        {
            "str1": "abcdef",
            "str2": "ghijkl",
            "output": 0
        }
    ]

    for i, test_case in enumerate(test_cases):
        print("==================================")
        print(f"Test case {i+1}")
        outputRecusive = longestCommonSubstr.longestCommonSubstrRecursive(test_case["str1"], test_case["str2"])
        print(f"Output (Recursive): {outputRecusive}")
        outputMemoization = longestCommonSubstr.longestCommonSubstrMemoization(test_case["str1"], test_case["str2"])
        print(f"Output (Memoization): {outputMemoization}")
        outputTabulation = longestCommonSubstr.longestCommonSubstrTabulation(test_case["str1"], test_case["str2"])
        print(f"Output (Tabulation): {outputTabulation}")
        outputTabulationSpaceOptimized = longestCommonSubstr.longestCommonSubstrTabulationSpaceOptimized(test_case["str1"], test_case["str2"])
        print(f"Output (Tabulation Space Optimized): {outputTabulationSpaceOptimized}")


        assert outputRecusive == test_case["output"]
        assert outputMemoization == test_case["output"]
        assert outputTabulation == test_case["output"]
        assert outputTabulationSpaceOptimized == test_case["output"]
