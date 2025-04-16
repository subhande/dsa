# Aggressive Cows

# Linear Search
# Time complexity: O(n * (max - min)) | Space complexity: O(1)
class Solution:
    def canWePlace(self, nums, dist, k):
        cows = 1
        lastPos = nums[0]

        for i in range(1, len(nums)):
            if nums[i] - lastPos >= dist:
                cows += 1
                lastPos = nums[i]
                if cows == k:
                    return True

        return False
    def aggressiveCows(self, nums, k):
        nums.sort()

        limit = nums[-1] - nums[0]

        # linear search
        for i in range(limit, 0, -1):
            if self.canWePlace(nums, i, k):
                return i

        return -1

# Binary Search
# Time complexity: O(n * log(max - min)) | Space complexity: O(1)
class Solution2:
    def canWePlace(self, nums, dist, k):
        cows = 1
        lastPos = nums[0]

        for i in range(1, len(nums)):
            if nums[i] - lastPos >= dist:
                cows += 1
                lastPos = nums[i]
                if cows == k:
                    return True

        return False
    def aggressiveCows(self, nums, k):
        nums.sort()

        low, high = 1, nums[-1] - nums[0]

        maxDist = -1

        while low <= high:
            mid = (low + high) // 2

            if self.canWePlace(nums, mid, k):
                maxDist = mid
                low = mid + 1
            else:
                high = mid - 1


        return maxDist
