"""
## Shortest common supersequence

Given two strings str1 and str2, find the shortest common supersequence.

The shortest common supersequence is the shortest string that contains both str1 and str2 as subsequences.

------------------------------------------------------------
Examples:
Input: str1 = "mno", str2 = "nop"

Output: "mnop"

Explanation: The shortest common supersequence is "mnop". It contains "mno" as the first three characters and "nop" as the last three characters, thus including both strings as subsequences.
------------------------------------------------------------
Input: str1 = "dynamic", str2 = "program"

Output: "dynprogramic"

Explanation: The shortest common supersequence is "dynamprogramic". It includes all characters from both "dynamic" and "program", with minimal overlap. For example, "dynamic" appears as "dynam...ic" and "program" appears as "...program..." within "dynamprogramic".
------------------------------------------------------------
Constraints:
1 <= str1.length, str2.length <= 1000
str1 and str2 consist of lowercase English letters.

"""


"""
Solution:
--------------
Approach:


"""

class Solution:

    ################################
    # Tabulation Approach
    ################################

    def lcs(self, str1, str2):
        n, m = len(str1), len(str2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp

    def generateSupersequence(self, str1, str2, dp):
        n, m = len(str1), len(str2)
        supersequence = ""

        while n > 0 and m > 0:
            if str1[n - 1] == str2[m - 1]:
                supersequence = str1[n - 1] + supersequence
                n -= 1
                m -= 1
            else:
                if dp[n - 1][m] > dp[n][m - 1]:
                    supersequence = str1[n - 1] + supersequence
                    n -= 1
                else:
                    supersequence = str2[m - 1] + supersequence
                    m -= 1

        while n > 0:
            supersequence = str1[n - 1] + supersequence
            n -= 1

        while m > 0:
            supersequence = str2[m - 1] + supersequence
            m -= 1

        return supersequence

    def shortestCommonSupersequenceTabulation(self, str1: str, str2: str):
        dp = self.lcs(str1, str2)
        supersequence = self.generateSupersequence(str1, str2, dp)
        return supersequence



if __name__ == "__main__":
    shortestCommonSupersequence = Solution()

    test_cases = [
        {
            "str1": "mno",
            "str2": "nop",
            "output": "mnop"
        },
        {
            "str1": "dynamic",
            "str2": "program",
            "output": "dynprogramic"
        }
    ]

    for i, test_case in enumerate(test_cases):
        print("==================================")
        print(f"Test case {i+1}")
        outputTabulation = shortestCommonSupersequence.shortestCommonSupersequenceTabulation(test_case["str1"], test_case["str2"])
        print(f"Output (Tabulation): {outputTabulation}")
        assert outputTabulation == test_case["output"]
