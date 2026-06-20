from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Empty list -> nothing to process
        if head is None:
            return None

        # Last node in the deduplicated (unique) portion of the list
        lastUniqueNode = head

        # Tracks the previously visited node
        previousNode = head

        # Start checking from the second node
        currentNode = head.next

        while currentNode is not None:
            # If the current value differs from the previous value,
            # we have found a new unique node
            if previousNode.val != currentNode.val:
                # Connect the last unique node to the newly found unique node
                lastUniqueNode.next = currentNode

                # Move the tail of the unique list forward
                lastUniqueNode = currentNode

            # Move to the next node
            previousNode = currentNode
            currentNode = currentNode.next

        # Remove any remaining duplicate nodes that may still be linked
        # after the last unique node
        lastUniqueNode.next = None

        return head
