# Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/editorial/
# https://leetcode.com/discuss/post/5804713/google-l4-bangalore-rejected-by-anonymou-5gal/

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak

# Longest Increasing Consicutive Subsequence
from typing import List

class Solution2:
    def longestIncreasingConsecutiveSubsequence(self, arr: List[int]) -> List[int]:
        if not arr:
            return []

        # Initialize
        max_start = 0         # start index of max subsequence
        max_len = 1           # length of max subsequence
        curr_start = 0        # start index of current subsequence
        curr_len = 1          # length of current subsequence

        # Walk through the array
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                # still increasing, extend current
                curr_len += 1
            else:
                # reset current
                if curr_len > max_len:
                    max_len = curr_len
                    max_start = curr_start
                curr_start = i
                curr_len = 1

        # Final check in case the longest ends at the last element
        if curr_len > max_len:
            max_len = curr_len
            max_start = curr_start

        # Slice out the subsequence
        return arr[max_start : max_start + max_len]


# Longest Increasing Consicutive Subsequence with Max k diff

from typing import List
class Solution3:
    def longestIncreasingSubsequenceWithMaxDiff(self, arr: List[int], k: int) -> List[int]:
        if not arr:
            return []

        max_start = curr_start = 0
        max_len = curr_len = 1

        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]
            # continue current run if it’s increasing but not too steep
            if 0 < diff <= k:
                curr_len += 1
            else:
                # check if the run we just ended is the best so far
                if curr_len > max_len:
                    max_len, max_start = curr_len, curr_start
                # start a new run at i
                curr_start, curr_len = i, 1

        # final check in case the best run ends at the last element
        if curr_len > max_len:
            max_len, max_start = curr_len, curr_start

        return arr[max_start : max_start + max_len]
