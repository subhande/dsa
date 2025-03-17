# Shortest Path In An Undirected Graph With Unit Weights
# https://takeuforward.org/plus/dsa/graph/hard-problems/shortest-path-in-undirected-graph-with-unit-weights

from collections import deque

class Solution:
    def bfs (self, src, adj, dist):
        queue = deque()

        queue.append(src)

        while queue:
            node = queue.popleft()

            for neighbor in adj[node]:
                if dist[node] + 1 < dist[neighbor]:
                    dist[neighbor] = dist[node] + 1
                    queue.append(neighbor)

    def shortestPath(self, edges, N, M):
        adj = [[] for _ in range(N)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        dist = [float('inf')] * N

        dist[0] = 0

        self.bfs(0, adj, dist)

        for i in range(N):
            if dist[i] == float('inf'):
                dist[i] = -1

        return dist
