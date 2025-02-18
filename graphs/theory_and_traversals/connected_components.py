# Connected Components

"""
The idea is to build an adjacency list from the given edges and then traverse the graph. Every time we discover a vertex that has not been visited, we perform DFS (or BFS) from that vertex to mark all reachable vertices in the same connected component. Finally, we count how many times we initiated a DFS which is equal to the number of connected components.

-------
Explanation of the code:

1. Building the Graph:
   - We create a dictionary called "graph" where each key is a vertex (from 0 to V-1) and each value is a list that will store the connected neighbors.
   - For every undirected edge in the list "edges", we add the corresponding vertices as neighbors.

2. DFS Helper Function:
   - The "dfs" function takes a starting node and marks it as visited.
   - It then recursively visits all its unvisited neighbors. This effectively traverses the entire component.

3. Counting Components:
   - We iterate through every vertex from 0 to V-1.
   - If a vertex has not been visited, it means a new component is found. We increment the counter and run DFS from that vertex to mark all vertices in this component.

4. Return the total count of connected components.

This solution efficiently counts the number of connected components in an undirected graph.
"""

class Solution:
    # Time Complexity: O(V + E) | Space Complexity: O(V + E)
    def findNumberOfComponent(self, E, V, edges):
        # Create a graph as an adjacency list
        # Initialize each vertex's list of neighbours as empty
        graph = {i: [] for i in range(V)}

        # Populate the adjacency list with the undirected edges
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # A set to keep track of visited nodes
        visited = set()

        # A helper method for DFS traversal
        # Time Complexity: O(V + E)
        def dfs(node):
            # Mark current node as visited
            visited.add(node)
            # Visit all neighbors that are not yet visited
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        # A helper method for BFS traversal
        # Time Complexity: O(V + E)
        def bfs(node):
            # Initialize a queue with the current node
            queue = [node]
            # Mark current node as visited
            visited.add(node)
            # Visit all neighbors that are not yet visited
            while queue:
                current = queue.pop(0)
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

        # Count of connected components
        component_count = 0

        # Iterate over every vertex. If it hasn't been visited,
        # it is the start of a new connected component
        for vertex in range(V):
            if vertex not in visited:
                component_count += 1  # Found a new component
                dfs(vertex)           # Visit all nodes in this component using DFS
                # bfs(vertex)         # Use BFS instead of DFS

        return component_count


if __name__ == "__main__":
    s = Solution()

    # Test Case 1
    E = 2
    V = 4
    edges = [[0, 1], [1, 2]]

    print(s.findNumberOfComponent(E, V, edges)) # 2

    # Test Case 2
    E = 4
    V = 7
    edges = [[0, 1], [1, 2], [2, 3], [4, 5]]
    print(s.findNumberOfComponent(E, V, edges)) # 3
