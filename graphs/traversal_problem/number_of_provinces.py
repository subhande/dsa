# Number Of Provinces
from collections import deque
from typing import List

class Solution:
    def numProvinces(self, adj: list[list]):
        """
        Parameters:
            adj: list[list] -> an adjacency matrix representing the graph
        Returns:
            int -> the number of provinces in the graph
        """
        V = len(adj)
        graph = {i: [] for i in range(V)}
        visited = set()

        # Populate the adjacency list with the undirected edges
        for i in range(V):
            for j in range(V):
                if adj[i][j] == 1:
                    graph[i].append(j)
                    graph[j].append(i)

        # A helper method for DFS traversal
        def dfs(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)


        province_count = 0
        for vertex in range(V):
            if vertex not in visited:
                province_count += 1
                dfs(vertex)

        return province_count

class Solution2:

    def bfs(self, node, visited, isConnected):

        visited[node] = True

        queue = deque([node])

        while queue:
            node = queue.popleft()

            for i in range(len(isConnected)):
                if isConnected[node][i] == 1 and not visited[i]:
                    visited[i] = True
                    queue.append(i)



    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        no_of_provinces = 0

        for i in range(n):
            if not visited[i]:
                no_of_provinces += 1
                self.bfs(i, visited, isConnected)

        return no_of_provinces

if __name__ == "__main__":

    sol = Solution()

    # Example 1
    adj = [[1,1,0],[1,1,0],[0,0,1]]
    print(sol.numProvinces(adj)) # Output: 2

    # Example 2
    adj = [[1,0,0],[0,1,0],[0,0,1]]
    print(sol.numProvinces(adj)) # Output: 3

    # Example 3
    adj = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
    print(sol.numProvinces(adj)) # Output: 1

    sol = Solution2()

    # Example 1
    adj = [[1,1,0],[1,1,0],[0,0,1]]
    print(sol.findCircleNum(adj)) # Output: 2

    # Example 2
    adj = [[1,0,0],[0,1,0],[0,0,1]]
    print(sol.findCircleNum(adj)) # Output: 3

    # Example 3
    adj = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
    print(sol.findCircleNum(adj)) # Output: 1
