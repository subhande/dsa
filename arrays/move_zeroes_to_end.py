# Move zeros to end


# Brute Force Solution
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        arr = [0] * n
        arr_idx = 0
        for i in range(n):
            if nums[i] != 0:
                arr[arr_idx] = nums[i]
                arr_idx += 1
        for i in range(n):
            nums[i] = arr[i]

# Optimal
class SolutionOptimal:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastNonZeroFoundAt = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lastNonZeroFoundAt] = nums[i]
                lastNonZeroFoundAt += 1
        for i in range(lastNonZeroFoundAt, len(nums)):
            nums[i] = 0
