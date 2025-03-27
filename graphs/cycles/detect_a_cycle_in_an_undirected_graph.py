
# Detect a cycle in an undirected graph

class Solution:
    def dfs(self, graph, visited, parent, node):
        visited[node] = True
        stack = [(node, parent)]
        while stack:
            node, parent = stack.pop()
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    stack.append((neighbor, node))
                    visited[neighbor] = True
                elif neighbor != parent:
                    return True

    # Time complexity: O(V + E) | Space complexity: O(V)
    def isCycleDFS(self, V, adj):
        graph = {}
        for i in range(V):
            graph[i] = adj[i]
        visited = [False] * V
        for node in range(V):
            if not visited[node]:
                if self.dfs(graph, visited, -1, node):
                    return True
        return False


    def bfs(self, graph, visited, parent, node):
        queue = [(node, parent)]
        while queue:
            node, parent = queue.pop(0)
            visited[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    queue.append((neighbor, node))
                elif neighbor != parent:
                    return True
        return False

    # Time complexity: O(V + E) | Space complexity: O(V)
    def isCycleBFS(self, V, adj):
        graph = {}
        for i in range(V):
            graph[i] = adj[i]
        visited = [False] * V
        for node in range(V):
            if not visited[node]:
                if self.bfs(graph, visited, -1, node):
                    return True
        return False








if __name__ == '__main__':
    sol = Solution()

    # Test 1
    V = 6
    adj= [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]
    print(sol.isCycleDFS(V, adj)) # True
    print(sol.isCycleBFS(V, adj)) # True

    # Test 2
    V = 4
    adj = [[1, 2], [0], [0, 3], [2]]
    print(sol.isCycleDFS(V, adj)) # False
    print(sol.isCycleBFS(V, adj)) # False
