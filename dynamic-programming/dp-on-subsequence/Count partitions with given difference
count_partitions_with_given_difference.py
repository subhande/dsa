# Count partitions with given difference

class Solution:
    # Modulus value to avoid overflow in calculations.
    mod = int(1e9 + 7)

    """Function to calculate the number of subsets
       with a specific target sum. Uses space optimization
       to store only the previous state in the DP table."""
    def findWays(self, num, tar):
        n = len(num)

        """ DP table to store number of ways
        to achieve a certain target sum."""
        prev = [0] * (tar + 1)

        """ 2 cases for target 0 when the first
        element is 0: either pick it or not."""
        if num[0] == 0:
            prev[0] = 2

        else:
            prev[0] = 1

        """ Initialize the base case for the
        first element and non-zero target."""
        if num[0] != 0 and num[0] <= tar:
            prev[num[0]] = 1

        """ Iterate through all elements of the
        array starting from the second element."""
        for ind in range(1, n):
            cur = [0] * (tar + 1)
            for target in range(tar + 1):
                """ Number of ways to achieve the target
                sum without including the current element."""
                not_taken = prev[target]

                """ Number of ways to achieve the target sum
                by including the current element."""
                taken = 0
                if num[ind] <= target:
                    taken = prev[target - num[ind]]

                """ Total ways to achieve the target sum either
                including or excluding the current element."""
                cur[target] = (not_taken + taken) % Solution.mod

            """ Update the previous state to the
            current state for the next iteration."""
            prev = cur

        # Return the number of subsets
        return prev[tar]

    def countPartitions(self, n, diff, arr):
        tot_sum = sum(arr)

        # Checking for edge cases
        if tot_sum - diff < 0 or (tot_sum - diff) % 2:
            return 0

        # Calculate the target sum for one subset.
        return self.findWays(arr, (tot_sum - diff) // 2)
