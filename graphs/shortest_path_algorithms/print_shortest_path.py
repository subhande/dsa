# Print Shortest Path

import heapq
from typing import List

class Solution:
    def dijkstraUsingHeap(self, V, adj, S, parent):
        INF = float('inf')

        dist = [INF] * V

        dist[S] = 0

        minHeap = [(0, S)]

        while minHeap:

            d, node = heapq.heappop(minHeap)

            for neighbor, weight in adj[node]:
                if dist[neighbor] > dist[node] + weight:
                    dist[neighbor] = dist[node] + weight
                    heapq.heappush(minHeap, (dist[neighbor], neighbor))
                    parent[neighbor] = node
        return dist

    def shortestPath(self, n:int, m:int, edges:List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n+1)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        parent = list(range(n+1))
        dist = self.dijkstraUsingHeap(n+1, adj, 1, parent)

        if dist[n] == float('inf'):
            return [-1]

        path = []

        node = n

        while parent[node] != node:
            path.append(node)
            node = parent[node]

        path.append(1)

        path.append(dist[n])

        return path[::-1]


if __name__ == '__main__':

    sol = Solution()

    # Test 1
    n = 5
    m = 6
    edges = [[1,2,2], [2,5,5], [2,3,4], [1,4,1],[4,3,3],[3,5,1]]
    print(sol.shortestPath(n, m, edges))  # Expected output: [5, 1, 4, 3, 5]

    # Test 2
    n = 4
    m = 4
    edges = [[1,2,2], [2,3,4], [1,4,1],[4,3,3]]
    print(sol.shortestPath(n, m, edges))  # Expected output: [1, 4, 4]
