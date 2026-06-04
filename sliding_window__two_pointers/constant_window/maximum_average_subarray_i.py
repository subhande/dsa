from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = float("-inf")
        n = len(nums)
        total_sum = 0
        for i in range(k):
            total_sum += nums[i]
        max_sum = total_sum
        for i in range(k, n):
            total_sum += nums[i] - nums[i - k]
            max_sum = max(total_sum, max_sum)
        return max_sum / k


class Solution2:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        n = len(nums)
        currSum = sum(nums[:k])
        maxAvg = currSum / k

        for i in range(1, n - k + 1):
            currSum -= nums[i - 1]
            currSum += nums[i + k - 1]

            maxAvg = max(maxAvg, currSum / k)

        return maxAvg
