# Book Allocation Problem


class Solution:
    def isPossible(self, nums, mid, m):
        students = 1
        pages = 0

        for i in range(len(nums)):
            pages += nums[i]

            if pages > mid:
                students += 1
                pages = nums[i]

            if students > m:
                return False

        return True

    def findPages(self, nums, m):
        totalPages = sum(nums)
        maxPagesInABook = max(nums)

        if len(nums) < m:
            return -1

        low, high = maxPagesInABook, totalPages
        maximumPages = -1
        while low <= high:

            mid = (low + high) // 2

            if self.isPossible(nums, mid, m):
                high = mid - 1
                maximumPages = mid
            else:
                low = mid + 1

        return maximumPages
