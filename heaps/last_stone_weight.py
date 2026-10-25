# Last Stone Weight


# Approach 1: Array-Based Simulation
# Time Complexity: O(n^2) | Space Complexity: O(1)
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        def remove_largest():
            index_of_largest = stones.index(max(stones))
            # Remove largest stone
            return stones.pop(index_of_largest)

        while len(stones) > 1:
            stone_1 = remove_largest()
            stone_2 = remove_largest()
            if stone_1 != stone_2:
                stones.append(stone_1 - stone_2)

        return stones[0] if stones else 0


# Approach 2: Sorted Array-Based Simulation
# Time Complexity: O(n^2) | Space Complexity: O(1)
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            stone_1 = stones.pop()
            stone_2 = stones.pop()
            if stone_1 != stone_2:
                bisect.insort(stones, stone_1 - stone_2)
        return stones[0] if stones else 0


# Approach 3.1: Heap-Based Simulation
# Time Complexity: O(n log n) | Space Complexity: O(n)


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # Make all the stones negative. We want to do this *in place*, to keep the
        # space complexity of this algorithm at O(1). :-)
        for i in range(len(stones)):
            stones[i] *= -1

        # Heapify all the stones.
        heapq.heapify(stones)

        # While there is more than one stone left, remove the two
        # largest, smash them together, and insert the result
        # back into the heap if it is non-zero.
        while len(stones) > 1:
            stone_1 = heapq.heappop(stones)
            stone_2 = heapq.heappop(stones)
            if stone_1 != stone_2:
                heapq.heappush(stones, stone_1 - stone_2)

        # Check if there is a stone left to return. Convert it back
        # to positive.
        return -heapq.heappop(stones) if stones else 0


# Approach 3.2: Heap-Based Simulation Without Heap Library
# Time Complexity: O(n log n) | Space Complexity: O(n)


class Solution:
    def heapifyDownMax(self, arr, index, heapSize):
        largest = index
        leftChild = 2 * index + 1
        rightChild = 2 * index + 2

        if leftChild < heapSize and arr[leftChild] > arr[index]:
            largest = leftChild

        if rightChild < heapSize and arr[rightChild] > arr[largest]:
            largest = rightChild

        if largest != index:
            arr[index], arr[largest] = arr[largest], arr[index]
            self.heapifyDownMax(arr, largest, heapSize)

    def heapifyUpMax(self, arr, index):
        parent = (index - 1) // 2

        if index > 0 and arr[index] > arr[parent]:
            arr[index], arr[parent] = arr[parent], arr[index]

            index = parent

            self.heapifyUpMax(arr, index)

    def buildMaxHeap(self, arr):
        heapSize = len(arr)

        for i in range((heapSize // 2) - 1, -1, -1):
            self.heapifyDownMax(arr, i, heapSize)

    def lastStoneWeight(self, stones: list[int]) -> int:

        self.buildMaxHeap(stones)

        heapSize = len(stones)

        print(stones)
        while heapSize > 1:
            print(stones)

            ele1 = stones[0]
            stones[0], stones[heapSize - 1] = stones[heapSize - 1], stones[0]
            heapSize -= 1
            self.heapifyDownMax(stones, 0, heapSize)

            ele2 = stones[0]
            stones[0], stones[heapSize - 1] = stones[heapSize - 1], stones[0]
            heapSize -= 1
            self.heapifyDownMax(stones, 0, heapSize)

            if ele1 - ele2 > 0:
                heapSize += 1
                stones[heapSize - 1] = ele1 - ele2
                self.heapifyUpMax(stones, heapSize - 1)

        return stones[0] if heapSize == 1 else 0
