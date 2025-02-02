"""
## Minimum insertions or deletions to convert string A to B

Given two strings str1 and str2, find the minimum number of insertions and deletions in string str1 required to transform str1 into str2.

Insertion and deletion of characters can take place at any position in the string.

------------------------------------------------------------
Examples:
Input: str1 = "kitten", str2 = "sitting"
Output: 5

Explanation: To transform "kitten" to "sitting", delete "k" and insert "s" to get "sitten", then insert "i" to get "sittin", and insert "g" at the end to get "sitting".
------------------------------------------------------------
Input: str1 = "flaw", str2 = "lawn"
Output: 2

Explanation: To transform "flaw" to "lawn", delete "f" and insert "n" at the end. Hence minimum number of operations required is 2".
------------------------------------------------------------
Constraints:
1 ≤ str1.length, str2.length ≤ 1000

"""


"""
Solution:
--------------
Approach:
-> Let 'n' and 'm' be the length of str1 and str2 respectively.
-> Find the length of the longest common subsequence ( say k) of str1 and str2 as discussed in Longest Common Subsequence.
-> Return (n-k) + (m-k) as answer.
"""

class Solution:

    ################################
    # Tabulation Approach
    ################################

    def minOperationsTabulation(self, str):
        pass


    ################################
    # Tabulation Space Optimized Approach
    ################################

    def minOperationsTabulationSpaceOptimized(self, str):
        pass




if __name__ == "__main__":
    minOperations = Solution()

    test_cases = [
        {
            "str1": "kitten",
            "str2": "sitting",
            "output": 5
        },
        {
            "str1": "flaw",
            "str2": "lawn",
            "output": 2
        },
    ]

    for i, test_case in enumerate(test_cases):
        print("==================================")
        print(f"Test case {i+1}")
        outputTabulation = minOperations.minOperationsTabulation(test_case["str"])
        print(f"Output (Tabulation): {outputTabulation}")
        outputTabulationSpaceOptimized = minOperations.minOperationsTabulationSpaceOptimized(test_case["str"])
        print(f"Output (Tabulation Space Optimized): {outputTabulationSpaceOptimized}")

        # assert outputTabulation == test_case["output"]
        # assert outputTabulationSpaceOptimized == test_case["output"]
