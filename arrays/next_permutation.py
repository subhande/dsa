# https://leetcode.com/problems/next-permutation/description/?envType=company&envId=google&favoriteSlug=google-three-months
# Next Permutation


"""
Explanation
------------
1. Traverse from right-to-left to find the first element (pivot) that is smaller than its next element.
2. If such a pivot is found, find the first element from the end that is greater than the pivot.
3. Swap the pivot with that element.
4. Finally, reverse the portion of the list to the right of the pivot.
"""

class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        # Find the first index "i" from the right such that nums[i] < nums[i+1]
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # If such an index was found, find the element to swap with.
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Swap the pivot nums[i] with nums[j]
            nums[i], nums[j] = nums[j], nums[i]

        # Reverse the elements in nums[i+1:]
        left = i + 1
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

# Example usage:
if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 3]
    sol.nextPermutation(nums)
    print(nums)  # Output should be [1, 3, 2]
    nums = [1, 2, 4, 9, 8, 7, 6, 5, 3]
    sol.nextPermutation(nums)
    print(nums)  # Output should be [1, 2, 5, 3, 4, 6, 7, 8, 9]
