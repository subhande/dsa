# Reverse Nodes in k-Group
# This is extension of the reverse linked list problem. We will reverse the nodes in k groups instead of reversing the entire list or from left to right
# Time Complexity: O(n) | Space Complexity: O(1)
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Compute the total length of the list
        list_length = 1
        node = head
        while node.next:
            list_length += 1
            node = node.next

        # Nothing to reverse if the list is shorter than k, or k is trivial
        if list_length < k or k == 1:
            return head

        prev_node = None
        curr_node = head

        # `group_tail` tracks the tail of the current k-group being reversed.
        # After reversal it becomes the tail, and its `.next` must point to the
        # start of the next group (or the remainder).
        # `connector` is the tail of the *already-reversed* segment; its `.next`
        # will be updated to the new group head once reversal is done.
        group_tail = curr_node  # first node of the current group = future tail
        connector = prev_node  # last node of the previously reversed segment

        nodes_processed = 1

        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node  # reverse the pointer
            prev_node = curr_node
            curr_node = next_node

            if nodes_processed % k == 0:
                # `prev_node` is now the new head of the just-reversed group.
                # Stitch it onto the previous segment (or make it the list head).
                if connector:
                    connector.next = prev_node
                else:
                    head = prev_node

                # Point the group tail to whatever comes next
                group_tail.next = curr_node

                # Stop early if the remaining nodes are fewer than k
                # (leave them as-is, per the problem spec)
                if list_length - nodes_processed < k:
                    break

                # Advance connector and group_tail for the next group
                connector = group_tail
                group_tail = curr_node

            nodes_processed += 1

        return head


# RAW Solution
class Solution2:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        size = 1
        node = head
        while node.next:
            size += 1
            node = node.next

        if size < k or k == 1:
            return head
        remaining = size

        prev, curr = None, head

        tail, con = curr, prev

        idx = 1

        while curr:
            third = curr.next
            curr.next = prev
            prev = curr
            curr = third

            if idx % k == 0:
                if con:
                    con.next = prev
                else:
                    head = prev
                tail.next = curr

                if size - idx < k:
                    break

                tail, con = curr, tail

            idx += 1

        return head
