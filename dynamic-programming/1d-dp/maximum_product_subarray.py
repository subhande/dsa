# Maximum Product Subarray

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        if not nums:
            return 0

        # Initialize the max and min products with the first element.
        max_prod = min_prod = result = nums[0]

        # Iterate through the array starting at the second element.
        for num in nums[1:]:
            # When the current number is negative, swap the max and min.
            if num < 0:
                max_prod, min_prod = min_prod, max_prod

            # Calculate the max product ending here by considering:
            # 1. Starting fresh from the current number.
            # 2. Extending the previous max product.
            max_prod = max(num, max_prod * num)

            # Calculate the min product ending here by considering:
            # 1. Starting fresh from the current number.
            # 2. Extending the previous min product.
            min_prod = min(num, min_prod * num)

            # Update our result with the best max product so far.
            result = max(result, max_prod)

        return result
