# First Unique Number

from collections import deque
from typing import List


# Approach 1: Brute Force | TLE
class FirstUnique:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.freq = {}
        for num in nums:
            self.freq[num] = self.freq.get(num, 0) + 1

    def showFirstUnique(self) -> int:
        for num in self.nums:
            if self.freq.get(num, 0) == 1:
                return num
        return -1

    def add(self, value: int) -> None:
        self.nums.append(value)
        self.freq[value] = self.freq.get(value, 0) + 1


# Approach 2: Using Queue and HashMap
class FirstUnique2:
    def __init__(self, nums: List[int]):
        self.freq = {}
        for num in nums:
            self.freq[num] = self.freq.get(num, 0) + 1
        self.queue = deque()
        for num in nums:
            if self.freq.get(num, 0) == 1:
                self.queue.append(num)

    def showFirstUnique(self) -> int:
        if self.queue:
            return self.queue[0]
        return -1

    def add(self, value: int) -> None:
        self.freq[value] = self.freq.get(value, 0) + 1
        if self.freq.get(value, 0) == 1:
            self.queue.append(value)
        elif self.queue and self.queue[0] == value:
            while self.queue and self.freq.get(self.queue[0], 0) > 1:
                self.queue.popleft()


# Approach 2: Using Queue and HashMap [Cleaner Implementation]
class FirstUnique3:
    def __init__(self, nums: List[int]):
        self._queue = deque(nums)
        self._is_unique = {}
        for num in nums:
            # Notice that we're calling the "add" method of FirstUnique; not of the queue.
            self.add(num)

    def showFirstUnique(self) -> int:
        # We need to start by "cleaning" the queue of any non-uniques at the start.
        # Note that we know that if a value is in the queue, then it is also in
        # is_unique, as the implementation of add() guarantees this.
        while self._queue and not self._is_unique[self._queue[0]]:
            self._queue.popleft()
        # Check if there is still a value left in the queue. There might be no uniques.
        if self._queue:
            return self._queue[0]  # We don't want to actually *remove* the value.
        return -1

    def add(self, value: int) -> None:
        # Case 1: We need to add the number to the queue and mark it as unique.
        if value not in self._is_unique:
            self._is_unique[value] = True
            self._queue.append(value)
        # Case 2 and 3: We need to mark the number as no longer unique.
        else:
            self._is_unique[value] = False


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
