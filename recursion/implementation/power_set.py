# Power Set

# Time Complexoty: O(2^n) | Space Complexity: O(n * 2^n)
class Solution:
    def backtrack(self, index, n, currSet, ans, nums):
        if index == n:
            return ans.append(currSet)
        self.backtrack(index+1, n, currSet, ans, nums)
        self.backtrack(index+1, n, currSet + [nums[index]], ans, nums)
    def powerSet(self, nums):
        ans = []
        self.backtrack(0, len(nums), [], ans, nums)
        return ans
