
# Implement a queue using linked list


class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedListQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, x):
        # 1 -> 2 -> 3 -> None
        # Push 4
        # 1 -> 2 -> 3 -> 4 -> None
        node = Node(x)
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1


    def pop(self):
        if self.isEmpty():
            return -1
        temp = self.head
        self.head = self.head.next
        self.size -= 1
        return temp.val


    def peek(self):
        if self.isEmpty():
            return -1
        return self.head.val


    def isEmpty(self):
        return self.size == 0



if __name__ == '__main__':
    queue = LinkedListQueue()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    print(queue.peek())
    queue.pop()
    print(queue.peek())
    queue.pop()
    print(queue.peek())
    queue.pop()
    print(queue.isEmpty())
    queue.push(1)
    print(queue.isEmpty())
    print(queue.peek())
    queue.pop()
    print(queue.isEmpty())
    print(queue.peek())
    queue.pop()
    print(queue.isEmpty())
    print(queue.peek())
