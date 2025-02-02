"""
## Edit distance

Given two strings start and target, you need to determine the minimum number of operations required to convert the string start into the string target. The operations you can use are:

Insert a character: Add any single character at any position in the string.
Delete a character: Remove any single character from the string.
Replace a character: Change any single character in the string to another character.

The goal is to transform start into target using the fewest number of these operations.

------------------------------------------------------------
Examples:
------------------------------------------------------------
Input: start = "planet", target = "plan"

Output: 2

Explanation:
To transform "planet" into "plan", the following operations are required:
1. Delete the character 'e': "planet" -> "plan"
2. Delete the character 't': "plan" -> "plan"
Thus, a total of 2 operations are needed.
------------------------------------------------------------
Input: start = "abcdefg", target = "azced"

Output: 4

Explanation:
To transform "abcdefg" into "azced", the following operations are required:
1. Replace 'b' with 'z': "abcdefg" -> "azcdefg"
2. Delete 'd': "azcdefg" -> "azcefg"
3. Delete 'f': "azcefg" -> "azceg"
4. Replace 'g' with 'd': "azceg" -> "azced"
Thus, a total of 4 operations are needed.
------------------------------------------------------------
Constraints:
1 ≤ start.length, target.length ≤ 1000
"""


"""
Solution:
--------------

"""

class Solution:

    ################################
    # Recursion Approach
    ################################

    def editDistanceRecursionHelper(self, start, target, i, j):
        if i < 0:
            return j + 1
        if j < 0:
            return i + 1

        if start[i] == target[j]:
            return self.editDistanceRecursionHelper(start, target, i - 1, j - 1)
        else:
            return 1 + min(
                self.editDistanceRecursionHelper(start, target, i - 1, j),
                self.editDistanceRecursionHelper(start, target, i, j - 1),
                self.editDistanceRecursionHelper(start, target, i - 1, j - 1)
            )

    def editDistanceRecursion(self, start, target):
        n, m = len(start), len(target)
        return self.editDistanceRecursionHelper(start, target, n - 1, m - 1)


    ################################
    # Recursion with Memoization Approach
    ################################

    def editDistanceRecursionMemoizationHelper(self, start, target, i, j, dp):
        if i < 0:
            return j + 1
        if j < 0:
            return i + 1
        if dp[i][j] != -1:
            return dp[i][j]

        if start[i] == target[j]:
            dp[i][j] = self.editDistanceRecursionMemoizationHelper(start, target, i - 1, j - 1, dp)
        else:
            dp[i][j] = 1 + min(
                self.editDistanceRecursionMemoizationHelper(start, target, i - 1, j, dp),
                self.editDistanceRecursionMemoizationHelper(start, target, i, j - 1, dp),
                self.editDistanceRecursionMemoizationHelper(start, target, i - 1, j - 1, dp)
            )
        return dp[i][j]

    def editDistanceRecursionMemoization(self, start, target):
        n, m = len(start), len(target)
        dp = [[-1] * (m) for _ in range(n)]
        return self.editDistanceRecursionMemoizationHelper(start, target, n-1, m-1, dp)

    ################################
    # Tabulation Approach
    ################################

    def editDistanceTabulation(self, start, target):
        n, m = len(start), len(target)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = i
        for j in range(m + 1):
            dp[0][j] = j

        for i in range(n + 1):
            for j in range(m + 1):
                if start[i - 1] == target[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],
                        dp[i][j - 1],
                        dp[i - 1][j - 1]
                    )
        return dp[n][m]



    ################################
    # Tabulation Space Optimized Approach
    ################################

    def editDistanceTabulationSpaceOptimized(self, start, target):
        n, m = len(start), len(target)

        prev = [0] * (m + 1)
        curr = [0] * (m + 1)

        for j in range(m + 1):
            prev[j] = j

        for i in range(1, n + 1):
            curr[0] = i
            for j in range(1, m + 1):
                if start[i - 1] == target[j - 1]:
                    curr[j] = prev[j - 1]
                else:
                    curr[j] = 1 + min(
                        prev[j],
                        curr[j - 1],
                        prev[j - 1]
                    )
            prev = curr[:]
        return curr[m]





if __name__ == "__main__":
    editDistance = Solution()

    test_cases = [
        {
            "start": "planet",
            "target": "plan",
            "output": 2
        },
        {
            "start": "abcdefg",
            "target": "azced",
            "output": 4
        },
        {
            "start": "saturday",
            "target": "sunday",
            "output": 1
        },
    ]

    for i, test_case in enumerate(test_cases):
        print("==================================")
        print(f"Test case {i+1}")
        outputRecursive = editDistance.editDistanceRecursion(test_case["start"], test_case["target"])
        print(f"Output (Recursion): {outputRecursive}")

        outputRecursiveMemoization = editDistance.editDistanceRecursionMemoization(test_case["start"], test_case["target"])
        print(f"Output (Recursion with Memoization): {outputRecursiveMemoization}")

        outputTabulation = editDistance.editDistanceTabulation(test_case["start"], test_case["target"])
        print(f"Output (Tabulation): {outputTabulation}")

        outputTabulationSpaceOptimized = editDistance.editDistanceTabulationSpaceOptimized(test_case["start"], test_case["target"])
        print(f"Output (Tabulation Space Optimized): {outputTabulationSpaceOptimized}")

        # assert outputTabulation == test_case["output"]
        # assert outputTabulationSpaceOptimized == test_case["output"]
