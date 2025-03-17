
# Topological sort or Kahn's algorithm
# Apply for DAG: Directed Acyclic Graph (DAG) is a directed graph with no cycles.
# Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge u v, vertex u comes before v in the ordering.
from collections import deque
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
        """
        1. Initialization:
           • We use an array 'inDegree' to keep track of how many prerequisites each vertex has.
           • All vertices with zero in-degree are added to our queue because they have no dependencies.

        2. BFS Processing:
           • We continuously pop vertices from the front of the queue.
           • For each vertex removed, we decrement the in-degree of its neighbours. If any neighbour's in-degree becomes 0, it is then added to the queue.

        3. Final Output:
           • The list 'topo' maintains the vertices in a valid topological order.
        """
        # V: Total number of vertices in the graph.
        # adj: Adjacency list representing the graph.

        # List to simulate a queue to process vertices with in-degree 0.
        queue = deque()

        # Array to store the in-degree (number of incoming edges) for each vertex.
        inDegree = [0] * V

        # Calculate in-degree for every vertex.
        # For each vertex i, look at all of its neighbours 'node' (i.e., all vertices that i points to).
        for i in range(V):
            for node in adj[i]:
                inDegree[node] += 1

        # Identify all vertices with in-degree 0 and add them to the queue.
        # Such vertices do not depend on any other vertices and can be processed first.
        for i in range(V):
            if inDegree[i] == 0:
                queue.append(i)

        # This list will store the vertices in topologically sorted order.
        topologicalOrder = []

        # Process vertices until the queue is empty.
        while queue:
            # Remove the vertex from the front of the queue.
            node = queue.popleft()

            # Add the current node to the topological order.
            topologicalOrder.append(node)

            # For every neighbour of the current vertex,
            # reduce its in-degree by 1 since we have now processed an incoming edge.
            for neighbor in adj[node]:
                inDegree[neighbor] -= 1

                # If in-degree becomes 0, it means no more prerequisites remain for 'neighbor',
                # so add it to the queue.
                if inDegree[neighbor] == 0:
                    queue.append(neighbor)

        # Finally, return the topologically sorted order of vertices.
        return topologicalOrder

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
