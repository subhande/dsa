# Left/Right Rotate Array by K Places


# Approach 1: Using Temporary Array
# Time Complexity: O(n) | Space Complexity: O(k)
class Solution:
    def rotateArrayLeft(self, nums, k):
        n = len(nums)
        if n == 0:
            return
        # Normalize k to ensure it is within the bounds of the array length
        k = k % n

        # If k is 0, no rotation is needed
        temp = nums[:k]

        # Shift the elements to the left by k places
        for i in range(k, n):
            nums[i - k] = nums[i]

        # Place the saved elements at the end of the array
        for i in range(k):
            nums[n - k + i] = temp[i]

        return nums

    def rotateArrayRight(self, nums, k):
        n = len(nums)
        if n == 0:
            return
        # Normalize k to ensure it is within the bounds of the array length
        k = k % n

        # If k is 0, no rotation is needed
        temp = nums[-k:]

        # Shift the elements to the right by k places
        for i in range(n - 1, k - 1, -1):
            nums[i] = nums[i - k]

        # Place the saved elements at the start of the array
        for i in range(k):
            nums[i] = temp[i]

        return nums


# Approach 2: Using Reversal Algorithm
# Time Complexity: O(n) | Space Complexity: O(1)
"""
------------------------------------------------------
# Left Rotate Array by K Places
1. Reverse the first k elements.
2. Reverse the remaining n-k elements.
3. Reverse the entire array.

e.g.

Input: nums = [1, 2, 3, 4, 5, 6, 7], k = 3

1. Reverse the first 3 elements: [3, 2, 1, 4, 5, 6, 7]
2. Reverse the remaining 4 elements: [3, 2, 1, 7, 6, 5, 4]
3. Reverse the entire array: [4, 5, 6, 7, 1, 2, 3]

------------------------------------------------------

# Right Rotate Array by K Places
1. Reverse the entire array.
2. Reverse the first k elements.
3. Reverse the remaining n-k elements.

e.g.
Input: nums = [1, 2, 3, 4, 5, 6, 7], k = 3
# 1. Reverse the entire array: [7, 6, 5, 4, 3, 2, 1]
# 2. Reverse the first 3 elements: [5, 6, 7, 4, 3, 2, 1]
# 3. Reverse the remaining 4 elements: [5, 6, 7, 1, 2, 3, 4]

"""

class Solution2:
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    def rotateArrayLeft(self, nums, k):
        n = len(nums)
        if n == 0:
            return
        # Normalize k to ensure it is within the bounds of the array length
        k = k % n

        # Reverse the first k elements
        self.reverse(nums, 0, k - 1)

        # Reverse the remaining n-k elements
        self.reverse(nums, k, n - 1)

        # Reverse the entire array
        self.reverse(nums, 0, n - 1)

        return nums

    def rotateArrayRight(self, nums, k):
        n = len(nums)
        if n == 0:
            return
        # Normalize k to ensure it is within the bounds of the array length
        k = k % n

        # Reverse the entire array
        self.reverse(nums, 0, n - 1)

        # Reverse the first k elements
        self.reverse(nums, 0, k - 1)

        # Reverse the remaining n-k elements
        self.reverse(nums, k, n - 1)

        return nums
