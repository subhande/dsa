
"""
# Heap Sort

Given an array of integers nums, sort the array in non-decreasing order using the heap sort algorithm. Sort the given array itself, there is no need to return anything.

A sorted array in non-decreasing order is one in which each element is either greater than or equal to all the elements to its left in the array.
---------------------------------------
Examples:
---------------------------------------
Input: nums = [7, 4, 1, 5, 3]
Output: [1, 3, 4, 5, 7]

Explanation:1 <= 3 <= 4 <= 5 <= 7.
One possible way to get the sorted array using heapSort :
[7, 4, 1, 5, 3] -> [3, 4, 1, 5, 7]
-> [5, 4, 1, 3, 7] -> [3, 4, 1, 5, 7]
-> [4, 3, 1, 5, 7] -> [1, 3, 4, 5, 7]
-> [3, 1, 4, 5, 7] -> [1, 3, 4, 5, 7]
-> [1, 3, 4, 5, 7] -> [1, 3, 4, 5, 7]
---------------------------------------
Input: nums = [5, 4, 4, 1, 1]
Output: [1, 1, 4, 4, 5]
Explanation: 1 <= 1 <= 4 <= 4 <= 5.
Thus the array is sorted in non-decreasing order.
---------------------------------------
Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
nums[i] may contain duplicate values.
------------------------------------
Approach:
    - Build a max-heap from the given array using HeapifyDown for all non-leaf nodes.
    - Iterate over all elements of the heap.
    - Swap the root of the heap with the last element of the heap.
    - Reduce the size of the heap by 1.
    - Maintain the max-heap property of the heap.
    - Repeat the above steps until the heap is sorted.
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

    def heapSort(self, nums):
        # Build a max-heap from the given array
        self.buildMaxHeap(nums)
        size = len(nums)
        # Iterate over all elements of the heap
        for i in range(size - 1, 0, -1):
            # Swap the root of the heap with the last element of the heap
            nums[0], nums[i] = nums[i], nums[0]
            # Reduce the size of the heap by 1
            size -= 1
            # Maintain the max-heap property of the heap
            self.heapifyDown(0, nums, size)
        return

# Driver code
if __name__ == "__main__":
    nums = [60, 30, 40, 20, 10, 50]

    print("Input Array:", end=" ")
    for x in nums:
        print(x, end=" ")

    # Creating an object of Solution class
    sol = Solution()

    # Function call to sort the array using heap-sort
    sol.heapSort(nums)

    print("\nSorted Array:", end=" ")
    for x in nums:
        print(x, end=" ")
