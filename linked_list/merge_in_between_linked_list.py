# Merge In Between Linked Lists
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(
        self, list1: ListNode, a: int, b: int, list2: ListNode
    ) -> ListNode:

        tail = list2

        while tail.next:
            tail = tail.next

        list1_part1_tail = None
        list1_part2_head = None

        prev = None
        curr = list1
        count = 0
        while curr:
            if count == a:
                list1_part1_tail = prev
            if count == b:
                list1_part2_head = curr.next
            count += 1
            prev, curr = curr, curr.next

        if list1_part1_tail:
            list1_part1_tail.next = list2
            tail.next = list1_part2_head
        else:
            head = list2
            tail = list1_part2_head
        return list1
