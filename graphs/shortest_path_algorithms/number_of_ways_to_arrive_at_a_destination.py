# Number of ways to arrive at a destination
# https://takeuforward.org/plus/dsa/graph/shortest-path-algorithms/number-of-ways-to-arrive-at-destination

import heapq

from typing import List

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adjList = [[] for _ in range(n)]
        MOD = 10 ** 9 + 7
        INF = float("inf")

        for road in roads:
            adjList[road[0]].append((road[1], road[2]))
            adjList[road[1]].append((road[0], road[2]))

        dist = [INF] * n
        minWays = [0] * n


        dist[0] = 0
        minWays[0] = 1

        minHeap = [(0, 0)]

        while minHeap:

            timeElapsed, node = heapq.heappop(minHeap)

            if timeElapsed > dist[node]:
                continue

            for neighbor, duration in adjList[node]:

                if timeElapsed + duration < dist[neighbor]:

                    dist[neighbor] = timeElapsed + duration

                    minWays[neighbor] = minWays[node]

                    heapq.heappush(minHeap, (dist[neighbor], neighbor))

                elif dist[node] + duration == dist[neighbor]:

                    minWays[neighbor] = (minWays[neighbor] + minWays[node]) % MOD

        return minWays[-1]
