from typing import List

# Ref: https://www.youtube.com/watch?v=Pr6T-3yB9RM


# Basic Idea:
# Key Assumptions Given:
# 1. Each car has a position and a speed.
# 2. A car can catch up to another car if it is faster and behind it
# 3. When a faster car catches up to a slower car, they form a fleet
# 4. Single Lane road, so cars cannot pass each other.
# Solution Approach:
# 1. Sort the cars based on their positions.
# 2. Calculate the time it takes for each car to reach the target.
# 3. Use a stack to keep track of the fleets. If a car takes more time to reach the target than the car in front of it, it forms a new fleet. Otherwise, it joins the fleet of the car in front of it.


# Time Complexity: O(nlogn) - Sorting the cars based on their positions takes O(nlogn) time. The subsequent loop to calculate the time to reach the target and manage the stack takes O(n) time.
# Space Complexity: O(n) - We use additional space to store the time to reach the target for each car and the stack to keep track of the fleets.
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # n = len(position)
        # cars = [(position[i], speed[i]) for i in range(n)]
        # cars.sort(key=lambda x: x[0])
        # stack = []
        # timeToReachTarget = [0] * n

        # for idx in range(n):
        #     timeToReachTarget[idx] = (target - cars[idx][0]) / cars[idx][1]

        n = len(position)
        cars = sorted(zip(position, speed))
        timeToReachTarget = [float(target - p) / s for p, s in cars]
        stack = []

        for idx in range(n - 1, -1, -1):
            if not stack:
                stack.append(timeToReachTarget[idx])
            else:
                if timeToReachTarget[idx] > stack[-1]:
                    stack.append(timeToReachTarget[idx])
        return len(stack)
