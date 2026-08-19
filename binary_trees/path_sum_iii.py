class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Continuous subarray sum problem, but in a tree. We can use a hash map to store the prefix sums and their counts. As we traverse the tree, we keep track of the current sum and check if there is a prefix sum that, when subtracted from the current sum, equals the target sum. If so, we increment our count by the number of times that prefix sum has occurred.
# Ref: https://leetcode.com/problems/subarray-sum-equals-k/


class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        def preorder(node: TreeNode | None, currSum) -> None:
            nonlocal count

            if not node:
                return

            currSum += node.val

            if currSum == targetSum:
                count += 1

            count += h[currSum - targetSum]

            h[currSum] += 1

            preorder(node.left, currSum)
            preorder(node.right, currSum)

            h[currSum] -= 1

        count, k = 0, sum
        h = defaultdict(int)
        # h[0] = 1
        preorder(root, 0)
        return count


class Solution2:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        def preorder(node: TreeNode | None, currSum) -> None:
            nonlocal count

            if not node:
                return

            currSum += node.val

            count += h[currSum - targetSum]

            h[currSum] += 1

            preorder(node.left, currSum)
            preorder(node.right, currSum)

            h[currSum] -= 1

        count, k = 0, sum
        h = defaultdict(int)
        h[0] = 1
        preorder(root, 0)
        return count
