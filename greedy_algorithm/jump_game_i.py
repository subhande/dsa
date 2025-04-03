# Jump Game I


class Solution:
    # Function to determine if the last index is reachable
    def canJump(self, jumps):
        # Initialize the maximum reachable index
        max_reachable_index = 0

        # Iterate through each index of the array
        for current_index in range(len(jumps)):
            # If the current index is greater than the maximum reachable index,
            # it means we cannot proceed further, so return False
            if current_index > max_reachable_index:
                return False

            # Update the maximum reachable index by comparing the current
            # maximum and the sum of the current index and the jump at that index
            max_reachable_index = max(max_reachable_index, current_index + jumps[current_index])

        # If we complete the loop, it means we can reach the last index
        return True





from typing import List
class Solution2:
    def canJump(self, nums: List[int]):
        n = len(nums)
        dp = [False] * n
        dp[0] = True
        for i in range(1, n):
            for k in range(i-1, -1, -1):
                if not dp[i]:
                    dp[i] = nums[k] >= i-k and dp[k]
        return dp[-1]
