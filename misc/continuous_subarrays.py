# Continuous Subarrays


from typing import List

# Time Complexity: O(n^2) | Space Complexity: O(n^2)
# Brute Force | Time Limit Exceeded
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        minMaxHashMap = {}
        n = len(nums)
        count = 0
        for i in range(n):
            minMaxHashMap[(i,i)] = (nums[i], nums[i])
            count += 1

        for i in range(n-1):
            if abs(nums[i]-nums[i+1]) <= 2:
                minMaxHashMap[(i,i+1)] = (nums[i], nums[i+1]) if nums[i] < nums[i+1] else (nums[i+1], nums[i])
                count += 1

        for length in range(3, n+1):
            for i in range(n-length+1):
                j = i + length - 1
                if (i+1, j-1) in minMaxHashMap:
                    prev_min, prev_max = minMaxHashMap[(i+1, j-1)]
                    new_min = min(nums[i], nums[j], prev_min)
                    new_max = max(nums[i], nums[j], prev_max)
                    if new_max - new_min <= 2:
                        minMaxHashMap[(i,j)] = (new_min, new_max)
                        count += 1
        return count
