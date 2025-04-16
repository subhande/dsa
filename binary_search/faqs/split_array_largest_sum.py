# Split Array Largest Sum
# Split Array Largest Sum - Leetcode 410
#
#
from typing import List
import itertools
import functools


# Time Complexity: O(n^2 * m) where n is the length of nums and m is the number of subarrays.
# Space Complexity: O(n * m) for the memoization cache.
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)

        # Create a prefix sum array of nums.
        prefix_sum = [0] + list(itertools.accumulate(nums))

        @functools.lru_cache(None)
        def get_min_largest_split_sum(curr_index: int, subarray_count: int):
            # Base Case: If there is only one subarray left, then all of the remaining numbers
            # must go in the current subarray. So return the sum of the remaining numbers.
            if subarray_count == 1:
                return prefix_sum[n] - prefix_sum[curr_index]

            # Otherwise, use the recurrence relation to determine the minimum largest subarray sum
            # between curr_index and the end of the array with subarray_count subarrays remaining.
            minimum_largest_split_sum = prefix_sum[n]
            for i in range(curr_index, n - subarray_count + 1):
                # Store the sum of the first subarray.
                first_split_sum = prefix_sum[i + 1] - prefix_sum[curr_index]

                # Find the maximum subarray sum for the current first split.
                largest_split_sum = max(first_split_sum,
                                        get_min_largest_split_sum(i + 1, subarray_count - 1))

                # Find the minimum among all possible combinations.
                minimum_largest_split_sum = min(minimum_largest_split_sum, largest_split_sum)

                '''As we iterate through different possible split points (i), the first_split_sum (the sum of elements from curr_index to i) is monotonically increasing because we're adding more elements to it.
                If we reach a point where first_split_sum (the sum of just the first partition) is already greater than or equal to our current best solution (minimum_largest_split_sum), then continuing to explore later split points is pointless because:

                The first_split_sum will only get larger as i increases
                The largest split sum would be at least as large as first_split_sum
                Therefore, we can't get a better result than our current minimum_largest_split_sum'''
                if first_split_sum >= minimum_largest_split_sum:
                    break

            return minimum_largest_split_sum

        return get_min_largest_split_sum(0, m)


# Optimal Solution using Binary Search
# Time Complexity: O(n * log(sum(nums))) where n is the length of nums and sum(nums) is the total sum of the array.
# Space Complexity: O(1) for the binary search variables.

class Solution2:
    def splitArray(self, nums: List[int], m: int) -> int:

        def min_subarrays_required(max_sum_allowed: int) -> int:
            current_sum = 0
            splits_required = 0

            for element in nums:
                # Add element only if the sum doesn't exceed max_sum_allowed
                if current_sum + element <= max_sum_allowed:
                    current_sum += element
                else:
                    # If the element addition makes sum more than max_sum_allowed
                    # Increment the splits required and reset sum
                    current_sum = element
                    splits_required += 1

            # Return the number of subarrays, which is the number of splits + 1
            return splits_required + 1

        # Define the left and right boundary of binary search
        left = max(nums)
        right = sum(nums)
        minimum_largest_split_sum = -1
        while left <= right:
            # Find the mid value
            max_sum_allowed = (left + right) // 2

            # Find the minimum splits. If splits_required is less than
            # or equal to m move towards left i.e., smaller values
            if min_subarrays_required(max_sum_allowed) <= m:
                right = max_sum_allowed - 1
                minimum_largest_split_sum = max_sum_allowed
            else:
                # Move towards right if splits_required is more than m
                left = max_sum_allowed + 1

        return minimum_largest_split_sum


class Solution3:
    def isPossible(self, nums, mid, m):
        splitRequired = 1
        currentSum = 0
        for i in range(len(nums)):
            currentSum += nums[i]

            if currentSum > mid:
                splitRequired += 1
                currentSum = nums[i]

            if splitRequired > m:
                return False
        return True
    def splitArray(self, nums: List[int], m: int) -> int:
        totalSum = sum(nums)
        maxElement = max(nums)

        if len(nums) < m:
            return -1

        left, right = maxElement, totalSum
        minimumLargestSplitSum = -1
        while left <= right:

            mid = (left + right) // 2

            if self.isPossible(nums, mid, m):
                right = mid - 1
                minimumLargestSplitSum = mid
            else:
                left = mid + 1

        return minimumLargestSplitSum
