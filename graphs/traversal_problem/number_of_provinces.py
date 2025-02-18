# Number Of Provinces


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

if __name__ == "__main__":

    sol = Solution()

    # Example 1
    adj = [[1,1,0],[1,1,0],[0,0,1]]
    print(sol.numProvinces(adj)) # Output: 2

    # Example 2
    adj = [[1,0,0],[0,1,0],[0,0,1]]
    print(sol.numProvinces(adj)) # Output: 3
