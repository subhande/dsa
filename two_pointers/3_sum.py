# 3 SUM

from typing import List


# Approach 1: Two Pointers
# Time Complexity: O(n^2) | Space Complexity: O(n)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = {}
        target = 0
        n = len(nums)
        for i in range(n-2):
            left = i+1
            right = n-1
            if nums[i] > 0:
                break
            while left < right:
                currentSum = nums[i] + nums[left] + nums[right]
                if currentSum == target:
                    triplet = [nums[i] , nums[left] , nums[right]]
                    triplets[str(triplet)] = triplet
                    left += 1
                    right -= 1
                elif currentSum < target:
                    left += 1
                elif currentSum > target:
                    right -= 1

        return list(triplets.values())

# Approach 2: Hashing
# Time Complexity: O(n^2) | Space Complexity: O(n)
class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = {}
        target = 0
        n = len(nums)
        for i in range(n-2):
            if nums[i] > 0:
                break
            seen = set()
            for j in range(i+1, n):
                complement = target - nums[i] - nums[j]
                if complement in seen:
                    triplet = [nums[i], complement, nums[j]]
                    triplets[str(triplet)] = triplet
                seen.add(nums[j])

        return list(triplets.values())
