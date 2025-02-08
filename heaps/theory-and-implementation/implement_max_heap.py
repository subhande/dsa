"""
# Implement Max Heap

You need to implement the Min Heap with the following given methods.
insert (x) -> insert value x to the max heap
getMax -> Output the maximum value from min heap
exctractMax -> Remove the maximum element from the heap
heapSize -> return the current size of the heap
isEmpty -> returns if heap is empty or not
changeKey (ind, val) -> update the value at given index to val (index will be given 0-based indexing)
initializeHeap -> Initialize the heap

---------------------------------------
Examples:
---------------------------------------
Input : operation = [ "initializeHeap", "insert", "insert", "insert", "getMax", "heapSize", "isEmpty", "exctractMax", "changeKey" , "getMax" ]
nums = [ [4], [1], [10], [0, 16] ]
Output : [ null, null, null, null, 10, 3, 0, null, null, 16 ]

Explanation : In 1st operation we initialize the heap to empty heap.
In 2nd, 3rd, 4th operation we insert 4, 1, 10 to the heap respectively. The heap after 4th operation will be -> [10, 4, 1].
In 5th operation we output the maximum element from the heap i.e. 10.
In 6th operation we output the size of the current heap i.e. 3.
In 7th operation we output whether the heap is empty or not i.e. false (0).
In 8th operation we remove the maximum element from heap. So the ne heap becomes -> [4, 1].
In 9th operation we change the 0th index element to 16. So new heap becomes -> [16, 1]. After heapify -> [16, 1].
In 10th operation we output the minimum element of the heap i.e. 16.
---------------------------------------
Input : operation = [ "initializeHeap", "insert", "insert", "exctractMax", "getMax", "insert", "heapSize", "isEmpty", "exctractMax", "changeKey" , "getMax" ]
nums = [ [4], [1], [4], [0, 2] ]
Output : [ null, null, null, null, 1, null, 2, 0, null, null, 2 ]

Explanation : In 1st operation we initialize the heap to empty heap.
In 2nd, 3rd operation we insert 4, 1 to the heap respectively. The heap after 4th operation will be -> [4, 1].
In 4th operation we remove the maximum element from heap. So the ne heap becomes -> [1].
In 5th operation we output the maximum element of the heap i.e. 1.
In 6th operation we operation we insert 4 to the heap. The heap after 6th operation will be -> [4, 1].
In 7th operation we output the size of the current heap i.e. 2.
In 8th operation we output whether the heap is empty or not i.e. false (0).
In 9th operation we remove the maximum element from heap. So the ne heap becomes -> [1].
In 10th operation we change the 0th index element to 2. So new heap becomes -> [2].
In 11th operation we output the maximum element of the heap i.e. 2.
---------------------------------------
Constraints:
1 <= n <= 10^5
-10^5 <= nums[i] <= 10^5
"""


class Solution:

    def __init__(self):
        self.heap = []
        self.size = 0

    def heapifyUp(self, index):
        parentIdx = (index - 1) // 2
        if index > 0 and self.heap[parentIdx] < self.heap[index]:
            self.heap[parentIdx], self.heap[index] = self.heap[index], self.heap[parentIdx]
            self.heapifyUp(parentIdx)
        return

    def heapifyDown(self, index):
        leftChildIdx = 2 * index + 1
        rightChildIdx = 2 * index + 2
        largest = index

        if leftChildIdx < self.size and self.heap[leftChildIdx] > self.heap[largest]:
            largest = leftChildIdx

        if rightChildIdx < self.size and self.heap[rightChildIdx] > self.heap[largest]:
            largest = rightChildIdx

        if largest != index:
            self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
            self.heapifyDown(largest)
        return

    def initializeHeap(self):
        self.heap.clear()
        self.size = 0


    def insert(self, key):
        self.heap.append(key)
        self.size += 1
        self.heapifyUp(self.size - 1)
        return



    def changeKey(self, index, new_val):
        # Update the value at index `ind`
        if index < 0 or index >= self.size:
            return
        # If the updated value is smaller than previous value, heapify down
        if self.heap[index] > new_val:
            self.heap[index] = new_val
            self.heapifyDown(index)
        # If the updated value is greater than previous value, heapify up
        else:
            self.heap[index] = new_val
            self.heapifyUp(index)


    def extractMax(self):
        if self.size == 0:
            return None
        ele = self.heap[0]

        # Swap the root with the last element
        self.heap[0], self.heap[self.size - 1] = self.heap[self.size - 1], self.heap[0]

        # Remove the last element
        self.heap.pop()

        # Decrease the size of the heap
        self.size -= 1

        # Heapify down the root element
        if self.size > 0:
            self.heapifyDown(0)

        return ele


    def isEmpty(self):
        # Check if the heap is empty
        return self.size == 0

    def getMax(self):
        # Return the maximum element of the heap
        return self.heap[0]

    def heapSize(self):
        # Return the size of the heap
        return self.size


# Driver code
def main():
    # Creating an object of the Solution class
    heap = Solution()

    # Initializing a max heap data structure
    heap.initializeHeap()

    # Performing different operations
    heap.insert(4); print("Inserting 4 in the max-heap")
    heap.insert(1); print("Inserting 1 in the max-heap")
    heap.insert(10); print("Inserting 10 in the max-heap")
    print("Maximum value in the heap is:", heap.getMax())
    print("Size of max-heap is:", heap.heapSize())
    print("Is heap empty:", heap.isEmpty())
    print(f"Extracting maximum value from the heap -> {heap.extractMax()}")
    print("Maximum value in the heap is:", heap.getMax())
    print("Changing value at index 0 to 16")
    heap.changeKey(0, 16)
    print("Maximum value in the heap is:", heap.getMax())

if __name__ == "__main__":
    main()
