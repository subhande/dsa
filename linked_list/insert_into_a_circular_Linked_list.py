from typing import Optional


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


# ============================================================================
# CORE IDEA
# ----------------------------------------------------------------------------
# Walk the list once with two pointers, prev and curr, examining each
# adjacent pair (each "edge" prev -> curr). For every edge ask:
# "does insertVal belong right here?" There are exactly three situations
# where the answer is yes:
#
#   Case A - the normal slot:
#       prev.val <= insertVal <= curr.val
#       The value fits cleanly between two ascending neighbors.
#
#   Case B - the pivot (wrap point): tail -> start, where prev.val > curr.val
#       prev.val > curr.val   (the single edge where max wraps back to min,
#                              e.g. 4 -> 1). Insert here if either:
#         * insertVal >= prev.val  -> new global MAX, goes after old max
#         * insertVal <= curr.val  -> new global MIN, goes before old min
#
#   Case C - full loop, no slot found:
#       Happens when every node has the same value, so neither A nor B ever
#       fires. Detect by checking whether prev has cycled back to head, then
#       insert anywhere (every position is valid when all values are equal).
#
#   NOTE: the `prev is head` guard is the ONLY thing guaranteeing termination.
#         Without it, an all-equal list loops forever.
# ============================================================================


class Solution:
    def insert(self, head: "Optional[Node]", insertVal: int) -> "Node":
        node = Node(insertVal)

        # ---- Empty list: single node points to itself ----
        if head is None:
            node.next = node
            return node

        prev, curr = head, head.next
        while True:
            # ---- Case A: normal ascending slot ----
            if prev.val <= insertVal <= curr.val:
                break
            # ---- Case B: at the max -> min pivot ----
            elif prev.val > curr.val:
                if insertVal >= prev.val or insertVal <= curr.val:
                    break
            # advance to the next edge
            prev, curr = curr, curr.next
            # ---- Case C: came full circle, insert anywhere ----
            if prev is head:
                break

        # splice the new node between prev and curr
        prev.next = node
        node.next = curr
        return head


# ============================================================================
# TRACE  (Example 1:  3 -> 4 -> 1 -> (back to 3),  insertVal = 2)
# ----------------------------------------------------------------------------
# Start: prev = 3, curr = 4
#
#   prev=3, curr=4 :  Case A? 3 <= 2  -> no
#                     Case B? 3 > 4    -> no
#                     advance.            prev is head? no
#
#   prev=4, curr=1 :  Case A? 4 <= 2  -> no
#                     Case B? 4 > 1    -> yes
#                               2 >= 4 -> no
#                               2 <= 1 -> no
#                     advance.            prev is head? no
#
#   prev=1, curr=3 :  Case A? 1 <= 2 <= 3 -> YES  -> break
#
# Splice between 1 and 3:  3 -> 4 -> 1 -> 2 -> (back to 3)
# Return the original node 3.  ✓
# ----------------------------------------------------------------------------
# TRACE  (all-equal edge case:  3 -> 3 -> 3 -> (back to 3),  insertVal = 0)
# ----------------------------------------------------------------------------
#   prev=3, curr=3 :  A? 3<=0 no.  B? 3>3 no.  advance.  prev is head? no
#   prev=3, curr=3 :  A? no.       B? no.      advance.  prev is head? no
#   prev=3, curr=3 :  A? no.       B? no.      advance.  prev is head? YES -> break
#   Insert anywhere: 3 -> 3 -> 3 -> 0 -> (back).  Still sorted. ✓
# ============================================================================
