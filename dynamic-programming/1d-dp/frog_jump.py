# Frog Jump (Jump Game Variation)
# https://takeuforward.org/plus/dsa/dynamic-programming/1d-dp/frog-jump

class Solution:
    def frogJump(self, heights):
        total_steps = len(heights)
        if total_steps == 0 or total_steps == 1:
            return 0
        if total_steps == 2:
            return abs(heights[0]-heights[1])
        one_step_back = abs(heights[0]-heights[1])
        two_step_back = 0

        for i in range(2, total_steps):
            current_energy = min(
                one_step_back + abs(heights[i]-heights[i-1]),
                two_step_back + abs(heights[i]-heights[i-2])
            )
            two_step_back = one_step_back
            one_step_back = current_energy
        return one_step_back

# Time: O(n) | Space: O(n)
class Solution2:
    def solve(self, ind, heights, dp):
        if ind == 0:
            # Base case
            return 0
        if dp[ind] != -1:
            # Memoized result
            return dp[ind]

        jumpOne = self.solve(ind - 1, heights, dp) + abs(heights[ind] - heights[ind - 1])
        jumpTwo = float('inf')
        if ind > 1:
            jumpTwo = self.solve(ind - 2, heights, dp) + abs(heights[ind] - heights[ind - 2])
        # Store and return result
        dp[ind] = min(jumpOne, jumpTwo)
        return dp[ind]

    def frogJump(self, heights):
        n = len(heights)
        dp = [-1] * n
        # Start solving from the last stair
        return self.solve(n - 1, heights, dp)
