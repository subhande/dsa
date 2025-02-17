# Next Greater Element II
"""
Given a circular integer array arr, return the next greater element for every element in arr.
The next greater element for an element x is the first element greater than x that we come across while traversing the array in a clockwise manner.
If it doesn't exist, return -1 for that element element.
"""

"""
Explanation:

1. Brute Force Approach:
   • For each index i, we check the next n-1 numbers (using modulo n for circularity).
   • As soon as we find a number greater than arr[i], we set that as the answer for index i.
   • If no greater number is found after checking all, we leave it as -1.

2. Optimized Approach Using a Stack:
   • We iterate through the array twice from right to left (i.e. from 2n-1 down to 0).
   • The stack keeps potential “next greater” candidates in descending order.
   • For each element, we pop elements from the stack that are less than or equal to it.
   • If we’re in the first pass (i < n), the top of the stack (if any) is the next greater element.
   • Finally, we push the current element to the stack for future comparisons.

Both methods ultimately return the correct next greater element for every element in the circular array.
"""
class Solution:
    # Time complexity: O(n^2) | Space complexity: O(n)
    def nextGreaterElementsBruteForce(self, arr):
        n = len(arr)
        result = [-1] * n
        # For each element, search ahead circularly.
        for i in range(n):
            # Try to find the next greater element by checking the next n-1 elements.
            for j in range(1, n):
                cand = arr[(i + j) % n]
                if cand > arr[i]:
                    result[i] = cand
                    break
        return result
    # Time complexity: O(n) | Space complexity: O(n)
    def nextGreaterElementsOptimized(self, arr):
        n = len(arr)
        result = [-1] * n
        stack = []  # This will store values (or you can also store indices)

        # We simulate circularity by iterating twice through the array.
        # Iterating backwards allows us to process and keep candidates in stack.
        for i in range(2 * n - 1, -1, -1):
            # Use modulo to simulate circular array.
            current = arr[i % n]
            # Pop elements that are not greater than current.
            while stack and stack[-1] <= current:
                stack.pop()
            # For the first pass (i < n): assign next greater if exists.
            if i < n:
                # If stack is not empty, the top is next greater element.
                if stack:
                    result[i] = stack[-1]
                else:
                    result[i] = -1
            # Push the current element as a possible candidate for the left elements.
            stack.append(current)
        return result

if __name__ == '__main__':
    sol = Solution()

    # Test 1
    arr = [3, 10, 4, 2, 1, 2, 6, 1, 7, 2, 9]
    # Output: [10, -1, 6, 6, 2, 6, 7, 2, 9, 9, 10]
    print(sol.nextGreaterElementsBruteForce(arr))
    print(sol.nextGreaterElementsOptimized(arr))

    # Test 2
    arr =  [5, 7, 1, 7, 6, 0]
    # Output: [7, -1, 7, -1, 7, 5]
    print(sol.nextGreaterElementsBruteForce(arr))
    print(sol.nextGreaterElementsOptimized(arr))
