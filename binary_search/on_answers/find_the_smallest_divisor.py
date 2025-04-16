# Find the smallest divisor
import math
class Solution:
    def smallestDivisor(self, nums, limit):
        # Binary search for smallest divisor
        left, right = 1, max(nums)

        while left <= right:
            mid = (left + right) // 2

            # Calculate the sum of ceil(num / mid) for all nums
            total = sum(math.ceil(num/mid) for num in nums)
            print([left, right, mid, total, limit])
            if total > limit:
                left = mid + 1
            else:
                right = mid - 1

        return left


if __name__ == "__main__":
    sol = Solution()

    nums = [1, 2, 3, 4, 5]
    limit  = 8
    output = 3
    result = sol.smallestDivisor(nums, limit)
    print(f"Smallest Divisor: {result} == {output}")

    nums = [8,4,2,3]
    limit  = 10
    output = 2
    result = sol.smallestDivisor(nums, limit)
    print(f"Smallest Divisor: {result} == {output}")
