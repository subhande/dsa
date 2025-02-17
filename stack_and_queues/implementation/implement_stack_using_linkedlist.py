
class LinkedListNode:
    def __init__(self, x):
        self.val = x
        self.next: LinkedListNode | None = None


class LinkedListStack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, x):
        # 2 <- 1 <- None
        # Push 3
        # 3 <- 2 <- 1 <- None
        # Push 4
        # 4 <- 3 <- 2 <- 1 <- None
        node = LinkedListNode(x)
        node.next = self.head
        self.head = node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            return -1
        temp = self.head
        self.head = self.head.next
        self.size -= 1
        return temp.val


    def top(self):
        if self.isEmpty():
            return -1
        return self.head.val


    def isEmpty(self):
        return self.size == 0



if __name__ == '__main__':
    stack = LinkedListStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.top())
    stack.pop()
    print(stack.top())
    stack.pop()
    print(stack.top())
    stack.pop()
    print(stack.isEmpty())
    stack.push(1)
    print(stack.isEmpty())
    print(stack.top())
    stack.pop()
    print(stack.isEmpty())
    print(stack.top())
    stack.pop()
    print(stack.isEmpty())
    print(stack.top())
