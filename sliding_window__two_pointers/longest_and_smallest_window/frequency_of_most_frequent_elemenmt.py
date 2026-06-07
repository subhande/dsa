from typing import List


# Approach 1: Brute Force
# Time Complexity: O(n^2) | Space Complexity: O(n)
class Solution1:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        maxCount = 0
        for idx in range(n - 1, -1, -1):
            ele = nums[idx]
            temp = nums[:]
            count = 0
            buffer = k
            for sc_idx in range(idx, -1, -1):
                temp[sc_idx] = ele - temp[sc_idx]
                if temp[sc_idx] > buffer:
                    break

                buffer -= temp[sc_idx]
                count += 1

            maxCount = max(maxCount, count)
        return maxCount


# Approach 2: Sliding Window
# Time Complexity: O(n log n) | Space Complexity: O(1)
class Solution2:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, 0
        window_sum = 0
        maxFrequency = 0
        n = len(nums)
        while right < n:
            target = nums[right]
            window_sum += target

            while (right - left + 1) * target - window_sum > k:
                window_sum -= nums[left]
                left += 1

            maxFrequency = max(maxFrequency, right - left + 1)
            right += 1

        return maxFrequency
