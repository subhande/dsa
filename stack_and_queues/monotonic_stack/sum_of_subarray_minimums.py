# Sum of Subarray Minimums

class Solution:
    def sumSubarrayMinsBruteForce(self, arr):
        n = len(arr)
        mod = int(1e9 + 7)
        # Initialize the sum of minimum elements in subarrays.
        subArraySumOfMinElements = 0
        # For each subarray size, find the minimum element in each subarray.
        for size in range(1, n+1):
            # Find the minimum element in each subarray of size 'size'.
            for i in range(n-size+1):
                # Add the minimum element to the sum.
                subArraySumOfMinElements = (subArraySumOfMinElements + min(arr[i:i+size])) % mod
        return subArraySumOfMinElements


    def previousSmallerElement(self, arr):
        n = len(arr)
        result = [-1] * n
        # Initialize the stack to keep track of the previous smaller elements.
        stack = []

        # Iterate through the array to find the previous smaller element for each element.
        for i in range(n):
            # Pop elements from the stack that are greater than or equal to the current element.
            while stack and stack[-1] >= arr[i]:
                stack.pop()
            # If the stack is not empty, the top of the stack is the previous smaller element.
            result[i] = stack[-1] if stack else arr[i]

            # Push the current element to the stack for future comparisons.
            stack.append(arr[i])
        return result

    def sumSubarrayMinsOptimized(self, arr):
        mod = 10**9 + 7
        n = len(arr)

        # Arrays to hold count contributions from left and right
        left = [0] * n  # counts for subarrays ending at i
        right = [0] * n # counts for subarrays starting at i

        # Compute left: for each element, count the number of contiguous subarrays ending at i
        # where arr[i] is minimum by scanning to the left.
        stack = []
        for i in range(n):
            count = 1  # at least the element itself
            # If any previous element is greater than arr[i], it cannot be the minimum.
            while stack and stack[-1][0] > arr[i]:
                count += stack.pop()[1]
            left[i] = count
            stack.append((arr[i], count))

        # Compute right: for each element, count the number of subarrays starting at i
        # where arr[i] is minimum by scanning to the right.
        stack = []
        for i in range(n - 1, -1, -1):
            count = 1
            # Notice that to avoid double counting subarrays when elements are equal,
            # we use >= so that the current value can extend subarrays where later elements
            # are equal to arr[i].
            while stack and stack[-1][0] >= arr[i]:
                count += stack.pop()[1]
            right[i] = count
            stack.append((arr[i], count))

        # Aggregate the result using the counts from left and right.
        total = 0
        print(arr)
        print(left)
        print(right)
        for i in range(n):
            total = (total + arr[i] * left[i] * right[i]) % mod

        return total


"""
The idea behind computing total += arr[i] * left[i] * right[i] is to account for every subarray in which arr[i] is the minimum element. Here's a step-by-step explanation:

1. For each element arr[i], we want to know in how many subarrays this element is the minimum.

2. The left[i] value tells you how many contiguous subarrays ending at i (extending to the left) have arr[i] as the minimum.
   • Think of moving left from index i: for each element that is greater than arr[i] (or until you reach the beginning), arr[i] will dominate as the minimum.

3. The right[i] value tells you how many contiguous subarrays starting at i (extending to the right) have arr[i] as the minimum.
   • Similarly, moving right from index i: for each element that is greater than or equal to arr[i] (and using the appropriate condition to handle duplicates), arr[i] continues to be the minimum.

4. If you have left[i] options on the left and right[i] options on the right, then the total number of subarrays where arr[i] is the minimum is exactly left[i] * right[i]. This is because for each left segment that can be paired with each right segment, you get a unique subarray where arr[i] is guaranteed to be the minimum.

5. Now, since arr[i] is the minimum for all those subarrays, the contribution of these subarrays to the sum of subarray minimums is arr[i] multiplied by the number of such subarrays, i.e., arr[i] * left[i] * right[i].

6. The overall total is then the sum of these contributions for every index i in the array.

By doing total += arr[i] * left[i] * right[i], we are effectively summing the minimum values of all subarrays, but by counting contributions from each element in an optimized way rather than by iterating over all possible subarrays explicitly.
"""

if __name__ == '__main__':

    sol = Solution()

    # Test 1
    arr = [3, 1, 2, 5]
    # Output: 18
    print(sol.sumSubarrayMinsBruteForce(arr))
    print(sol.sumSubarrayMinsOptimized(arr))

    # Test 2
    arr = [2, 3, 1]
    # Output: 10
    print(sol.sumSubarrayMinsBruteForce(arr))
    print(sol.sumSubarrayMinsOptimized(arr))
