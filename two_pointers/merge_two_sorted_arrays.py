# Merge Two Sorted Arrays

from typing import List


# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        merged = []

        index_nums1, index_nums2 = 0, 0

        #
        while index_nums1 < m and index_nums2 < n:
            if nums1[index_nums1] < nums2[index_nums2]:
                merged.append(nums1[index_nums1])
                index_nums1 += 1
            else:
                merged.append(nums2[index_nums2])
                index_nums2 += 1
        while index_nums1 < m:
            merged.append(nums1[index_nums1])
            index_nums1 += 1
        while index_nums2 < n:
            merged.append(nums2[index_nums2])
            index_nums2 += 1

        for idx, value in enumerate(merged):
            nums1[idx] = value


# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution2:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        index_nums1, index_nums2 = m - 1, n - 1

        index = m + n - 1

        for index in range(m + n - 1, -1, -1):
            if index_nums2 < 0:
                break
            elif index_nums1 >= 0 and nums1[index_nums1] > nums2[index_nums2]:
                nums1[index] = nums1[index_nums1]
                index_nums1 -= 1
            else:
                nums1[index] = nums2[index_nums2]
                index_nums2 -= 1


# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution3:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        insert_index = m + n - 1
        i, j = m - 1, n - 1

        while insert_index >= 0:
            if i >= 0 and j >= 0:
                if nums1[i] > nums2[j]:
                    nums1[insert_index] = nums1[i]
                    insert_index -= 1
                    i -= 1
                else:
                    nums1[insert_index] = nums2[j]
                    insert_index -= 1
                    j -= 1
            elif i >= 0:
                nums1[insert_index] = nums1[i]
                insert_index -= 1
                i -= 1
            else:
                nums1[insert_index] = nums2[j]
                insert_index -= 1
                j -= 1
