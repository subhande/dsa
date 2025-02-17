

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        return f"Node({self.key}, {self.value})"

class DoublyLinkedList:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

    def insertAtHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        node.next = self.head
        self.head.prev = node
        self.head = node

    def removeNode(self, node):
        if node == self.head:
            self.head = node.next
        else:
            node.prev.next = node.next
        if node == self.tail:
            self.tail = node.prev
        else:
            node.next.prev = node.prev
        node.next = None
        node.prev = None

    def moveToHead(self, node):
        self.removeNode(node)
        self.insertAtHead(node)

    def removeTail(self):
        node = self.tail
        self.removeNode(node)
        return node






class LRUCacheUsingDLL:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.dll = DoublyLinkedList(None, None)

    # O(1) time | O(1) space
    def get(self, key_):
        if key_ not in self.cache:
            return -1
        node = self.cache[key_]
        self.dll.moveToHead(node)
        return node.value

    # O(1) time | O(1) space
    def put(self, key_, value):
        if key_ in self.cache:
            node = self.cache[key_]
            node.value = value
            self.dll.moveToHead(node)
        else:
            node = Node(key_, value)
            self.cache[key_] = node
            self.dll.insertAtHead(node)
            self.size += 1
            if self.size > self.capacity:
                tail = self.dll.removeTail()
                print(f"Removing {tail}")
                del self.cache[tail.key]
                self.size -= 1

from collections import OrderedDict

class LRUCacheUsingDict:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        # If key is not present, return -1.
        if key not in self.cache:
            return -1
        # Move the key to the end to denote recent use.
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        # If the key is already in the cache, delete it so that we can re-insert it as most recent.
        if key in self.cache:
            self.cache.pop(key)
        # If the cache exceeds its capacity, remove the least recently used item.
        elif len(self.cache) >= self.capacity:
            # popitem(last=False) pops the first item inserted.
            self.cache.popitem(last=False)
        # Insert the key as the most recently used (end of OrderedDict).
        self.cache[key] = value

if __name__ == '__main__':
    lru = LRUCacheUsingDLL(2)
    lru.put(1, 1)
    lru.put(2, 2)
    print(lru.get(1))
    lru.put(3, 3)
    print(lru.get(2))
    lru.put(4, 4)
    print(lru.get(1))
    print(lru.get(3))
    print(lru.get(4))

    lru = LRUCacheUsingDict(2)
    lru.put(1, 1)
    lru.put(2, 2)
    print(lru.get(1))
    lru.put(3, 3)
    print(lru.get(2))
    lru.put(4, 4)
    print(lru.get(1))
    print(lru.get(3))
    print(lru.get(4))
