# Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/
# https://takeuforward.org/plus/dsa/dynamic-programming/1d-dp/climbing-stairs

# Solution 1: Recursion

class Solution:
    # Function to count total ways to reach nth stair
    def climbStairs(self, n):
        # Base case
        if n == 0:
            return 1
        if n == 1:
            return 1

        # Taking 1 step at a time
        oneStep = self.climbStairs(n-1)

        # Taking 2 steps at a time
        twoSteps = self.climbStairs(n-2)

        # Return total ways
        return oneStep + twoSteps

# Solution 2: Recursion with Memoization

class Solution2:
    #Helper function to apply memoization
    def func(self, n, dp):
        # Base condition
        if n <= 1:
            return 1

        # Check if the subproblem is already solved
        if dp[n] != -1:
            return dp[n]

        # Return the calculated value
        dp[n] = self.func(n-1, dp) + self.func(n-2, dp)
        return dp[n]

    # Function to count total ways to reach nth stair
    def climbStairs(self, n):
        # Initialize dp array with -1
        dp = [-1] * (n + 1)

        return self.func(n, dp)



# Solution 3: Tabulation

class Solution3:
    # Function to count total ways to reach the nth stair
    def climbStairs(self, n):
        # Declare dp array of size n+1 and initialize with -1
        dp = [-1] * (n + 1)

        # Insert the values of base conditions
        dp[0] = 1
        dp[1] = 1

        # Iterate and update every index of dp array
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        # Return the answer
        return dp[n]

# Solution 4: Tabulation with Optimized Space Complexity

class Solution4:
    # Function to count total ways to reach nth stair
    def climbStairs(self, n):
        """Initialize two variables to
        store previous results"""
        prev2 = 1
        prev = 1

        #Iterate and update the variables
        for i in range(2, n+1):
            curr = prev2 + prev
            prev2 = prev
            prev = curr

        #Return the answer as prev
        return prev
