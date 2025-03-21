# Number of operations to make network connected
# https://takeuforward.org/plus/dsa/graph/hard-problems-ii/number-of-operations-to-make-network-connected
# https://leetcode.com/problems/number-of-operations-to-make-network-connected/description/

from collections import deque
from typing import List


class DisjointSet:
    def __init__(self, n):
        self.rank = [0] * n
        self.parent = [i for i in range(n)]

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
    def makeConnectedBFS(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        adj = [[] for _ in range(n)]
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * n
        components = 0

        for i in range(n):
            if not visited[i]:
                components += 1
                q = deque([i])
                while q:
                    node = q.popleft()
                    visited[node] = True
                    for neighbor in adj[node]:
                        if not visited[neighbor]:
                            q.append(neighbor)

        return components - 1

    def makeConnectedUnionFind(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        ds = DisjointSet(n)
        noOfComponents = n

        for u, v in connections:
            if not ds.find(u, v):
                ds.union(u, v)
                noOfComponents -= 1

        return noOfComponents - 1
