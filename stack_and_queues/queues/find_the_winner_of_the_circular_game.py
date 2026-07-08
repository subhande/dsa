# Find the winner of the circular game

from collections import deque


# Approach 1: Brute Force with list manipulation
# Time Complexity: O(n^2) | Space Complexity: O(n)
class Solution1:
    def findTheWinner(self, n: int, k: int) -> int:
        # Initialize list of N friends, labeled from 1-N
        circle = list(range(1, n + 1))

        # Maintain the index of the friend to start the count on
        start_index = 0

        # Perform eliminations while there is more than 1 friend left
        while len(circle) > 1:
            # Calculate the index of the friend to be removed
            removal_index = (start_index + k - 1) % len(circle)

            # Remove the friend at removal_index
            circle.pop(removal_index)

            # Update the start_index for the next round
            start_index = removal_index

        return circle[0]


# Approach 2: Simulation using deque
# Time Complexity: O(n*k) | Space Complexity: O(n)
class Solution2:
    def findTheWinner(self, n: int, k: int) -> int:

        queue = deque(range(1, n + 1))

        while len(queue) != 1:
            for i in range(k - 1):
                queue.append(queue.popleft())
            queue.popleft()

        return queue[0]
