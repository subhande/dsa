
# Number Of Islands II
# https://leetcode.com/problems/number-of-islands-ii/description/
# https://takeuforward.org/plus/dsa/graph/hard-problems-ii/number-of-islands-ii



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
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        ds = DisjointSet(m * n)
        res = []
        islands = 0
        vis = [[0] * n for _ in range(m)]
        for r, c in positions:
            node = r * n + c
            if vis[r][c]:
                res.append(islands)
                continue
            vis[r][c] = 1
            islands += 1
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and vis[nr][nc] == 1:
                    adjNode = nr * n + nc
                    if ds.findParent(node) != ds.findParent(adjNode):
                        islands -= 1
                        ds.union(node, adjNode)
            res.append(islands)
        return res


if __name__ == "__main__":
    s = Solution()
    n = 4
    m = 5
    k = 12
    positions = [[0,0],[0,0],[1,1],[1,0],[0,1],[0,3],[1,3],[0,4], [3,2], [2,2],[1,2], [0,2]]

    print(s.numIslands2(n, m, positions))
