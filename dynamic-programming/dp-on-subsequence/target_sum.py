"""
Given an array nums of n integers and an integer target, build an expression using the integers from nums where each integer can be prefixed with either a '+' or '-' sign. The goal is to achieve the target sum by evaluating all possible combinations of these signs. Determine the number of ways to achieve the target sum and return your answer with modulo 109+7.
-------------------------------------------------------------
Example 1
Input: nums = [1, 2, 7, 1, 5], target = 4
Output: 2

Explanation: There are 2 ways to assign symbols to make the sum of nums be target 4.
-1 + 2 + 7 - 1 + 5 = 4
+1 - 2 + 7 - 1 + 5 = 4
-------------------------------------------------------------
Example 2
Input: nums = [1], target = 1
Output: 1

Explanation: There is only one way to assign symbols to make the sum of nums be target 1.
-------------------------------------------------------------
Constraints:
1 ≤ n ≤ 100
0 ≤ nums[i] ≤ 1000
0 <= sum(A[i]) <= 104
-1000 <= target <= 1000
-------------------------------------------------------------
"""


class Solution:
    ################################
    # Recursive Approach
    ################################
    def targetSumRecursiveHelper(self, ind, target, arr):
        # Base case: if index is 0
        if ind == 0:
            # If target is 0 and first element is 0, there are 2 ways (include or exclude)
            if target == 0 and arr[0] == 0:
                return 2
            # If target is 0 or target is equal to the first element, there is 1 way
            if target == 0 or target == arr[0]:
                return 1
            # Otherwise, no way to achieve the target
            return 0
        # Calculate the number of ways by not taking the current element
        notTaken = self.targetSumRecursiveHelper(ind - 1, target, arr)

        # Calculate the number of ways by taking the current element
        taken = 0
        if arr[ind] <= target:
            taken = self.targetSumRecursiveHelper(ind - 1, target - arr[ind], arr)

        # Return the total number of ways
        return (notTaken + taken) % (10**9 + 7)

    def targetSumRecursive(self, n, target, nums):
        # Calculate the total sum of the array
        totSum = sum(nums)
        # If total sum is less than target, no solution exists
        if totSum < target:
            return 0
        # If (totSum + target) is odd, no solution exists
        if (totSum + target) % 2 == 1:
            return 0
        # Calculate the subset sum we need to find
        s2 = (totSum + target) // 2
        # Call the helper function to find the number of ways
        return self.targetSumRecursiveHelper(n - 1, s2, nums)

    ################################
    # Memoization Approach
    ################################
    
    def targetSumMemoizationHelper(self, ind, target, arr, dp):
        # Base case: if index is 0
        if ind == 0:
            # If target is 0 and first element is 0, there are 2 ways (include or exclude)
            if target == 0 and arr[0] == 0:
                return 2
            # If target is 0 or target is equal to the first element, there is 1 way
            if target == 0 or target == arr[0]:
                return 1
            # Otherwise, no way to achieve the target
            return 0
        # If the value is already computed, return it
        if dp[ind][target] != -1:
            return dp[ind][target]

        # Calculate the number of ways by not taking the current element
        notTaken = self.targetSumTabularHelper(ind - 1, target, arr, dp)

        # Calculate the number of ways by taking the current element
        taken = 0
        if arr[ind] <= target:
            taken = self.targetSumTabularHelper(ind - 1, target - arr[ind], arr, dp)

        # Store the result in dp array
        dp[ind][target] = (notTaken + taken) % (10**9 + 7)
        return dp[ind][target]

    def targetSumMemoization(self, n, target, nums):
        # Calculate the total sum of the array
        totSum = sum(nums)
        # If total sum is less than target, no solution exists
        if totSum < target:
            return 0
        # If (totSum + target) is odd, no solution exists
        if (totSum + target) % 2 == 1:
            return 0
        # Calculate the subset sum we need to find
        s2 = (totSum + target) // 2
        # Create a dp array
        dp = [[-1 for i in range(s2 + 1)] for j in range(n)]
        # Call the helper function to find the number of ways
        return self.targetSumTabularHelper(n - 1, s2, nums, dp)


if __name__ == "__main__":

    # Create an instance of Solution class
    sol = Solution()

    nums = [1, 2, 3, 1]
    target = 3
    n = len(nums)
    print("The total number of ways is", sol.targetSumTabular(n, target, nums))

    nums = [1, 2, 7, 1, 5]
    target = 4
    n = len(nums)
    print("The total number of ways is", sol.targetSumTabular(n, target, nums))

    num = [2, 1, 3, 1, 2]
    target = 2
    n = len(nums)
    print("The total number of ways is", sol.targetSumTabular(n, target, nums))
