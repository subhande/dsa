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
        # -2147483648 / -1 = 2147483648 which is greater than 2**31 - 1
        # => 2147483647, so we need to return 2**31 - 1 in this case
        if quotient > 2**31 - 1 and isPositive:
            return 2**31 - 1
        # -2147483648 / 1 = -2147483648 which is less than -2**31
        # => -2147483648, which is valid, so we can return -2147483648 in this case
        # Commenting below condition as it is not needed, we can return -2147483648 in this case as it is valid
        # elif quotient > 2**31 - 1 and not isPositive:
        #     return -2**31
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
            # 22 % 6
            # divisor << 1 = 6 * (1 << 1) = 12
            # divisor << 1 = 6 * (1 << 1) = 12
            # Max = 6 * (1 << 1) = 12, count = 1
            while dividend >= (divisor << (count+1)):
                count += 1

            # Updating the answer & dividend
            # 1 << 1 = 2, ans = 2, dividend = 22 - 12 = 10
            # dividend = dividend - divisor * (1 << count)
            # = 22 - 3 * 2 = 22 - 12 = 10
            ans += (1 << count)
            dividend -= divisor << count # divisor * (1 << count)


        # Overflow condition
        # -2147483648 / -1 = 2147483648 which is greater than 2**31 - 1
        # => 2147483647, so we need to return 2**31 - 1 in this case
        if ans > 2**31 - 1 and isPositive:
            return 2**31 - 1
        # -2147483648 / 1 = -2147483648 which is less than -2**31
        # => -2147483648, which is valid, so we can return -2147483648 in this case
        # Commenting below condition as it is not needed, we can return -2147483648 in this case as it is valid
        # elif ans > 2**31 - 1 and not isPositive:
        #     return -2**31

        # Returning the quotient
        # with proper sign
        return ans if isPositive else -1 * ans
