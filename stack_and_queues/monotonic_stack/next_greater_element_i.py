# Next Greater Element I

from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping = {}

        stack = []
        result = [-1] * len(nums2)

        for idx in range(len(nums2) - 1, -1, -1):
            while stack and stack[-1] < nums2[idx]:
                stack.pop()
            if stack:
                result[idx] = stack[-1]
            stack.append(nums2[idx])

        for idx in range(len(nums2)):
            mapping[nums2[idx]] = result[idx]

        return [mapping[ele] for ele in nums1]
