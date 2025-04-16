# Minimum days to make M bouquets


# Brute Force: Linear search
# Time complexity: O(n * (maxDays - minDays)) | Space complexity: O(1)
class Solution:
    def isPossible(self, nums, day, m, k):
        bouquets = 0
        flowers = 0

        for i in range(len(nums)):
            if nums[i] <= day:
                flowers += 1
            else:
                bouquets += flowers // k
                flowers = 0

        bouquets += flowers // k

        return bouquets >= m

    def roseGarden(self, n, nums, k, m):
        noOfRoses = k * m

        if noOfRoses > n:
            return -1

        minDays = min(nums)
        maxDays = max(nums)

        for i in range(minDays, maxDays + 1):
            if self.isPossible(nums, i, m, k):
                return i

        return -1

# Brute Force: Binary search
# Time complexity: O(n * log(maxDays - minDays)) | Space complexity: O(1)
class Solution2:
    def isPossible(self, nums, day, m, k):
        bouquets = 0
        flowers = 0

        for i in range(len(nums)):
            if nums[i] <= day:
                flowers += 1
            else:
                bouquets += flowers // k
                flowers = 0

        bouquets += flowers // k

        return bouquets >= m

    def roseGarden(self, n, nums, k, m):
        noOfRoses = k * m

        if noOfRoses > n:
            return -1

        minDays = min(nums)
        maxDays = max(nums)

        low = minDays
        high = maxDays
        minNoOfDayRequired = -1
        while low <= high:
            mid = (low + high) // 2

            if self.isPossible(nums, mid, m, k):
                high = mid - 1
                minNoOfDayRequired = mid
            else:
                low = mid + 1

        return minNoOfDayRequired
