# Find Square Root of a Number

class Solution:
    def floorSqrt(self, n: int) -> int:
        # Base case
        if n < 2:
            return n

        # Binary search for square root
        left, right = 1, n // 2
        while left <= right:

            mid = (left + right) // 2
            # print(f"left: {left}, right: {right}, mid: {mid} => {mid * mid}")
            square = mid * mid

            if square == n:
                return mid
            elif square < n:
                left = mid + 1
            else:
                right = mid - 1

        return right


if __name__ == "__main__":
    solution = Solution()
    # Example usage
    n = 16
    result = solution.floorSqrt(n)
    print(f"The floor square root of {n} is {result}.")

    n = 8
    result = solution.floorSqrt(n)
    print(f"The floor square root of {n} is {result}.")

    n = 28
    result = solution.floorSqrt(n)
    print(f"The floor square root of {n} is {result}.")
