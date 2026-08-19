# Longest Univalue Path
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time Complexity: O(n) | Space Complexity: O(h) where h is the height of the tree


class Solution:
    def longestUnivaluePathHelper(
        self, node: TreeNode | None, maxPathSameValue: list[int]
    ) -> tuple:
        if node is None:
            return (None, -1)
        if node.left is None and node.right is None:
            maxPathSameValue[0] = max(maxPathSameValue[0], 1)
            return (node.val, 1)
        leftValue, leftSameValuePathLength = self.longestUnivaluePathHelper(
            node.left, maxPathSameValue
        )
        rightValue, rightSameValuePathLength = self.longestUnivaluePathHelper(
            node.right, maxPathSameValue
        )

        if (
            leftValue is not None
            and rightValue is not None
            and leftValue == rightValue == node.val
        ):
            maxPathSameValue[0] = max(
                maxPathSameValue[0],
                1 + leftSameValuePathLength + rightSameValuePathLength,
            )
            return node.val, max(leftSameValuePathLength, rightSameValuePathLength) + 1
        elif leftValue is not None and leftValue == node.val:
            maxPathSameValue[0] = max(maxPathSameValue[0], 1 + leftSameValuePathLength)
            return node.val, leftSameValuePathLength + 1
        elif rightValue is not None and rightValue == node.val:
            maxPathSameValue[0] = max(maxPathSameValue[0], 1 + rightSameValuePathLength)
            return node.val, rightSameValuePathLength + 1
        else:
            maxPathSameValue[0] = max(maxPathSameValue[0], 1)
            return node.val, 1

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        maxPathSameValue = [0]
        self.longestUnivaluePathHelper(root, maxPathSameValue)
        return maxPathSameValue[0] - 1


class Solution2:
    def longestUnivaluePath(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        longest = [0]  # longest univalue path seen anywhere, measured in NODES
        self._longestDownwardChain(root, longest)
        return longest[0] - 1  # convert node count to edge count

    def _longestDownwardChain(self, node: TreeNode | None, longest: list[int]) -> tuple:
        """
        Returns (node.val, chainLength) where chainLength is the number of nodes
        in the longest straight-downward run of node.val that STARTS at node.

        Two distinct quantities are computed here, and mixing them up is the
        classic bug in this problem:
          - what we RECORD into longest[]: the path may bend through node,
            so it can use both children's chains at once.
          - what we RETURN to the parent: the parent can only extend through
            ONE child, so we hand up the longer arm only.
        """
        if node is None:
            return (None, -1)  # sentinel; never read, every use is guarded below

        if node.left is None and node.right is None:
            longest[0] = max(longest[0], 1)
            return (node.val, 1)

        leftVal, leftChain = self._longestDownwardChain(node.left, longest)
        rightVal, rightChain = self._longestDownwardChain(node.right, longest)

        matchesLeft = leftVal is not None and leftVal == node.val
        matchesRight = rightVal is not None and rightVal == node.val

        if matchesLeft and matchesRight:
            # Path can bend: left arm + node + right arm.
            longest[0] = max(longest[0], 1 + leftChain + rightChain)
            # But only one arm can continue upward — take the longer.
            return (node.val, max(leftChain, rightChain) + 1)

        if matchesLeft:
            longest[0] = max(longest[0], 1 + leftChain)
            return (node.val, leftChain + 1)

        if matchesRight:
            longest[0] = max(longest[0], 1 + rightChain)
            return (node.val, rightChain + 1)

        # Neither child matches: node is a chain of length 1 on its own.
        longest[0] = max(longest[0], 1)
        return (node.val, 1)


class Solution3:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.ans = 0

        def dfs(node):
            if not node:
                return 0

            left_len = dfs(node.left)
            right_len = dfs(node.right)

            # Only extend the arm if child exists and matches value
            left_arm = left_len + 1 if node.left and node.left.val == node.val else 0
            right_arm = (
                right_len + 1 if node.right and node.right.val == node.val else 0
            )

            # Path through this node connects both arms
            self.ans = max(self.ans, left_arm + right_arm)

            # Return the longer single arm upward
            return max(left_arm, right_arm)

        dfs(root)
        return self.ans
