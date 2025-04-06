# Convert Sorted Array to Binary Search Tree

from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructBST(self, nums, start_idx, end_idx):
        if start_idx > end_idx:
            return None
        if start_idx == end_idx:
            return TreeNode(nums[start_idx])
        mid = (start_idx + end_idx ) // 2
        left = self.constructBST(nums, start_idx, mid-1)
        right = self.constructBST(nums, mid+1, end_idx)
        node = TreeNode(nums[mid], left, right)
        return node
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.constructBST(nums, 0, len(nums)-1)
