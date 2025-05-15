# Car Pooling

from typing import List

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        maxDist = max([trip[-1] for trip in trips])
        passengers = [0] * (maxDist + 1)

        for trip in trips:
            passengers[trip[1]] += trip[0]
            passengers[trip[2]] -= trip[0]

        currNoOfPassengers = 0
        for p in passengers:
            currNoOfPassengers += p
            if currNoOfPassengers > capacity:
                return False
        return True
