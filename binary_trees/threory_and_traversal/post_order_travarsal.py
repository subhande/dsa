
"""
# Post Order Traversal
"""

class TreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.value)

class Solution:
    def postOrderRecursive(self, root: TreeNode | None):
        if root is None:
            return []
        return self.postOrderRecursive(root.left) + self.postOrderRecursive(root.right) + [root.value]

    def postOrderIterative(self, root: TreeNode | None):
        stack = []
        result = []
        if root is None:
            return result

        current = root
        prev = None

        while current is not None or stack:
            while current is not None:
                # Push the current node to the stack
                stack.append(current)
                # Move to the left child
                current = current.left
            # Set current to the top of the stack
            current = stack[-1]
            # If the right child is None or already visited
            if current.right is None or current.right == prev:
                # Append the current node to the result
                result.append(current.value)
                # Pop the current node from the stack
                stack.pop()
                # Set prev to the current node
                prev = current
                # Set current to None
                current = None
            else:
                # Move to the right child
                current = current.right
        return result

"""
Let's break down the iterative post order traversal method in simple terms. In post order traversal, you visit a node’s left subtree, then its right subtree, and finally the node itself. The recursive solution is straightforward, but doing it iteratively is a bit trickier because you have to simulate the “returning back” from the recursive calls. This solution uses a stack and a helper pointer (named “prev”) to keep track of the last node that was processed.

Imagine you have a binary tree like this:

         1
       /   \
      2     3
     / \   / \
    4   5 6   7

The goal is to produce the output in post order: [4, 5, 2, 6, 7, 3, 1].

Here’s a step-by-step explanation of how the iterative function works:

1. Initialization:
   • Create an empty stack to simulate the recursion.
   • Create an empty list called “result” to store the final traversal.
   • Set “current” to the root (node 1) and “prev” to None. The “prev” pointer will remember the last node we finished processing.

2. Traverse the tree until there’s no current node and the stack is empty:
   • First, go as far left as possible:
     – Push the current node onto the stack.
     – Move “current” to its left child.
   • Continue doing this until “current” becomes None.

3. Process the node at the top of the stack:
   • When you can’t go left anymore, look at the node on the top of the stack (don’t pop it yet).
   • Check if this node has a right child that has not yet been processed.
     – If there is a right child and it hasn’t been processed, move “current” to the right child.
     – If there is no right child or the right child was just processed (i.e., “prev” equals that right child), then it means both the left and right subtrees for this node are done. Now you can add this node’s value to the “result” list.
     – Pop the node from the stack, mark it as “prev” (the last processed node), and set “current” to None so that the next iteration will check the stack again.

4. Repeat this until both the stack is empty and “current” is None.

Let’s walk through our tree example:

A. Start at root (1):
   - current = 1, stack = []
   - Push 1 to stack, then set current to left child (node 2).
     Stack: [1]

B. Now at node 2:
   - current = 2, stack = [1]
   - Push 2 to stack, then set current to left child (node 4).
     Stack: [1, 2]

C. At node 4:
   - current = 4, stack = [1, 2]
   - Push 4 to stack, then set current to left child. Node 4 has no left child, so current becomes None.
     Stack: [1, 2, 4]

D. With current = None:
   - Look at the node on top of the stack: node 4.
   - Node 4 has no right child, so it’s time to process it.
   - Append 4 to “result”, pop it from the stack, set prev = 4.
     Result: [4]
     Stack: [1, 2]

E. Back to the loop:
   - Now, current is None, so check the top of the stack (node 2).
   - For node 2, the right child is node 5, and since prev is not node 5 (it’s node 4), we haven’t processed node 2’s right subtree yet.
   - Set current to node 5.
     Stack remains: [1, 2]

F. At node 5:
   - current = 5, stack = [1, 2]
   - Push node 5 onto stack, move to its left child. Node 5 has no left child, so current becomes None.
     Stack: [1, 2, 5]

G. With current = None:
   - Look at the top of the stack: node 5.
   - Node 5 has no right child, so process it.
   - Append 5 to “result”, pop it from the stack, set prev = 5.
     Result: [4, 5]
     Stack: [1, 2]

H. Return to the top of the stack:
   - The top is node 2. Its right child is node 5 which is already processed (prev == 5). So, process node 2.
   - Append 2 to “result”, pop it, set prev = 2.
     Result: [4, 5, 2]
     Stack: [1]

I. Now back to node 1:
   - Top of the stack is node 1.
   - Node 1’s right child is node 3, and prev is not node 3 (prev is node 2), so move to the right child.
   - Set current = 3.
     Stack remains: [1]

J. At node 3:
   - current = 3, stack = [1]
   - Push node 3 onto stack and move to its left child (node 6).
     Stack: [1, 3]

K. At node 6:
   - current = 6, stack = [1, 3]
   - Push node 6 onto stack and move to its left child. Node 6 doesn’t have a left child, so current becomes None.
     Stack: [1, 3, 6]

L. With current = None:
   - Look at the top of the stack: node 6.
   - Node 6 has no right child, so process it.
   - Append 6 to “result”, pop it, set prev = 6.
     Result: [4, 5, 2, 6]
     Stack: [1, 3]

M. Now, examine node 3 (top of the stack):
   - For node 3, the right child is node 7, which hasn't been processed.
   - Set current = 7.
     Stack remains: [1, 3]

N. At node 7:
   - current = 7, stack = [1, 3]
   - Push node 7 onto stack and move to its left child. Node 7 has no left child, so current becomes None.
     Stack: [1, 3, 7]

O. With current = None:
   - Look at the top: node 7. It has no right child, so process it.
   - Append 7 to “result”, pop it, set prev = 7.
     Result: [4, 5, 2, 6, 7]
     Stack: [1, 3]

P. Back to node 3:
   - Now, node 3’s right child (7) is already processed (prev equals 7), so process node 3.
   - Append 3 to “result”, pop it, set prev = 3.
     Result: [4, 5, 2, 6, 7, 3]
     Stack: [1]

Q. Finally, return to node 1:
   - Node 1’s right child (3) is processed (prev equals 3), so process node 1.
   - Append 1 to “result”, pop it, set prev = 1.
     Result: [4, 5, 2, 6, 7, 3, 1]
     Stack: []

5. The loop stops when both the stack is empty and there is no current node. The final “result” list contains the post order traversal.

Summary of Key Points:
• A stack helps keep track of nodes we’re working on.
• We use a “prev” pointer to check whether we have just finished visiting a node’s right subtree.
• The algorithm can always decide whether to process the node or move right based on whether the right child exists and if it has been processed.
• For our example tree, the nodes are added in the order: 4, then 5, then 2, then 6, then 7, then 3, and finally 1.

That’s the iterative post order traversal explained using a stack, “current,” and “prev” pointers with a full example walkthrough.
"""

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    s = Solution()
    print("===== Recursive =====")
    print(s.postOrderRecursive(root))
    print("===== Iterative =====")
    print(s.postOrderIterative(root))
