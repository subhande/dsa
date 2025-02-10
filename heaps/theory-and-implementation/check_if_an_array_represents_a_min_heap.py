"""
# Check if an array represents a min heap

Given an array of integers nums. Check whether the array represents a binary min-heap or not. Return true if it does, otherwise return false.
A binary min-heap is a complete binary tree where the key at the root is the minimum among all keys present in a binary min-heap and the same property is recursively true for all nodes in a Binary Tree.
--------------------------------------------
Examples:
--------------------------------------------
Input: nums = [10, 20, 30, 21, 23]
Output: true
Explanation: Each node has a lower or equal value than its children.
--------------------------------------------
Input: nums = [10, 20, 30, 25, 15]
Output: false
Explanation: The node with value 20 has a child with value 15, thus it is not a min-heap.
--------------------------------------------
Input: nums = [1, 2, 1, 3]
Output: true
Explanation: Each node has a lower or equal value than its children.
--------------------------------------------
Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
The array represents a complete binary tree.
--------------------------------------------
"""

class Solution:
    def isHeap(self, nums):
        """
        Check whether the given array represents a binary min-heap or not.
        :param nums: List of integers representing the array.
        :return: True if the array represents a binary min-heap, False otherwise.
        """

        n = len(nums)
        # Iterate over all parent nodes or non-leaf nodes
        for idx in range(n // 2 - 1, -1, -1):
            leftChildIdx = 2 * idx + 1
            rightChildIdx = 2 * idx + 2
            ele = nums[idx]
            # if left child is smaller than the parent node
            if leftChildIdx < n and nums[leftChildIdx] < ele:
                return False
            # if right child is smaller than the parent node
            if rightChildIdx < n and nums[rightChildIdx] < ele:
                return False
        return True


def main():
    nums = [10, 20, 30, 21, 23]

    print("Given Array: ", end="")
    for x in nums:
        print(x, end=" ")

    # Creating an object of the Solution class
    sol = Solution()

    # Function call to check if the given array is a min-heap
    ans = sol.isHeap(nums)

    if ans:
        print("\nThe given array is a min-heap.")
    else:
        print("\nThe given array is not a min-heap.")

if __name__ == "__main__":
    main()
