# Top K Frequent Elements

from typing import List
from collections import Counter
class Heap:
    def __init__(self, arr: List[tuple]):
        print(arr)
        self.heap = arr
        self.size = len(arr)
        self.buildMaxHeap()

    def buildMaxHeap(self):
        for i in range(self.size // 2 - 1, -1, -1):
            self.heapifyDown(i)

    def heapifyDown(self, index):

        largest = index
        left = index * 2 + 1
        right = index * 2 + 2

        if left < self.size and self.heap[left][0] > self.heap[largest][0]:
            largest = left
        if right < self.size and self.heap[right][0] > self.heap[largest][0]:
            largest = right

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.heapifyDown(largest)
        return

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count the frequency of each element in nums
        count = Counter(nums)

        # Create a max heap based on the frequencies
        heap = Heap([(freq, num) for num, freq in count.items()])

        # Extract the top k frequent elements
        top_k = []
        for _ in range(k):
            top_k.append(heap.heap[0][1])
            heap.size -= 1
            heap.heap[0] = heap.heap[heap.size]
            heap.heapifyDown(0)

        return top_k
