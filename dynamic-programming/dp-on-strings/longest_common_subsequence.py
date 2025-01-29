"""
## Longest common subsequence

Given two strings str1 and str2, find the length of their longest common subsequence.

A subsequence is a sequence that appears in the same relative order but not necessarily contiguous and a common subsequence of two strings is a subsequence that is common to both strings.

------------------------------------------------------------
Examples:
Input: str1 = "bdefg", str2 = "bfg"

Output: 3
Explanation: The longest common subsequence is "bfg", which has a length of 3.

------------------------------------------------------------
Input: str1 = "mnop", str2 = "mnq"

Output: 2
Explanation: The longest common subsequence is "mn", which has a length of 2.
------------------------------------------------------------
Constraints:
- n=str1.length
- m=str2.length
- 1<= n, m <=103
- str1 and str2 are in lowercase alphabet

"""

class Solution:

    ###############################################
    # Recursive Approach
    ###############################################

    def lcsRecursiveHelper(self, str1, str2, index1, index2):
        # Base case: If either string is exhausted
        if index1 < 0 or index2 < 0:
            return 0

        # If characters match, increment the count and move diagonally in both strings
        if str1[index1] == str2[index2]:
            return 1 + self.lcsRecursiveHelper(str1, str2, index1 - 1, index2 - 1)

        # If characters do not match, find the maximum of the two possibilities:
        # - Excluding the current character of str1
        # - Excluding the current character of str2
        return max(self.lcsRecursiveHelper(str1, str2, index1 - 1, index2),
                   self.lcsRecursiveHelper(str1, str2, index1, index2 - 1))

    def lcsRecursive(self, str1, str2):
        return self.lcsRecursiveHelper(str1, str2, len(str1) - 1, len(str2) - 1)

    ###############################################
    # Memoization Approach
    ###############################################

    def lcsMemoizationHelper(self, str1, str2, index1, index2, memo):
        # Base case: If either string is exhausted
        if index1 < 0 or index2 < 0:
            return 0

        # Return the result if it is already computed
        if memo[index1][index2] != -1:
            return memo[index1][index2]

        # If characters match, store the result and move diagonally in both strings
        if str1[index1] == str2[index2]:
            memo[index1][index2] = 1 + self.lcsMemoizationHelper(str1, str2, index1 - 1, index2 - 1, memo)
        else:
            # If characters do not match, take the maximum of the two possibilities
            memo[index1][index2] = max(
                self.lcsMemoizationHelper(str1, str2, index1 - 1, index2, memo),
                self.lcsMemoizationHelper(str1, str2, index1, index2 - 1, memo)
            )
        return memo[index1][index2]

    def lcsMemoization(self, str1, str2):
        n, m = len(str1), len(str2)
        # Initialize a memoization table with -1
        memo = [[-1] * m for _ in range(n)]
        return self.lcsMemoizationHelper(str1, str2, n - 1, m - 1, memo)

    ###############################################
    # Tabulation Approach
    ###############################################

    def lcsTabulation(self, str1, str2):
        n, m = len(str1), len(str2)

        # Initialize a 2D DP table with dimensions (n+1) x (m+1)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # Fill the DP table
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # If characters match, take the value from the diagonal and add 1
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    # Otherwise, take the maximum of excluding one character from either string
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # The last cell contains the length of the LCS
        return dp[n][m]

    ###############################################
    # Tabulation Space Optimized Approach
    ###############################################

    def lcsTabulationSpaceOptimized(self, str1, str2):
        n, m = len(str1), len(str2)

        # Initialize two 1D arrays for storing the previous and current rows of the DP table
        prevRow = [0] * (m + 1)
        currentRow = [0] * (m + 1)

        # Fill the DP table row by row
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # If characters match, take the value from the diagonal (prevRow[j-1]) and add 1
                if str1[i - 1] == str2[j - 1]:
                    currentRow[j] = 1 + prevRow[j - 1]
                else:
                    # Otherwise, take the maximum of excluding one character from either string
                    currentRow[j] = max(prevRow[j], currentRow[j - 1])
            # Update the previous row with the current row
            prevRow = currentRow[:]

        # The last cell of prevRow contains the length of the LCS
        return prevRow[m]


if __name__ == "__main__":
    lcs = Solution()

    # Define test cases
    test_cases = [
        {
            "str1": "bdefg",
            "str2": "bfg",
            "expected_output": 3
        },
        {
            "str1": "mnop",
            "str2": "mnq",
            "expected_output": 2
        },
        {
            "str1": "abc",
            "str2": "dafb",
            "expected_output": 2
        }
    ]

    # Run the test cases
    for i, test_case in enumerate(test_cases):
        print("==================================")
        print(f"Test case {i + 1}")

        recursiveOutput = lcs.lcsRecursive(test_case["str1"], test_case["str2"])
        print(f"Output (Recursive): {recursiveOutput}")

        memoizationOutput = lcs.lcsMemoization(test_case["str1"], test_case["str2"])
        print(f"Output (Memoization): {memoizationOutput}")

        tabulationOutput = lcs.lcsTabulation(test_case["str1"], test_case["str2"])
        print(f"Output (Tabulation): {tabulationOutput}")

        spaceOptimizedOutput = lcs.lcsTabulationSpaceOptimized(test_case["str1"], test_case["str2"])
        print(f"Output (Tabulation Space Optimized): {spaceOptimizedOutput}")

        # Check if outputs match the expected output
        assert recursiveOutput == test_case["expected_output"]
        assert memoizationOutput == test_case["expected_output"]
        assert tabulationOutput == test_case["expected_output"]
        assert spaceOptimizedOutput == test_case["expected_output"]

    print("All test cases passed!")
