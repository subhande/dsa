# Power (x, n)

# Time Complexoty: O(n) | Space Complexity: O(1)
class Solution1:
    def myPow(self, x, n):
        if n < 0:
            x = 1/x
            n = -1 * n
        if n == 0:
            return 1
        return x * self.myPow(x, n-1)


class Solution2:
    def power(self, x, n):
        # Base case: anything raised to 0 is 1
        if n == 0:
            return 1.0

        # Base case: anything raised to 1 is itself
        if n == 1:
            return x

        # If 'n' is even
        if n % 2 == 0:
            # Recursive call: x * x, n // 2
            return self.power(x * x, n // 2)

        # If 'n' is odd
        # Recursive call: x * power(x, n - 1)
        return x * self.power(x, n - 1)

    def myPow(self, x, n):
        # If 'n' is negative
        if n < 0:
            # Calculate the power of -n and take reciprocal
            return 1.0 / self.power(x, -n)

        # If 'n' is non-negative
        return self.power(x, n)

# Example usage
sol = Solution()
x = 2.0
n = 10

# Calculate x raised to n
result = sol.myPow(x, n)

# Print the result
print(f"{x}^{n} = {result}")
