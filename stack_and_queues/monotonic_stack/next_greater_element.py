# Next Greater Element


"""
Approach 1: Brute Force
• For each index i, we check the next n-1 numbers (using modulo n for circularity).
• As soon as we find a number greater than arr[i], we set that as the answer for index i.
• If no greater number is found after checking all, we leave it as -1.

Approach 2: Optimized Approach Using a Stack
• We iterate through the array once from right to left (i.e. from n-1 down to 0).
• The stack keeps potential “next greater” candidates in descending order.
• For each element, we pop elements from the stack that are less than or equal to it.
• Assign the top of the stack (if any) as the next greater element.

"""

class Solution:

    # Time complexity: O(n^2) | Space complexity: O(n)
    def nextLargerElementBruteForce(self, arr):
        n = len(arr)
        # Create a result list filled with -1
        result = [-1] * n

        # For each element in the array, check the subsequent elements to find a larger one
        for i in range(n):
            for j in range(i + 1, n):
                if arr[j] > arr[i]:
                    result[i] = arr[j]
                    break  # Exit the inner loop once the next greater element is found
        return result

    # Time complexity: O(n) | Space complexity: O(n)
    def nextLargerElement(self, arr):
        n = len(arr)
        # Initialize the result list with default value -1 for each element
        result = [-1] * n
        # Use a stack to keep track of the potential next greater elements
        stack = []

        # Traverse the array from right to left
        for i in range(n - 1, -1, -1):
            # Pop elements that are less than or equal to arr[i]
            while stack and stack[-1] <= arr[i]:
                stack.pop()
            # If stack is not empty, then the top element is the next larger element
            if stack:
                result[i] = stack[-1]
            # Push the current element onto the stack
            stack.append(arr[i])

        return result

"""
arr = [1, 3, 2, 4]

------
idx = 3, arr[i] = 4
stack = [4]
------
idx = 2, arr[i] = 2
stack | True and stack[-1] <= arr[i] | 4 <= 2 | False -> False
result = [-1, -1, 4, -1]
stack = [4, 2]
------
idx = 1, arr[i] = 3
stack | True and stack[-1] <= arr[i] | 2 <= 3 | True -> True
stack | True and stack[-1] <= arr[i] | 4 <= 3 | False -> False
result = [-1, 4, 4, -1]
stack = [4, 3]
------
idx = 0, arr[i] = 1
stack | True and stack[-1] <= arr[i] | 3 <= 1 | False -> False
result = [3, 4, 4, -1]
stack = [4, 3, 1]
-----
Output: [3, 4, 4, -1]
=====================
arr = [5, 6, 7, 3, 1, 2, 4]
----
idx = 6, arr[i] = 4
stack = [4]
----
idx = 5, arr[i] = 2
stack | True and stack[-1] <= arr[i] | 4 <= 2 | False -> False
result = [-1, -1, -1, -1, -1, 4, -1]
stack = [4, 2]
----
idx = 4, arr[i] = 1
stack | True and stack[-1] <= arr[i] | 2 <= 1 | False -> False
result = [-1, -1, -1, -1, 2, 4, -1]
stack = [4, 2, 1]
----
idx = 3, arr[i] = 3
stack | True and stack[-1] <= arr[i] | 1 <= 3 | True -> True
stack | True and stack[-1] <= arr[i] | 2 <= 3 | True -> True
stack | True and stack[-1] <= arr[i] | 4 <= 3 | False -> False
result = [-1, -1, -1, 4, 2, 4, -1]
stack = [4, 3]
----
idx = 2, arr[i] = 7
stack | True and stack[-1] <= arr[i] | 3 <= 7 | True -> True
stack | True and stack[-1] <= arr[i] | 4 <= 7 | True -> True
stack = [7]
result = [-1, -1, -1, 4, 2, 4, -1]
---
idx = 1, arr[i] = 6
stack | True and stack[-1] <= arr[i] | 7 <= 6 | False -> False
result = [-1, 7, -1, 4, 2, 4, -1]
stack = [7, 6]
---
idx = 0, arr[i] = 5
stack | True and stack[-1] <= arr[i] | 6 <= 5 | False -> False
result = [6, 7, -1, 4, 2, 4, -1]
stack = [7, 6, 5]
---
Output: [6, 7, -1, 4, 2, 4, -1]
"""

if __name__ == '__main__':
    sol = Solution()

    # Test 1
    arr = [1, 3, 2, 4]
    # Output: [3, 4, 4, -1]
    print(sol.nextLargerElementBruteForce(arr))
    print(sol.nextLargerElement(arr))

    # Test 2
    arr = [4, 3, 2, 1]
    # Output: [-1, -1, -1, -1]
    print(sol.nextLargerElementBruteForce(arr))
    print(sol.nextLargerElement(arr))

    # Test 3
    arr = [1, 2, 3, 4]
    # Output: [2, 3, 4, -1]
    print(sol.nextLargerElementBruteForce(arr))
    print(sol.nextLargerElement(arr))

    # Test 3
    arr = [5, 6, 7, 3, 1, 2, 4]
    # Output: [6, 7, -1, 4, 2, 4, -1]
    print(sol.nextLargerElementBruteForce(arr))
    print(sol.nextLargerElement(arr))
