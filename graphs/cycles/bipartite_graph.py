
# Bipartite graph
from collections import deque
class Solution:
    def bfs(self, start, V, adj, color):
        queue = deque([start])
        color[start] = 1
        while queue:
            node = queue.popleft()
            for neighbor in adj[node]:
                if color[neighbor] == -1:
                    color[neighbor] = 1 - color[node]
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    return False
        return True

    def isBipartite(self, V, adj):
        color = [-1] * V
        for i in range(V):
            if color[i] == -1:
                if not self.bfs(i, V, adj, color):
                    return False
        return True



if __name__ == '__main__':
    sol = Solution()

    # Test 1
    V = 4
    adj=  [[1,3],[0,2],[1,3],[0,2]]
    print(sol.isBipartite(V, adj)) # True
    # print(sol.isBipartite(V, adj)) # True

    # Test 2
    V = 4
    adj = [[1,2,3],[0,2],[0,1,3],[0,2]]
    print(sol.isBipartite(V, adj)) # False
    # print(sol.isBipartite(V, adj)) # False
