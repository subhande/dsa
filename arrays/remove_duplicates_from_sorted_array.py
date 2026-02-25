# Remove Duplicates from Sorted Array

from typing import List

# Approach 1: Brute Force
# Time Complexity: O(n) | Space Complexity: O(n)

class Solution:
    # Function to remove duplicates from the array
    def removeDuplicates(self, nums):

        # Set data structure to store unique elements
        s = set()

        # Add all elements from array to the set
        for val in nums:
            s.add(val)

        # Get the sorted list of unique elements
        sorted_unique = sorted(s)

        # Copy unique elements from sorted list to array
        for j in range(len(sorted_unique)):
            nums[j] = sorted_unique[j]

        # Return the number of unique elements
        return len(sorted_unique)


# Approach 2: Two Pointers
# Time Complexity: O(n) | Space Complexity: O(1)


class Solution2:
    # Function to remove duplicates from the list
    def removeDuplicates(self, nums: List[int]) -> int:
        # Initialize pointer for unique elements
        i = 0
        # Iterate through the list
        for j in range(1, len(nums)):
            """ If current element is different
            from the previous unique element"""
            if nums[i] != nums[j]:

                """ Move to the next position in
                the list for the unique element"""
                i += 1

                """ Update the current position
                with the unique element"""
                nums[i] = nums[j]
        # Return the number of unique elements
        return i + 1

    def removeDuplicates2(self, nums: List[int]) -> int:
            size = len(nums)
            insertIndex = 1
            for i in range(1, size):
                # Found unique element
                if nums[i - 1] != nums[i]:
                    # Updating insertIndex in our main array
                    nums[insertIndex] = nums[i]
                    # Incrementing insertIndex count by 1
                    insertIndex = insertIndex + 1
            return insertIndex
