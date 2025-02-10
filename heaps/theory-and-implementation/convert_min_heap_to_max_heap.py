"""
# Convert Min Heap to Max Heap

Given a min-heap in array representation named nums, convert it into a max-heap and return the resulting array.

A min-heap is a complete binary tree where the key at the root is the minimum among all keys present in a binary min-heap and the same property is recursively true for all nodes in the Binary Tree.

A max-heap is a complete binary tree where the key at the root is the maximum among all keys present in a binary max-heap and the same property is recursively true for all nodes in the Binary Tree.
---------------------------------------
Examples:
---------------------------------------
Input: nums = [10, 20, 30, 21, 23]
Output: [30, 21, 23, 10, 20]
---------------------------------------
Input: nums = [-5, -4, -3, -2, -1]
Output: [-1, -2, -3, -4, -5]
---------------------------------------
Input: nums = [2, 6, 3, 100, 120, 4, 5]
Output: [120, 100, 5, 2, 6, 4, 3]
---------------------------------------
Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
nums represents a min-heap
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

    def minToMaxHeap(self, nums):
        size = len(nums)

        # Iterate over all non-leaf nodes and heapify down
        for i in range(size // 2 - 1, -1, -1):
            self.heapifyDown(i, nums, size)

        return nums


def main():
    nums = [2, 6, 3, 100, 120, 4, 5]


    print("Initial Min-heap Array: ", end="")
    for x in nums:
        print(x, end=" ")

    # Creating an object of the Solution class
    sol = Solution()

    # Function call to convert the given array from min-heap to max-heap
    nums = sol.minToMaxHeap(nums)

    print("\nMax-heap converted Array: ", end="")
    for x in nums:
        print(x, end=" ")

if __name__ == "__main__":
    main()
