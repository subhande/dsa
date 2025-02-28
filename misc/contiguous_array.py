"""
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.



Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.


Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.

"""
from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        running_count = 0
        seen = {0: -1}  # running_count: first index it was seen
        max_length = 0

        for index, num in enumerate(nums):
            # update running count: decrement for 0, increment for 1.
            running_count += -1 if num == 0 else 1

            if running_count in seen:
                max_length = max(max_length, index - seen[running_count])
            else:
                seen[running_count] = index

        return max_length
