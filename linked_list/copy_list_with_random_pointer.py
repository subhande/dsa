from typing import Optional


class Node:
    def __init__(
        self, x: int, next: Optional["Node"] = None, random: Optional["Node"] = None
    ):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":

        nodeMap = {}

        sentinel = Node(0)

        current = sentinel

        randomHead = head

        while head:
            node = Node(head.val, head.next)
            nodeMap[id(head)] = node
            current.next = node
            current = current.next
            head = head.next

        while randomHead:
            if randomHead.random:
                node = nodeMap[id(randomHead)]
                node.random = nodeMap[id(randomHead.random)]
            randomHead = randomHead.next

        return sentinel.next

    def copyRandomListRecursive(self, head: "Optional[Node]") -> "Optional[Node]":

        visitedHash = {}

        def copyNode(node):
            if node is None:
                return None

            if node in visitedHash:
                return visitedHash[node]

            newNode = Node(node.val)
            visitedHash[node] = newNode
            newNode.next = copyNode(node.next)
            newNode.random = copyNode(node.random)

            return newNode

        return copyNode(head)


class Solution2:
    def __init__(self):
        # Creating a visited dictionary to hold old node reference as "key" and new node reference as the "value"
        self.visited = {}

    def getClonedNode(self, node):
        # If node exists then
        if node:
            # Check if its in the visited dictionary
            if node in self.visited:
                # If its in the visited dictionary then return the new node reference from the dictionary
                return self.visited[node]
            else:
                # Otherwise create a new node, save the reference in the visited dictionary and return it.
                self.visited[node] = Node(node.val, None, None)
                return self.visited[node]
        return None

    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":

        if not head:
            return head

        old_node = head
        # Creating the new head node.
        new_node = Node(old_node.val, None, None)
        self.visited[old_node] = new_node

        # Iterate on the linked list until all nodes are cloned.
        while old_node != None:
            # Get the clones of the nodes referenced by random and next pointers.
            new_node.random = self.getClonedNode(old_node.random)
            new_node.next = self.getClonedNode(old_node.next)

            # Move one step ahead in the linked list.
            old_node = old_node.next
            new_node = new_node.next

        return self.visited[head]
