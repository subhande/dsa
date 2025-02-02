"""
## Wildcard matching

Given a string str and a pattern pat, implement a pattern matching function that supports the following special characters:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The pattern must match the entire string.

------------------------------------------------------------
Examples:
------------------------------------------------------------
Input: str = "xaylmz", pat = "x?y*z"
Output: true

Explanation:
The pattern "x?y*z" matches the string "xaylmz":
- '?' matches 'a'
- '*' matches "lm"
- 'z' matches 'z'
------------------------------------------------------------
Input: str = "xyza", pat = "x*z"
Output: false

Explanation:
The pattern "x*z" does not match the string "xyza" because there is an extra 'a' at the end of the string that is not matched by the pattern.
------------------------------------------------------------
Constraints:
1 <= length of(str, pattern) <= 200

Solution:
--------------

"""

class Solution:

    ################################
    # Recursion Approach
    ################################

    def is_all_stars(self, s, j):
        # Check if all characters in pattern[0...j] are '*'
        for k in range(j + 1):
            if s[k] != '*':
                return False
        return True

    def wildCardRecursionHelper(self, str, pat, i, j):
        # Base case
        # If both string and pattern are exhausted, it's a match
        if i < 0 and j < 0:
            return True
        # If pattern is exhausted but string is not, no match
        if j < 0 and i >= 0:
            return False
        # If string is exhausted but pattern is not, pattern must be all '*'
        if i < 0 and j >= 0:
            return self.is_all_stars(pat, j)

        # If current characters match or pattern has a '?', move both pointers
        if str[i] == pat[j] or pat[j] == '?':
            return self.wildCardRecursionHelper(str, pat, i - 1, j - 1)

        # If pattern has '*', it can either match no character or one character
        if pat[j] == '*':
            return self.wildCardRecursionHelper(str, pat, i - 1, j) or self.wildCardRecursionHelper(str, pat, i, j - 1)

        # Characters don't match and no wildcard is present
        return False

    def wildCardRecursion(self, str, pat):
        return self.wildCardRecursionHelper(str, pat, len(str) - 1, len(pat) - 1)


    ################################
    # Recursion with Memoization Approach
    ################################

    def wildCardRecursionMemoizationHelper(self, str, pat, i, j, dp):
        # Base case
        # If both string and pattern are exhausted, it's a match
        if i < 0 and j < 0:
            return True
        # If pattern is exhausted but string is not, no match
        if j < 0 and i >= 0:
            return False
        # If string is exhausted but pattern is not, pattern must be all '*'
        if i < 0 and j >= 0:
            return self.is_all_stars(pat, j)

        if dp[i][j] != -1:
            return dp[i][j]

        # If current characters match or pattern has a '?', move both pointers
        if str[i] == pat[j] or pat[j] == '?':
            dp[i][j] = self.wildCardRecursionMemoizationHelper(str, pat, i - 1, j - 1, dp)
            return dp[i][j]
        else:
            # If pattern has '*', it can either match no character or one character
            if pat[j] == '*':
                dp[i][j] = self.wildCardRecursionMemoizationHelper(str, pat, i - 1, j, dp) or self.wildCardRecursionMemoizationHelper(str, pat, i, j - 1, dp)
                return dp[i][j]
            else:
                # Characters don't match and no wildcard is present
                dp[i][j] = False
                return dp[i][j]

    def wildCardRecursionMemoization(self, str, pat):
        dp = [[-1 for _ in range(len(pat))] for _ in range(len(str))]
        return self.wildCardRecursionMemoizationHelper(str, pat, len(str) - 1, len(pat) - 1, dp)

    ################################
    # Tabulation Approach
    ################################

    def wildCardTabulation(self, s: str, pat: str) -> bool:
        """
        Tabulation approach (2D DP) for wildcard matching.
        '?' matches any single character.
        '*' matches any sequence of characters (including the empty sequence).
        """
        n, m = len(s), len(pat)
        # dp[i][j] is True if s[0:i] matches pat[0:j]
        dp = [[False] * (m + 1) for _ in range(n + 1)]

        # Base case: empty string matches empty pattern
        dp[0][0] = True

        # Fill the first row: empty string vs pattern
        for j in range(1, m + 1):
            if pat[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]
            else:
                dp[0][j] = False

        # Fill the DP table
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if pat[j - 1] == s[i - 1] or pat[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif pat[j - 1] == '*':
                    # '*' can match zero characters (dp[i][j-1])
                    # or one more character from s (dp[i-1][j])
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                else:
                    dp[i][j] = False

        return dp[n][m]



    ################################
    # Tabulation Space Optimized Approach
    ################################

    def wildCardTabulationSpaceOptimized(self, s: str, pat: str) -> bool:
        """
        Space-optimized tabulation approach for wildcard matching.
        Uses a single 1D DP array to store the previous row's results.
        '?' matches any single character.
        '*' matches any sequence of characters (including the empty sequence).
        """
        n, m = len(s), len(pat)
        # dp[j] will represent the result for the previous row (i-1) at pattern position j.
        dp = [False] * (m + 1)

        # Base case: empty string matches empty pattern.
        dp[0] = True

        # Initialize dp for an empty string s and non-empty pattern.
        for j in range(1, m + 1):
            if pat[j - 1] == '*':
                dp[j] = dp[j - 1]
            else:
                dp[j] = False

        # Iterate over each character in s.
        for i in range(1, n + 1):
            # temp_dp[0] should be False since a non-empty s does not match an empty pattern.
            # We'll update dp in-place, but need to keep the previous value for dp[j-1] of the previous row.
            prev = dp[0]  # dp[i-1][0]
            dp[0] = False
            for j in range(1, m + 1):
                temp = dp[j]  # Save the current dp[j] (from previous row) before updating.
                if pat[j - 1] == s[i - 1] or pat[j - 1] == '?':
                    dp[j] = prev
                elif pat[j - 1] == '*':
                    dp[j] = dp[j] or dp[j - 1]
                else:
                    dp[j] = False
                prev = temp  # Move to next column: prev becomes the old dp[j] value (dp[i-1][j])

        return dp[m]







if __name__ == "__main__":
    wildCard = Solution()

    test_cases = [
        {
            "str": "xaylmz",
            "pat": "x?y*z",
            "output": True
        },
        {
            "str": "xyza",
            "pat": "x*z",
            "output": False
        },
        {
            "str": "abc",
            "pat": "a?c",
            "output": True
        },
        {
            "str": "mayfojkazdpj",
            "pat": "?*?d*j",
            "output": True
        },
    ]

    for i, test_case in enumerate(test_cases):
        print("==================================")
        print(f"Test case {i+1}")
        outputRecursive = wildCard.wildCardRecursion(test_case["str"], test_case["pat"])
        # print(test_case)
        print(f"Output (Recursion): {outputRecursive} | Expected: {test_case['output']}")

        outputRecursiveMemoization = wildCard.wildCardRecursionMemoization(test_case["str"], test_case["pat"])
        print(f"Output (Recursion with Memoization): {outputRecursiveMemoization}")

        outputTabulation = wildCard.wildCardTabulation(test_case["str"], test_case["pat"])
        print(f"Output (Tabulation): {outputTabulation}")

        outputTabulationSpaceOptimized = wildCard.wildCardTabulationSpaceOptimized(test_case["str"], test_case["pat"])
        print(f"Output (Tabulation Space Optimized): {outputTabulationSpaceOptimized}")

        assert outputTabulation == test_case["output"]
        assert outputTabulationSpaceOptimized == test_case["output"]
        assert outputRecursive == test_case["output"]
        assert outputRecursiveMemoization == test_case["output"]
