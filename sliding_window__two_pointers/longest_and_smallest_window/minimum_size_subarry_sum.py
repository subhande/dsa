from typing import List

# Solution 1: Using Prefix Sum and Two Pointers | left, right -> -1, 0
# Solution 2: Using Prefix Sum and Two Pointers with Corrected Window Size Calculation | left, right -> 0, 0
# Solution 3: Using Two Pointers and Current Window Sum | left, right -> -1, 0
# Solution 4: Using Two Pointers and Current Window Sum with Corrected Window Size Calculation | left, right -> 0, 0


class Solution1:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        n = len(nums)

        for idx in range(1, n):
            nums[idx] += nums[idx - 1]

        left, right = -1, 0

        minLength = n + 1

        while right < n:
            leftValue = 0 if left < 0 else nums[left]
            rightValue = nums[right]
            while rightValue - leftValue >= target:
                minLength = min(minLength, right - left)
                left += 1
                leftValue = nums[left]
            right += 1
        return minLength if minLength <= n else 0


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        n = len(nums)

        for idx in range(1, n):
            nums[idx] += nums[idx - 1]

        minLength = n + 1

        while right < n:
            leftValue = 0 if left == 0 else nums[left]
            rightValue = nums[right]
            while rightValue - leftValue >= target:
                minLength = min(minLength, right - left + 1)
                leftValue = nums[left]
                left += 1

            right += 1
        return minLength if minLength <= n else 0


class Solution3:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        n = len(nums)

        left, right = -1, 0

        minLength = n + 1

        currentWindowSum = 0

        while right < n:
            currentWindowSum += nums[right]
            while currentWindowSum >= target:
                minLength = min(minLength, right - left)
                left += 1
                currentWindowSum -= nums[left]
            right += 1
        return minLength if minLength <= n else 0


class Solution4:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        n = len(nums)

        minLength = n + 1

        currentWindowSum = 0

        while right < n:
            currentWindowSum += nums[right]
            while currentWindowSum >= target:
                minLength = min(minLength, right - left + 1)
                currentWindowSum -= nums[left]
                left += 1

            right += 1
        return minLength if minLength <= n else 0
