class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Approach:
# 1. Find middle of the linked list using slow and fast pointers.
# 2. Reverse the second half of the linked list.
# 3. Merge the two halves of the linked list alternatively.
# 1 -> 2 -> 3 -> 4 -> 5 -> 6
# 1. Find middle: 4
# 2. Reverse second half: 6 -> 5 -> 4
# 3. Merge: 1 -> 6 -> 2 -> 5 -> 3 -> 4
# Time complexity: O(n) | Space complexity: O(1)
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return

        # find the middle of linked list [Problem 876]
        # in 1->2->3->4->5->6 find 4
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second part of the list [Problem 206]
        # convert 1->2->3->4->5->6 into 1->2->3->4 and 6->5->4
        # reverse the second half in-place
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
            # nextNode = curr.next
            # curr.next = prev
            # prev = curr
            # curr = nextNode

        # merge two sorted linked lists [Problem 21]
        # merge 1->2->3->4 and 6->5->4 into 1->6->2->5->3->4
        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next

            # temp = first.next
            # first.next = second
            # first = temp
            #
            # temp = second.next
            # second.next = first
            # second = temp
