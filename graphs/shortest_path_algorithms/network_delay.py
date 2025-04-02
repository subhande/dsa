# Network Delay
# https://leetcode.com/problems/network-delay-time/description/

from typing import List
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adjList = [[] for _ in range(n+1)]

        for edge in times:
           adjList[edge[0]].append((edge[1], edge[2]))
        INF = float("inf")
        durations = [INF] * (n+1)
        durations[k] = 0

        minHeap = [(0, k)]

        while minHeap:
            timeElapsed, node = heapq.heappop(minHeap)
            for neighbour, time in adjList[node]:
                if timeElapsed + time < durations[neighbour]:

                    durations[neighbour] = timeElapsed + time

                    heapq.heappush(minHeap, (durations[neighbour], neighbour))

        for i in range(1, n+1):
            if durations[i] == INF:
                return -1
        return max(durations[1:])
