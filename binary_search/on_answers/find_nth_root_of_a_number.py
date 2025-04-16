# Find Nth root of a number



class Solution:
    def helper(self, mid, n, m):
        '''
        3 * 5

        14 * 3  | 27

        1 * 14 = 14

        '''
        ans, base = 1, mid
        while n > 0:
            if n % 2 == 1:
                ans *= base
                if ans > m:
                    return 2
                n -= 1
            else:
                base *= base
                n //= 2
                if base > m:
                    return 2
        if ans == m:
            return 1
        return 0


    def NthRoot(self, n, m):

        # Binary search for nth root

        left, right = 1, m

        while left <= right:
            mid = (left + right) // 2

            # power = mid ** n
            # if power == m:
            #     return mid
            # elif power < m:
            #     left = mid + 1
            # else:
            #     right = mid - 1
            # we are doing this to avoid overflow

            midN = self.helper(mid=mid, n=n, m=m)

            if midN == 1:
                return mid
            elif midN == 0:
                left = mid + 1
            else:
                right = mid - 1

        return -1


if __name__ == "__main__":
    sol = Solution()

    # Example usage
    n = 3
    m = 27
    result = sol.NthRoot(n, m)
    print(f"The {n}th root of {m} is {result}.")

    n = 4
    m = 16
    result = sol.NthRoot(n, m)
    print(f"The {n}th root of {m} is {result}.")

    n = 4
    m = 27
    result = sol.NthRoot(n, m)
    print(f"The {n}th root of {m} is {result}.")
