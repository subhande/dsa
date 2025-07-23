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
from collections import deque, defaultdict
from typing import List

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


class Solution2:

    # Depth-First Search (DFS) helper function
    def dfs(self, node, graph, visited):
        visited.add(node)  # Mark the current node as visited
        for neighbor in graph[node]:  # Traverse all neighbors of the current node
            if neighbor not in visited:  # If neighbor hasn't been visited
                self.dfs(neighbor, graph, visited)  # Recursively visit the neighbor

    # Breadth-First Search (BFS) helper function
    def bfs(self, node, graph, visited):
        queue = deque([node])  # Initialize queue with the starting node
        visited.add(node)      # Mark the starting node as visited

        while queue:  # Continue until the queue is empty
            current = queue.popleft()  # Get the next node from the queue
            for neighbor in graph[current]:  # Check all neighbors of the current node
                if neighbor not in visited:  # If neighbor hasn't been visited
                    visited.add(neighbor)   # Mark neighbor as visited
                    queue.append(neighbor)  # Add neighbor to the queue for further traversal

    # Main function to count the number of connected components in the graph
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        # Build the adjacency list for the graph
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])  # Add the edge in both directions (undirected)
            graph[edge[1]].append(edge[0])

        visited = set()  # Set to keep track of visited nodes
        connectedComponents = 0  # Counter for connected components

        # Iterate through all nodes from 0 to n-1
        for node in range(n):
            if node not in visited:  # If the node hasn't been visited yet
                connectedComponents += 1  # Found a new connected component
                self.bfs(node, graph, visited)  # Traverse all nodes in this component using BFS
                # Alternatively, you could use DFS:
                # self.dfs(node, graph, visited)
        return connectedComponents  # Return the total number of connected components


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


    s2 = Solution2()

    # Test Case 1
    n = 5
    edges = [[0, 1], [1, 2], [3, 4]]
    print(s2.countComponents(n, edges))  # Output: 2

    # Test Case 2
    n = 6
    edges = [[0, 1], [1, 2], [3, 4], [4, 5]]
    print(s2.countComponents(n, edges))  # Output: 2
