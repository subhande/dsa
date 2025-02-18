
# Detect a cycle in an directed graph

class Solution:
    # Helper for DFS cycle detection. Here, "parent" will be used as the recursion stack.
    def dfs(self, adj, visited, recStack, node):
        visited[node] = True
        recStack[node] = True  # mark this node in the current DFS path

        # Explore each neighbor
        for neighbor in adj[node]:
            # If neighbor is not visited, recursively continue DFS.
            if not visited[neighbor]:
                if self.dfs(adj, visited, recStack, neighbor):
                    return True
            # If neighbor is in the recursion stack, there is a cycle.
            elif recStack[neighbor]:
                return True

        recStack[node] = False  # remove the node from current DFS path
        return False

    def isCycleDFS(self, V, adj):
        visited = [False] * V
        recStack = [False] * V  # This acts as "parent" or recursion stack.
        for node in range(V):
            if not visited[node]:
                if self.dfs(adj, visited, recStack, node):
                    return True
        return False

    # Although a bfs helper method signature is provided, for directed graphs
    # a cleaner way is to use Kahn's algorithm to detect cycles.
    def bfs(self, adj, V):
        # First, build in-degree for each node.
        indegree = [0] * V
        for node in range(V):
            for neighbor in adj[node]:
                indegree[neighbor] += 1

        # Create a queue and enqueue all vertices with in-degree 0.
        queue = []
        for i in range(V):
            if indegree[i] == 0:
                queue.append(i)

        count = 0  # count of vertices in topological order
        while queue:
            current = queue.pop(0)
            count += 1
            for neighbor in adj[current]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # If count of processed vertices is not equal to V then there is a cycle.
        if count != V:
            return True
        else:
            return False

    def isCycleBFS(self, V, adj):
        return self.bfs(adj, V)


# Testing the solution:
if __name__ == '__main__':
    sol = Solution()

    # Test 1
    V = 6
    adj = [ [1], [2, 5], [3], [4], [1], [] ]
    print(sol.isCycleDFS(V, adj))  # Expected output: True
    print(sol.isCycleBFS(V, adj))  # Expected output: True

    # Test 2
    V = 4
    adj = [[1, 2], [2], [], [0, 2]]
    print(sol.isCycleDFS(V, adj))  # Expected output: False
    print(sol.isCycleBFS(V, adj))  # Expected output: False
