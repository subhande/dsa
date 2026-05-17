# Increasing Triplet Subsequence
from typing import List


# Approach 1: Brute Force
# Time Complexity: O(n^3) | Space Complexity: O(1)
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[i] < nums[j] and nums[j] < nums[k]:
                        return True
        return False


# TODO: This can also be solved using LCS (DP)

"""
[2, 1, 5, 0, 4, 6]
0 < 4 < 6
[2, 1, 5, 0, 6]
1 < 5 < 6

Here in below code num1 and num2 do always represnt actual valid num1 < num2 < num3.
It represents the smallest and second smallest number in the array. If we find a number greater than num2, then we can say that there exists a triplet. It may not be num1 < num2 < num3 but we can say that there exists a triplet such that num1 < num2 < num3.

e.g. [2, 1, 5, 0, 6]

at the end of the loop, num1 = 0, num2 = 5. Now we have found a number 6 which is greater than num2. So we can say that there exists a triplet such that num1 < num2 < num3. It may not be 0 < 5 < 6 but we can say that there exists a triplet such that num1 < num2 < num3.

"""


# Approach 2: Optimal Solution
# Time Co# Time Complexity: O(n) | Space Complexity: O(1)
class Solution2:
    def increasingTriplet(self, nums: List[int]) -> bool:
        smallest_number = float("inf")
        second_smallest_number = float("inf")

        for num in nums:
            if num <= smallest_number:
                smallest_number = num
            elif num <= second_smallest_number:
                second_smallest_number = num
            else:
                return True
        return False
