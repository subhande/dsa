# Find Duplicate Subtree
# https://www.youtube.com/watch?v=kn0Z5_qPPzY

from collections import defaultdict
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Solution 1: Using serialization of subtrees | Brute Force Approach
# Time Complexity: O(n^2) - for each node we build a serialized string of its
#   subtree (O(n) work in the worst case), and we do this for all n nodes.
# Space Complexity: O(n^2) - the dictionary can end up storing O(n) serialized
#   strings, each of length up to O(n).
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        # Maps a subtree's serialized string representation -> list of nodes
        # that produced that exact serialization.
        subtrees = defaultdict(list)

        def dfs(node):
            # Use a sentinel ("N") to represent empty children so that
            # different tree shapes don't produce ambiguous serializations.
            if node is None:
                return "N"

            # Serialize the subtree rooted at `node` as "val left right",
            # built bottom-up so that identical subtrees always produce
            # identical strings.
            s = " ".join([str(node.val), dfs(node.left), dfs(node.right)])

            # The first time we see a second occurrence of this serialization,
            # record the node as the representative duplicate.
            if len(subtrees[s]) == 1:
                res.append(node)
            subtrees[s].append(node)
            return s

        res = []
        dfs(root)
        return res


# Solution 2: Using unique identifiers for subtrees | Optimized Approach
# Instead of comparing full serialized strings, assign each distinct subtree
# shape/value combination a small integer id, so comparisons become O(1)
# tuple/dict lookups instead of O(n) string comparisons.
# Time Complexity: O(n) - each node is visited once and does O(1) work.
# Space Complexity: O(n) - `ids` and `count` each hold at most one entry per
#   distinct subtree, bounded by the number of nodes.
class Solution2:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        ids = {}  # (val, left_id, right_id) -> int, assigns a unique id per distinct subtree
        count = defaultdict(int)  # subtree id -> number of times it has been seen
        res = []

        def dfs(node):
            # Empty subtrees all share the id -1.
            if node is None:
                return -1

            # Build a key from the node's value and its children's ids.
            # Two subtrees are identical iff they produce the same key.
            key = (node.val, dfs(node.left), dfs(node.right))

            # Assign a new unique id the first time this key is encountered.
            if key not in ids:
                ids[key] = len(ids)

            sid = ids[key]
            count[sid] += 1

            # Add the node to the result exactly once, the moment its
            # subtree is seen for the second time.
            if count[sid] == 2:
                res.append(node)
            return sid

        dfs(root)
        return res
