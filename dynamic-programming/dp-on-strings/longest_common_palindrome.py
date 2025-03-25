"""
## Longest palindromic subsequence

Given a string, Find the longest palindromic subsequence length in given string.

A palindrome is a sequence that reads the same backwards as forward.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

------------------------------------------------------------
Examples:
Input: s = "eeeme"

Output: 4

Explanation: The longest palindromic subsequence is "eeee", which has a length of 4.
------------------------------------------------------------
Input: s = "annb"

Output: 2

Explanation: The longest palindromic subsequence is "nn", which has a length of 2.
------------------------------------------------------------
Constraints:
1 ≤ s.length ≤ 1000

"""


class Solution:

    ################################
    # Recursive Approach with Memoization
    # ###############################

    def lpsMemoizationHelper(self, str1, str2, index1, index2, memo):
        # Base case: If either string is exhausted
        if index1 < 0 or index2 < 0:
            return 0

        # Return the result if it is already computed
        if memo[index1][index2] != -1:
            return memo[index1][index2]

        # If characters match, store the result and move diagonally in both strings
        if str1[index1] == str2[index2]:
            memo[index1][index2] = 1 + self.lpsMemoizationHelper(str1, str2, index1 - 1, index2 - 1, memo)
        else:
            # If characters do not match, take the maximum of the two possibilities
            memo[index1][index2] = max(
                self.lpsMemoizationHelper(str1, str2, index1 - 1, index2, memo),
                self.lpsMemoizationHelper(str1, str2, index1, index2 - 1, memo)
            )
        return memo[index1][index2]

    def lpsMemoization(self, str1):
        n, m = len(str1), len(str1)
        # Initialize a memoization table with -1
        memo = [[-1] * m for _ in range(n)]
        return self.lpsMemoizationHelper(str1, str1[::-1], n - 1, m - 1, memo)

    def longestPalinSubseqRecursiveMemo(self, str, start, end, memo):
        if start > end:
            return 0
        if start == end:
            return 1
        if memo[start][end] != -1:
            return memo[start][end]
        if str[start] == str[end]:
            memo[start][end] = 2 + self.longestPalinSubseqRecursiveMemo(str, start + 1, end - 1, memo)
        else:
            memo[start][end] = max(self.longestPalinSubseqRecursiveMemo(str, start + 1, end, memo), self.longestPalinSubseqRecursiveMemo(str, start, end - 1, memo))
        return memo[start][end]

    ################################
    # Tabulation Approach
    ################################

    def longestPalinSubseqTabulation(self, str):
        '''
        This function finds the length of the longest palindromic subsequence in the given string using tabulation approach.
        - Intuition: We need to find the length of the longest palindromic subsequence in the given string.
        str = "b b a b c b c a b"
        str_rev = "b a c b c b a b b"
        Now, we have taken the reverse of the string for the following two reasons:
         -> The longest palindromic subsequence being a palindrome will remain the same when the entire string is reversed.
         -> The length of the palindromic subsequence will also remain the same when the entire string is reversed.

        From the above discussion we can conclude that the longest palindromic subsequence of a string is the longest common subsequence of the given string and its reverse.
        '''
        str_rev = str[::-1]
        n, m = len(str), len(str_rev)

        # Declare a 2D DP array to store length of the LCS
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # # Initialize first row and first column to 0
        # for i in range(n + 1):
        #     dp[i][0] = 0
        # for i in range(m + 1):
        #     dp[0][i] = 0

        # Fill in the DP array
        for ind1 in range(1, n + 1):
            for ind2 in range(1, m + 1):
                if str[ind1 - 1] == str_rev[ind2 - 1]:
                    dp[ind1][ind2] = 1 + dp[ind1 - 1][ind2 - 1]
                else:
                    dp[ind1][ind2] = max(dp[ind1 - 1][ind2], dp[ind1][ind2 - 1])

        # The value at dp[n][m] contains length of the LCS
        return dp[n][m]




    ################################
    # Tabulation Space Optimized Approach
    ################################

    def longestPalinSubseqTabulationSpaceOptimized(self, str):
        str_rev = str[::-1]
        n, m = len(str), len(str_rev)

        # Declare two arrays to store the length of the LCS
        prev = [0] * (m + 1)
        curr = [0] * (m + 1)

        # Fill in the DP array

        for ind1 in range(1, n + 1):
            for ind2 in range(1, m + 1):
                if str[ind1 - 1] == str_rev[ind2 - 1]:
                    curr[ind2] = 1 + prev[ind2 - 1]
                else:
                    curr[ind2] = max(prev[ind2], curr[ind2 - 1])
            prev = curr[:]

        return prev[m]




if __name__ == "__main__":
    longestPalinSubseq = Solution()

    test_cases = [
        {
            "str": "eeeme",
            "output": 4
        },
        {
            "str": "annb",
            "output": 2
        },
        {
            "str": "bbabcbcab",
            "output": 7

        },
        {
            "str": "aacabdkacaa",
            "output": 9
        }
    ]

    for i, test_case in enumerate(test_cases):
        print("==================================")
        print(f"Test case {i+1}")
        outputTabulation = longestPalinSubseq.longestPalinSubseqTabulation(test_case["str"])
        print(f"Output (Tabulation): {outputTabulation}")
        outputTabulationSpaceOptimized = longestPalinSubseq.longestPalinSubseqTabulationSpaceOptimized(test_case["str"])
        print(f"Output (Tabulation Space Optimized): {outputTabulationSpaceOptimized}")

        assert outputTabulation == test_case["output"]
        # assert outputTabulationSpaceOptimized == test_case["output"]
        outputRecursiveMemo = longestPalinSubseq.lpsMemoization(test_case["str"])
        print(f"Output (Recursive with Memoization): {outputRecursiveMemo}")
