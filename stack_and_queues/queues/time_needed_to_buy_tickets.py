from collections import deque
from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque()

        for idx, ticket in enumerate(tickets):
            queue.append((idx, ticket))

        time_elapsed = 0

        while queue:
            idx, remaining = queue.popleft()

            remaining -= 1
            time_elapsed += 1

            if idx == k and remaining == 0:
                break
            if remaining > 0:
                queue.append((idx, remaining))
        return time_elapsed
