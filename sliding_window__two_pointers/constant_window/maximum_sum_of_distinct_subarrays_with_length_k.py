from typing import List


# Time Complexity: O(n) where n is the length of input array nums | Space Complexity: O(k) where k is the size of the window
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

        window_start = 0

        current_window = {}

        maxSumOfDistinctEle = 0

        currWindowSum = 0

        for window_end in range(len(nums)):
            curr_num = nums[window_end]

            current_window[curr_num] = current_window.get(curr_num, 0) + 1

            currWindowSum += curr_num

            if window_end - window_start + 1 > k:
                ougoing_num = nums[window_start]

                if ougoing_num in current_window:
                    current_window[ougoing_num] -= 1

                    if current_window[ougoing_num] <= 0:
                        del current_window[ougoing_num]

                currWindowSum -= ougoing_num

                window_start += 1

            if len(current_window) == k:
                maxSumOfDistinctEle = max(maxSumOfDistinctEle, currWindowSum)
        return maxSumOfDistinctEle
