# Maximum sum of non adjacent elements
# https://takeuforward.org/plus/dsa/dynamic-programming/1d-dp/maximum-sum-of-non-adjacent-elements


class Solution1:
    """ Function to calculate the maximum
    sum of nonAdjacent elements """
    def nonAdjacent(self, nums):
        n = len(nums)
        dp = [0] * n

        # Base case
        dp[0] = nums[0]

        # Iterate through the elements of the array
        for i in range(1, n):

            """ Calculate maximum value by either picking
            the current element or not picking it"""
            pick = nums[i]
            if i > 1:
                pick += dp[i - 2]
            nonPick = dp[i - 1]

            # Store the maximum value in dp array
            dp[i] = max(pick, nonPick)

        """ The last element of the dp array
        will contain the maximum sum"""
        return dp[-1]

class Solution2:
    """Function to calculate the maximum
    sum of nonAdjacent elements"""
    def nonAdjacent(self, nums):
        n = len(nums)
        prev = nums[0]
        prev2 = 0

        for i in range(1, n):
            # Maximum sum if we pick current element
            pick = nums[i]

            if i > 1:
                # Add the maximum sum two elements ago
                pick += prev2
            # Maximum sum if we don't pick current element
            nonPick = 0 + prev

            # Maximum at the current element
            cur_i = max(pick, nonPick)

            prev2 = prev
            prev = cur_i

        # Return the maximum sum
        return prev
