"""
## Minimum insertions to make string palindrome

Given a string s, find the minimum number of insertions needed to make it a palindrome. A palindrome is a sequence that reads the same backward as forward. You can insert characters at any position in the string.

------------------------------------------------------------
Examples:
Input: s = "abcaa"
Output: 2

Explanation: Insert 2 characters "c", and "b" to make "abcacba", which is a palindrome.
------------------------------------------------------------
Input: s = "ba"
Output: 1

Explanation: Insert "a" at the beginning to make "aba", which is a palindrome.
------------------------------------------------------------
Constraints:
1 <= s.length <= 1000,
s consists of only lowercase English letters

"""


"""
Solution:
--------------
Approach:
-> We are given a string (say s), store its length as n.
-> Find the length of the longest palindromic subsequence ( say k) as discussed Longest Common Subsequence
-> Return (n-k) as answer.
"""

class Solution:

    ################################
    # Tabulation Approach
    ################################

    def minInsertionTabulation(self, str):
        pass


    ################################
    # Tabulation Space Optimized Approach
    ################################

    def minInsertionTabulationSpaceOptimized(self, str):
        pass




if __name__ == "__main__":
    minInsertion = Solution()

    test_cases = [
        {
            "str": "abcaa",
            "output": 2
        },
        {
            "str": "ba",
            "output": 1
        }
    ]

    for i, test_case in enumerate(test_cases):
        print("==================================")
        print(f"Test case {i+1}")
        outputTabulation = minInsertion.minInsertionTabulation(test_case["str"])
        print(f"Output (Tabulation): {outputTabulation}")
        outputTabulationSpaceOptimized = minInsertion.minInsertionTabulationSpaceOptimized(test_case["str"])
        print(f"Output (Tabulation Space Optimized): {outputTabulationSpaceOptimized}")

        # assert outputTabulation == test_case["output"]
        # assert outputTabulationSpaceOptimized == test_case["output"]
