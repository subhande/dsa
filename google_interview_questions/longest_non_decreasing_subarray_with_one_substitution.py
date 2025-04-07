# Longest Non-Decreasing Subarray with One Substitution
# https://www.geeksforgeeks.org/longest-increasing-subarray-with-one-change-allowed/
# https://leetcode.com/discuss/post/5676384/google-onsite-interview-l4-by-anonymous_-eobb/

"""
Given an array { 1, 7, 7, 2,3, 7, 6,-20}. Find the longest nondecreasing contiguous sequence with substitution. we can substitute any array element with any integer such as all occurences of 7 replaced with 1. In this way new array would be { 1,1,1,2,3,1,6,-20}.
Only one substitution is allowed.
"""
"""
Approach:
    Step 1: We first compute the longest non-decreasing subarray ending at an index for every index in the given array. We store these values in l[].
    Step 2: Then calculate the longest non-decreasing subarray starting at an index for every index in the given array. We store these values in r[].
    Step 3: Update the answer ans = max ( ans, l[i-1] + r[i+1] + 1), when a[i-1] + 1 < a[i+1].

"""

class Solution:
    def longestNonDecreasingSubarrayWithOneSubstitution(self, arr):
        n = len(arr)
        l = [1] * n
        r = [1] * n

        # Step 1: Compute l[] where l[i] is the length of longest non-decreasing
        # subarray ending at index i without any modification.
        for i in range(1, n):
            if arr[i] >= arr[i - 1]:
                l[i] = l[i - 1] + 1

        # Step 2: Compute r[] where r[i] is the length of longest non-decreasing
        # subarray starting at index i.
        for i in range(n - 2, -1, -1):
            if arr[i] <= arr[i + 1]:
                r[i] = r[i + 1] + 1


         # Without substitution, answer is the maximum in l.
        ans = max(l)
        # Step 3: Try every element as candidate for substitution.
        for i in range(n):
            # Extend using left part and/or right part depending on position.
            # left_count is the length from the left part ending at (i-1)
            left_count = l[i-1] if i-1 >= 0 else 0
            # right_count is the length from the right part starting at (i+1)
            right_count = r[i+1] if i+1 < n else 0

            if i == 0:
                # At position 0, just substitute and attach the right side.
                candidate = 1 + right_count
            elif i == n-1:
                # At last position, substitute and attach the left side.
                candidate = left_count + 1
            else:
                # Both left and right parts exist.
                # We can merge if we are allowed to pick a number X such that:
                # arr[i-1] <= X <= arr[i+1]
                if arr[i-1] <= arr[i+1]:
                    candidate = left_count + 1 + right_count
                else:
                    # Cannot bridge both sides. But we can still keep one side.
                    candidate = max(left_count, right_count) + 1

            ans = max(ans, candidate)

        return ans


if __name__ == "__main__":
    arr = [1, 7, 7, 2, 3, 7, 6, -20]
    sol = Solution()
    print(sol.longestNonDecreasingSubarrayWithOneSubstitution(arr)) # Expected output: 5
