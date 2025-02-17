# Sliding Window Maximum
"""
Given an array of integers arr, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Examples:
Input: arr = [4, 0, -1, 3, 5, 3, 6, 8], k = 3

Output: [4, 3, 5, 5, 6, 8]

Explanation:
Window position          Max
------------------------     -----
[4 0 -1] 3 5 3 6 8      4
 4 [0 -1 3] 5 3 6 8      3
 4 0 [-1 3 5] 3 6 8      5
 4 0 -1 [3 5 3] 6 8      5
 4 0 -1 3 [5 3 6] 8      6
 4 0 -1 3 5 [3 6 8]     8
For each window of size k=3, we find the maximum element in the window and add it to our output array.
"""

from collections import deque

class Solution:
    # Time complexity: O((n-k)*k) | Space complexity: O(n)
    def maxSlidingWindowBruteForce(self, arr, k):
        n = len(arr)
        maxWindow = []
        # Iterate over each window of size k.
        for i in range(n - k + 1):
            # Find the maximum element in the current window.
            maxWindow.append(max(arr[i:i+k]))
        return maxWindow

    def maxSlidingWindow(self, arr, k):
        # Result list to store maximums for each window.
        result = []
        # Deque to store indexes of useful elements (elements that might be maximum for current or future windows).
        # The deque will store indexes in such a way that their values are in decreasing order.
        dq = deque()

        for i in range(len(arr)):
            # Step 1: Remove indexes from the front (left) that are no longer in the current window.
            if dq and dq[0] < i - k + 1:
                dq.popleft()

            # Step 2: Remove from the back all indexes whose corresponding values are less than the current element,
            # since they cannot be part of the solution for the current or any future window.
            while dq and arr[dq[-1]] < arr[i]:
                dq.pop()

            # Step 3: Append the current index. It might be a candidate to be maximum in future windows.
            dq.append(i)

            # Step 4: If the window has hit its full size, append the maximum (which is at the front of the deque)
            if i >= k - 1:
                result.append(arr[dq[0]])

        return result

"""
─────────────────────────────
Explanation:

1. Purpose of the Deque:
   • Instead of checking every element in every window (which would be O(n*k)), we use a deque to maintain indexes of the numbers.
   • The deque is maintained in a way that the elements’ values are in decreasing order. This means the front (leftmost index) always points to the maximum value of the current window.

2. Sliding the Window:
   • When moving to the next element in the array, we first check if the index at the front of the deque is outside the current window (i - k + 1 is the start index of the current window). If it is, we remove it.

3. Maintaining the Deque:
   • Before adding the current element’s index, we remove all indexes from the right end of the deque whose corresponding values are less than the current element.
   • This is because, with the current element being larger, those smaller values will never be useful for determining the maximum in the current or any subsequent window that includes this element.

4. Recording the Maximum:
   • After adjusting the deque, the current maximum for the window is at the front of the deque. Once we have processed at least k elements (i.e., i >= k - 1), we record the value at the front of the deque as the maximum of the current window.

5. Time Complexity:
   • Each element is added and removed from the deque at most once, so the entire algorithm runs in O(n) time.

This approach efficiently gives the maximum of all sliding windows and is particularly useful when n is very large.
"""

if __name__ == '__main__':
    sol = Solution()

    # Test 1
    arr = [4, 0, -1, 3, 5, 3, 6, 8]
    k = 3
    # Output: [4, 3, 5, 5, 6, 8]
    print(sol.maxSlidingWindowBruteForce(arr, k))
    print(sol.maxSlidingWindow(arr, k))

    # Test 2
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    # Output: [3, 3, 5, 5, 6, 7]
    print(sol.maxSlidingWindowBruteForce(arr, k))
    print(sol.maxSlidingWindow(arr, k))
