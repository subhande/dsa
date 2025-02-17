# LFU Cache

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        return f"Node({self.key}, {self.value})"

class DoublyLinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def insertAtHead(self, node):
        # Insert the node at the head of the DLL.
        if self.head is None:
            self.head = node
            self.tail = node
            return
        node.next = self.head
        self.head.prev = node
        self.head = node

    def removeNode(self, node):
        # Remove a node from the DLL.
        # (We add safety checks in case the node is the only one in the list.)
        if self.head is None:
            return
        # If node is at head.
        if node == self.head:
            self.head = node.next
            if self.head:
                self.head.prev = None
        else:
            node.prev.next = node.next

        # If node is at tail.
        if node == self.tail:
            self.tail = node.prev
            if self.tail:
                self.tail.next = None
        else:
            # node.next is guaranteed not None here
            node.next.prev = node.prev

        node.next = None
        node.prev = None

    def moveToHead(self, node):
        # Remove and reinsert at head.
        self.removeNode(node)
        self.insertAtHead(node)

    def removeTail(self):
        # Remove tail node and return it.
        if self.tail is None:
            return None
        tail_node = self.tail
        self.removeNode(tail_node)
        return tail_node

# LFU Cache using Doubly Linked Lists for nodes with equal frequency.
# We maintain:
#  • key_table: mapping key -> (node, freq)
#  • freq_table: mapping frequency -> DoublyLinkedList of nodes (most recently used at head)
#  • min_freq: the current minimum frequency among keys.
class LFUCacheUsingDLL:
    def __init__(self, capacity):
        self.capacity = capacity
        self.min_freq = 0
        self.key_table = {}   # key -> (node, frequency)
        self.freq_table = {}  # freq -> DoublyLinkedList

    # O(1) time | O(1) space
    def get(self, key_):
        if key_ not in self.key_table:
            return -1  # key not found

        node, freq = self.key_table[key_]

        # Remove the node from its current frequency list.
        dll = self.freq_table[freq]
        dll.removeNode(node)
        # If the list becomes empty, remove it from freq_table and update min_freq if needed.
        if dll.head is None:
            del self.freq_table[freq]
            if self.min_freq == freq:
                self.min_freq += 1

        # Increase the frequency of the node.
        new_freq = freq + 1
        if new_freq not in self.freq_table:
            self.freq_table[new_freq] = DoublyLinkedList()
        self.freq_table[new_freq].insertAtHead(node)
        self.key_table[key_] = (node, new_freq)

        return node.value

    # O(1) time | O(1) space
    def put(self, key_, value):
        if self.capacity <= 0:
            return

        # If key already exists, update the value and frequency.
        if key_ in self.key_table:
            node, freq = self.key_table[key_]
            node.value = value   # update the value
            # Calling get(key_) will update the node's frequency.
            self.get(key_)
            return

        # If cache is full, evict the least frequently used key.
        if len(self.key_table) >= self.capacity:
            # The key to remove is found in the DLL corresponding to min_freq.
            dll = self.freq_table[self.min_freq]
            node_to_remove = dll.removeTail()
            del self.key_table[node_to_remove.key]
            if dll.head is None:
                del self.freq_table[self.min_freq]

        # Insert the new node.
        new_node = Node(key_, value)
        # New insertion always has frequency 1.
        if 1 not in self.freq_table:
            self.freq_table[1] = DoublyLinkedList()
        self.freq_table[1].insertAtHead(new_node)
        self.key_table[key_] = (new_node, 1)
        self.min_freq = 1  # reset min_freq

from collections import defaultdict, OrderedDict

class LFUCacheUsingDict:
    def __init__(self, capacity: int):
        """
        Initialize LFU Cache.
        :param capacity: Maximum number of items in the cache.
        """
        self.capacity = capacity
        self.key_to_node = {}  # key: (value, freq)
        self.freq_to_keys = defaultdict(OrderedDict)  # freq: OrderedDict of keys preserving recency order.
        self.min_freq = 0

    def _update_freq(self, key: int):
        """
        Helper function to update the frequency of the given key.
        Moves the key from the old frequency list to the new frequency list.
        """
        value, freq = self.key_to_node[key]
        # Remove key from the old frequency's OrderedDict.
        del self.freq_to_keys[freq][key]
        # If the current frequency list is now empty, remove it.
        if not self.freq_to_keys[freq]:
            del self.freq_to_keys[freq]
            # Update min_freq if needed.
            if freq == self.min_freq:
                self.min_freq += 1

        # Increase frequency.
        new_freq = freq + 1
        self.key_to_node[key] = (value, new_freq)
        # Add key to the new frequency list. The order in the OrderedDict represents recency.
        self.freq_to_keys[new_freq][key] = None

    def get(self, key: int) -> int:
        """
        Retrieve the value of the key if present, otherwise return -1.
        Also updates the frequency of the accessed key.
        """
        if key not in self.key_to_node:
            return -1

        # Update key's frequency since it has been accessed.
        self._update_freq(key)
        return self.key_to_node[key][0]

    def put(self, key: int, value: int) -> None:
        """
        Insert or update the value of the key. If the cache reaches its capacity,
        it evicts the least frequently used item. If there is a tie, the least
        recently used one gets evicted.
        """
        if self.capacity <= 0:
            return

        # If key is already in the cache, update its value and frequency.
        if key in self.key_to_node:
            # Update the value.
            self.key_to_node[key] = (value, self.key_to_node[key][1])
            # Update frequency using the helper method.
            self._update_freq(key)
            return

        # If cache is full, we need to evict the LFU key.
        if len(self.key_to_node) >= self.capacity:
            # The LFU key is the least recently used one in freq_to_keys[min_freq]
            evict_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
            # Remove the evicted key from the key_to_node dict.
            del self.key_to_node[evict_key]
            # Remove the frequency dictionary if it's become empty.
            if not self.freq_to_keys[self.min_freq]:
                del self.freq_to_keys[self.min_freq]

        # Insert the new key with frequency 1.
        self.key_to_node[key] = (value, 1)
        self.freq_to_keys[1][key] = None
        self.min_freq = 1  # Reset min_freq to 1 for the new key

if __name__ == '__main__':
    LFU = LFUCacheUsingDLL(2)
    LFU.put(1, 1)
    LFU.put(2, 2)
    print(LFU.get(1))
    LFU.put(3, 3)
    print(LFU.get(2))
    LFU.put(4, 4)
    print(LFU.get(1))
    print(LFU.get(3))
    print(LFU.get(4))

    LFU = LFUCacheUsingDict(2)
    LFU.put(1, 1)
    LFU.put(2, 2)
    print(LFU.get(1))
    LFU.put(3, 3)
    print(LFU.get(2))
    LFU.put(4, 4)
    print(LFU.get(1))
    print(LFU.get(3))
    print(LFU.get(4))
