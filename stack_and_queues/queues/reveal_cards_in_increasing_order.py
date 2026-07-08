# Reveal Cards in Increasing Order

from collections import deque
from typing import List


# Approach 1: Simulation using Queue
# Time Complexity: O(n log n)
# Space Complexity: O(n)
class Solution1:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        # Sort the cards so they can be revealed in increasing order.
        deck.sort()

        n = len(deck)

        # Stores the final arrangement of cards.
        result = [0] * n

        # Queue stores the available positions in the deck.
        queue = deque(range(n))

        for card in deck:
            # Place the current smallest card at the next revealed position.
            index = queue.popleft()
            result[index] = card

            # Simulate moving the next top card to the bottom.
            if queue:
                queue.append(queue.popleft())

        return result


# Approach 2: Reverse Simulation using Two Pointers
# Time Complexity: O(n log n)
# Space Complexity: O(n)
