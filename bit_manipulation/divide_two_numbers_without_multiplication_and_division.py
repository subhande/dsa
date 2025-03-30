# Divide Two Numbers without using Multiplication and Division operators

# Brute Force
# Time Complexity: O(dividend) | Space Complexity: O(1)
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == divisor:
            return 1
        isPositive = not ((dividend >= 0 and divisor < 0) or (dividend < 0 and divisor > 0))

        dividend = abs(dividend)
        divisor = abs(divisor)

        if dividend < divisor:
            return 0

        quotient = 0
        while dividend >= divisor:
            dividend -= divisor
            quotient += 1

        # Overflow condition
        if quotient > 2**31 - 1 and isPositive:
            return 2**31 - 1
        elif quotient > 2**31 and not isPositive:
            return -2**31
        return quotient if isPositive else -quotient

# Optimal Approach
# Time Complexity: O((log(dividend))^2) | Space Complexity: O(1)
# Outer loop runs log(dividend) times and inner loop runs log(divisor) times
class Solution2:
    def divide(self, dividend: int, divisor: int) -> int:

        # Base case
        if dividend == divisor:
            return 1
        isPositive = not ((dividend >= 0 and divisor < 0) or (dividend < 0 and divisor > 0))

        dividend = abs(dividend)
        divisor = abs(divisor)

        if dividend < divisor:
            return 0

        ans = 0

        # Looping while dividend is
        # greater than equal to divisor
        while dividend >= divisor:
            count = 0

            # Finding the required
            # largest power of 2
            while dividend >= (divisor << (count+1)):
                count += 1

            # Updating the answer & dividend
            ans += (1 << count)
            dividend -= divisor << count # divisor * (1 << count)


        # Handling overflowing condition
        if ans > 2**31 - 1 and isPositive:
            return 2**31 - 1
        if ans > 2**31 - 1 and not isPositive:
            return -2**31

        # Returning the quotient
        # with proper sign
        return ans if isPositive else -1 * ans
