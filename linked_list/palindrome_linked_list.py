from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Approach 1: Using an Array
# Time Complexity: O(n) | Space Complexity: O(n)
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []

        while head:
            arr.append(head.val)
            head = head.next

        return arr == arr[::-1]


# Approach 2: Using a Stack
# Time Complexity: O(n) | Space Complexity: O(n)
class Solution2:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        slow = fast = head

        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        if fast:
            slow = slow.next

        while slow:
            if stack.pop() != slow.val:
                return False
            slow = slow.next

        return True


# Approach 3: Using Recursion
# Time Complexity: O(n) | Space Complexity: O(n)
class Solution3:
    def isPalindrome(self, head: ListNode) -> bool:
        self.front_pointer = head

        def recursively_check(current_node=head):
            if current_node is not None:
                if not recursively_check(current_node.next):
                    return False
                if self.front_pointer.val != current_node.val:
                    return False
                self.front_pointer = self.front_pointer.next
            return True

        return recursively_check()


# Approach 4: Reverse the Second Half of the List
# Time Complexity: O(n) | Space Complexity: O(1)
class Solution4:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True

        # Find the end of first half and reverse second half.
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)

        # Check whether or not there's a palindrome.
        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position is not None:
            if first_position.val != second_position.val:
                result = False
            first_position = first_position.next
            second_position = second_position.next

        # Restore the list and return the result.
        first_half_end.next = self.reverse_list(second_half_start)
        return result

    def end_of_first_half(self, head: ListNode) -> ListNode:
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_list(self, head: ListNode) -> ListNode:
        previous = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous
