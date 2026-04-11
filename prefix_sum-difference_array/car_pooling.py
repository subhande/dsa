# Car Pooling

from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        # Step 1: Find the farthest point we need to consider
        # trip[-1] = end location of each trip
        maxDist = max([trip[-1] for trip in trips])

        # Step 2: Create a "difference array" to track passenger changes
        # passengers[i] will store net change at location i
        passengers = [0] * (maxDist + 1)

        # Step 3: Process each trip
        for trip in trips:
            num_passengers = trip[0]
            start = trip[1]
            end = trip[2]

            # At 'start', passengers get in → increase
            passengers[start] += num_passengers

            # At 'end', passengers get out → decrease
            passengers[end] -= num_passengers

        # Step 4: Traverse and compute prefix sum
        currNoOfPassengers = 0
        for p in passengers:
            currNoOfPassengers += p  # accumulate passengers

            # If at any point capacity exceeded → not possible
            if currNoOfPassengers > capacity:
                return False

        # If never exceeded capacity → valid
        return True
