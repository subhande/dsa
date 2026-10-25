"""
# Build heap from a given Array
Given an array of integers nums, convert it in-place into a min-heap.

A binary min-heap is a complete binary tree where the key at the root is the minimum among all keys present in a binary min-heap and the same property is recursively true for all nodes in a Binary Tree.
--------------------------------------------
Examples:
--------------------------------------------
Input: nums = [6, 5, 2, 7, 1, 7]
Output: [1, 5, 2, 7, 6, 7]

Explanation: nums[0] <= nums[1], nums[2]
nums[1] <= nums[3], nums[4]
nums[2] <= nums[5]
--------------------------------------------
Input: nums = [2, 3, 4, 1, 7, 3, 9, 4, 6]
Output: [1, 2, 3, 3, 7, 4, 9, 4, 6]

Explanation: nums[0] <= nums[1], nums[2]
nums[1] <= nums[3], nums[4]
nums[2] <= nums[5], nums[6]
nums[3] <= nums[7], nums[8]
--------------------------------------------
Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
--------------------------------------------
"""


class Solution:
    def heapifyDown(self, arr, index, heapSize):
        """
        Maintains the min-heap property by moving the element at the given index down the heap.
        :param arr: List of integers representing the heap.
        :param index: Index of the element to heapify down.
        :param heapSize: Current size of the heap.
        """

        smallest = index  # assume the current index is the smallest value
        leftChild = 2 * index + 1
        rightChild = 2 * index + 2

        # Check if the left child exists and is smaller than the current smallest value.
        if leftChild < heapSize and arr[leftChild] < arr[smallest]:
            smallest = leftChild

        # Check if the right child exists and is smaller than the current smallest value.
        if rightChild < heapSize and arr[rightChild] < arr[smallest]:
            smallest = rightChild

        # If the smallest value is not at the current index, swap and continue heapifying down.
        if smallest != index:
            arr[index], arr[smallest] = arr[smallest], arr[index]
            self.heapifyDown(arr, smallest, heapSize)

    def buildMinHeap(self, nums):
        """
        Converts the given array into a min-heap in-place.
        :param nums: List of integers to be transformed into a min-heap.
        """

        heapSize = len(nums)

        for i in range((heapSize // 2) - 1, -1, -1):
            self.heapifyDown(nums, i, heapSize)

        return nums

    def heapifyDownMax(self, arr, index, heapSize):
        """
        Maintains the max-heap property by moving the element at the given index down the heap.
        :param arr: List of integers representing the heap.
        :param index: Index of the element to heapify down.
        :param heapSize: Current size of the heap.
        """

        largest = index  # assume the current index is the largest value
        leftChild = 2 * index + 1
        rightChild = 2 * index + 2

        # Check if the left child exists and is larger than the current largest value.
        if leftChild < heapSize and arr[leftChild] > arr[largest]:
            largest = leftChild

        # Check if the right child exists and is larger than the current largest value.
        if rightChild < heapSize and arr[rightChild] > arr[largest]:
            largest = rightChild

        # If the largest value is not at the current index, swap and continue heapifying down.
        if largest != index:
            arr[index], arr[largest] = arr[largest], arr[index]
            self.heapifyDownMax(arr, largest, heapSize)

    def buildMaxHeap(self, nums):
        """
        Converts the given array into a max-heap in-place.
        :param nums: List of integers to be transformed into a max-heap.
        """

        heapSize = len(nums)

        for i in range((heapSize // 2) - 1, -1, -1):
            self.heapifyDownMax(nums, i, heapSize)

        return nums


from binarytree import build


def print_tree(arr):
    tree = build(arr)
    print(tree)


if __name__ == "__main__":
    sol = Solution()
    nums = [6, 5, 2, 7, 1, 7]
    print_tree(nums)  # Output: [6, 5, 2, 7, 1, 7]
    nums = sol.buildMinHeap(nums)
    print_tree(nums)  # Output: [1, 5, 2, 7, 6, 7]

    nums = [2, 3, 4, 1, 7, 3, 9, 4, 6]
    print_tree(nums)  # Output: [2, 3, 4, 1, 7, 3, 9, 4, 6]
    nums = sol.buildMinHeap(nums)
    print_tree(nums)  # Output: [1, 2, 3, 3, 7, 4, 9, 4, 6]

    nums = [2, 7, 4, 1, 8, 1]
    print_tree(nums)  # Output: [2, 7 , 4, 1, 8, 1]
    nums = sol.buildMaxHeap(nums)
    print_tree(nums)  # Output: [8, 7, 4, 1, 2, 1]
