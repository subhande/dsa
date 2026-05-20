from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Sort to enable two-pointer technique and duplicate skipping
        nums.sort()
        result = []
        n = len(nums)

        for first in range(n - 3):
            # Skip duplicate values for the first element
            if first > 0 and nums[first] == nums[first - 1]:
                continue

            for second in range(first + 1, n - 2):
                # Skip duplicate values for the second element
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue

                left = second + 1
                right = n - 1

                while left < right:
                    total = nums[first] + nums[second] + nums[left] + nums[right]

                    if total == target:
                        result.append(
                            [nums[first], nums[second], nums[left], nums[right]]
                        )

                        # Skip duplicates for left and right pointers
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        left += 1
                        right -= 1

                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return result
