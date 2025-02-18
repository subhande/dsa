
# Topological sort or Kahn's algorithm
# Apply for DAG: Directed Acyclic Graph (DAG) is a directed graph with no cycles.
# Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge u v, vertex u comes before v in the ordering.

class Solution:
    def topoSortUsingDFS(self, V, adj):
        visited = [False] * V
        stack = []

        def dfs(node):
            visited[node] = True
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    dfs(neighbor)
            stack.append(node)

        for node in range(V):
            if not visited[node]:
                dfs(node)
        return stack[::-1]

    # Kahn's algorithm
    def topoSortUsingBFS(self, V, adj):
        indegree = [0] * V
        for node in range(V):
            for neighbor in adj[node]:
                indegree[neighbor] += 1

        queue = []
        for i in range(V):
            if indegree[i] == 0:
                queue.append(i)

        topoOrder = []
        while queue:
            current = queue.pop(0)
            topoOrder.append(current)
            for neighbor in adj[current]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return topoOrder

if __name__ == '__main__':
    sol = Solution()

    # Test 1
    V = 6
    adj =[ [ ], [ ], [3], [1], [0,1], [0,2] ]
    output = [5, 4, 2, 3, 1, 0]
    print(f"Expected output: {output}")
    print(f"Actual output: {sol.topoSortUsingDFS(V, adj)}")
    print(f"Actual output: {sol.topoSortUsingBFS(V, adj)}")

    # Test 2
    V = 4
    adj = [ [ ], [0], [0], [0] ]
    output = [3, 2, 1, 0]
    print(f"Expected output: {output}")
    print(f"Actual output: {sol.topoSortUsingDFS(V, adj)}")
    print(f"Actual output: {sol.topoSortUsingBFS(V, adj)}")
