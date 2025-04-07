# Find The MST Weight
#
import heapq

"""
1. In spanningTreePrimAlgorithm:
   - A min-heap (priority queue) is used to always pick the edge with the least weight.
   - An array "visited" keeps track of vertices already in the MST.
   - Starting from vertex 0, we push its neighbors into the heap.
   - We then extract the smallest edge that connects to an unvisited vertex, add its weight, mark the vertex as visited, and push its unvisited neighbors.
   - The process continues until all vertices are included.

2. In spanningTreeKruskalAlgorithm:
   - We first convert the adjacency list into an edge list and eliminate duplicate edges by only considering edges when u < v.
   - The edges are sorted by weight.
   - A union-find (DSU) structure is used to check for cycles while adding edges.
   - The smallest edge is added if it connects two different trees (using union-find). This continues until the MST has V - 1 edges.

"""

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def findParent(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.findParent(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        pu, pv = self.findParent(u), self.findParent(v)
        if pu != pv:
            if self.rank[pu] < self.rank[pv]:
                self.parent[pu] = pv
            elif self.rank[pu] > self.rank[pv]:
                self.parent[pv] = pu
            else:
                self.parent[pv] = pu
                self.rank[pu] += 1

    def find(self, u, v):
        return self.findParent(u) == self.findParent(v)

class Solution:
    # Prim's Algorithm
    # Time complexity: O(ElogE) | Space complexity: O(E + V)
    def spanningTreePrimAlgorithm(self, V, adj):
        total_weight = 0
        visited = [False] * V
        # Start from vertex 0 (can start from any vertex)
        minHeap = [(0, 0)] # (weight, vertex)

        while minHeap:
            weight, node = heapq.heappop(minHeap)

            if visited[node]:
                continue

            visited[node] = True
            total_weight += weight

            for neighbor, w in adj[node]:
                if not visited[neighbor]:
                    heapq.heappush(minHeap, (w, neighbor))

        return total_weight

    # Kruskal's Algorithm
    # Time complexity: O(V+E) + O(ElogE) + O(E*4α*2) |  | Space complexity: O(V+E)
    def spanningTreeKruskalAlgorithm(self, V, adj):
        edges = []
        for u in range(V):
            for v, w in adj[u]:
                if u < v:
                    edges.append((w, u, v))
        edges.sort()

        total_weight = 0

        dsu = DisjointSet(V)

        for w, u, v in edges:
            if not dsu.find(u, v):
                dsu.union(u, v)
                total_weight += w

        return total_weight


if __name__ == '__main__':

    sol = Solution()

    # Test 1
    V = 4
    edges = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [0, 3, 4]]
    adj = [[] for _ in range(V)]
    for u, v, w in edges:
        adj[u].append([v, w])
        adj[v].append([u, w])
    print(sol.spanningTreePrimAlgorithm(V, adj))  # Expected output: 6
    print(sol.spanningTreeKruskalAlgorithm(V, adj))  # Expected output: 6
