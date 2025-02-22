# Rotate Array
# https://leetcode.com/problems/rotate-array/description/?envType=company&envId=google&favoriteSlug=google-three-months

class Solution:
    def rotateBruteForce(self, nums: list[int], k: int) -> None:
        # speed up the rotation
        k %= len(nums)

        for i in range(k):
            previous = nums[-1]
            for j in range(len(nums)):
                nums[j], previous = previous, nums[j]


    def rotateExtraSpace(self, nums: list[int], k: int) -> None:
        n = len(nums)
        a = [0] * n

        for i in range(n):
            a[(i + k) % n] = nums[i]

        nums[:] = a

    def rotateReverse(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n

        def reverse(start, end):
            nums[start:end + 1] = nums[start:end + 1][::-1]

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)

    def rotateCyclicReplacements(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n
        count = 0

        for start in range(n):
            current = start
            prev = nums[start]

            print(f"{start}: {nums}")
            while True:
                next = (current + k) % n
                nums[next], prev = prev, nums[next]
                current = next
                count += 1
                print(f"{start}:{count} {nums}")
                if start == current:
                    break

            if count == n:
                break


if __name__ == "__main__":

    sol = Solution()

    # Test 1
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    sol.rotateBruteForce(nums, k)
    assert nums == [5, 6, 7, 1, 2, 3, 4]

    # Test 2
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    sol.rotateExtraSpace(nums, k)
    assert nums == [5, 6, 7, 1, 2, 3, 4]

    # Test 3
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    sol.rotateReverse(nums, k)
    assert nums == [5, 6, 7, 1, 2, 3, 4]

    # Test 4
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    sol.rotateCyclicReplacements(nums, k)
    assert nums == [5, 6, 7, 1, 2, 3, 4]
