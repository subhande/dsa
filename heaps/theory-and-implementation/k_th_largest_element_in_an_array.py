
"""
# K-th Largest element in an array

Given an array nums, return the kth largest element in the array.

---------------------------------------
Examples:
---------------------------------------
Input: nums = [1, 2, 3, 4, 5], k = 2
Output: 4
---------------------------------------
Input: nums = [-5, 4, 1, 2, -3], k = 5
Output: -5
---------------------------------------
"""

class Solution:
    def heapifyDown(self, index, nums, size):
        """
        Maintains the max-heap property by moving the element at the given index down the heap.
        """
        leftChildIdx = 2 * index + 1
        rightChildIdx = 2 * index + 2
        largest = index

        if leftChildIdx < size and nums[leftChildIdx] > nums[largest]:
            largest = leftChildIdx

        if rightChildIdx < size and nums[rightChildIdx] > nums[largest]:
            largest = rightChildIdx

        if largest != index:
            nums[largest], nums[index] = nums[index], nums[largest]
            self.heapifyDown(largest, nums, size)
        return

    def buildMaxHeap(self, nums):
        # Build a max-heap from the given array
        size = len(nums)
        # Iterate over all non-leaf nodes and heapify down
        for i in range(size // 2 - 1, -1, -1):
            self.heapifyDown(i, nums, size)
        return

    def kthLargestElement(self, nums, k):
        # Get the kth largest element from the given array
        # Build a max-heap from the given array
        self.buildMaxHeap(nums)

        size = len(nums)

        # Iterate over all elements of the heap
        for i in range(size - 1, size-k, -1):
            # Swap the root of the heap with the last element of the heap
            nums[0], nums[i] = nums[i], nums[0]
            # Reduce the size of the heap by 1
            size -= 1
            # Maintain the max-heap property of the heap
            self.heapifyDown(0, nums, size)
        return nums[0]


# Driver code
if __name__ == "__main__":
    nums = [-5, 4, 1, 2, -3]
    k = 5

    print("Input Array: ", nums, "k = {k}")

    # Creating an object of Solution class
    sol = Solution()

    # Function call to sort the array using heap-sort
    print(sol.kthLargestElement(nums, k))
