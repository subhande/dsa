# Shortest Path in a Directed Acyclic Graph (DAG)
# https://takeuforward.org/plus/dsa/graph/hard-problems/shortest-path-in-dag

from collections import deque

# Do Topological Sort and then relax the edges


class Solution:
    def topoSortDFS(self, adj, V):
        visited = [False] * V
        stack = []

        def dfs(node):
            visited[node] = True
            for neighbor in adj[node]:
                if not visited[neighbor[0]]:
                    dfs(neighbor[0])
            stack.append(node)

        for node in range(V):
            if not visited[node]:
                dfs(node)
        return stack[::-1]

    def shortestPath(self, N, M, edges):
        adj = [[] for _ in range(N)]
        for edge in edges:
            adj[edge[0]].append((edge[1], edge[2]))

        topoOrder = self.topoSortDFS(adj, N)

        # Initialize the distance array with infinity
        distance = [float("inf")] * N

        # Distance to the source node is 0
        distance[0] = 0

        # Relax the edges
        for node in topoOrder:
            if distance[node] != float("inf"):
                for neighbor in adj[node]:
                    distance[neighbor[0]] = min(
                        distance[neighbor[0]], distance[node] + neighbor[1]
                    )
        for i in range(N):
            if distance[i] == float("inf"):
                distance[i] = -1

        return distance



class Solution2:
    def topoSortBFS(self, adj, V):
        inDegree = [0] * V

        for node in range(V):
            for neighbor in adj[node]:
                inDegree[neighbor[0]] += 1

        queue = deque()
        for node in range(V):
            if inDegree[node] == 0:
                queue.append(node)
        topoOrder = []
        while queue:
            node = queue.popleft()
            topoOrder.append(node)
            for neighbor in adj[node]:
                inDegree[neighbor[0]] -= 1
                if inDegree[neighbor[0]] == 0:
                    queue.append(neighbor[0])
        return topoOrder


    def shortestPath(self, N, M, edges):
        adj = [[] for _ in range(N)]
        for edge in edges:
            adj[edge[0]].append((edge[1], edge[2]))

        topoOrder = self.topoSortBFS(adj, N)

        # Initialize the distance array with infinity
        distance = [float("inf")] * N

        # Distance to the source node is 0
        distance[0] = 0

        # Relax the edges
        for node in topoOrder:
            if distance[node] != float("inf"):
                for neighbor in adj[node]:
                    distance[neighbor[0]] = min(
                        distance[neighbor[0]], distance[node] + neighbor[1]
                    )
        for i in range(N):
            if distance[i] == float("inf"):
                distance[i] = -1

        return distance
