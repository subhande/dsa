# Detect a cycle in an undirected graph

"""
Explanation of Detect a Cycle in an Undirected Graph

Given `V` vertices and an adjacency list `adj`, return True if the undirected graph contains a cycle.

### Core Idea

Traverse the graph (DFS or BFS) while remembering the **parent** each node was reached from.
If we see a neighbor that is **already visited** and is **not the parent**, then there are two
different paths to that neighbor → a cycle exists.

The parent check matters because in an undirected graph every edge `u - v` appears in both
`adj[u]` and `adj[v]`. Going back along the same edge to the parent is not a cycle.

### Step-by-step Walkthrough

1. **Setup:** Build the graph and a `visited` array of size `V`.
2. **Handle components:** Loop over every node. If it is unvisited, start a traversal from it
   with parent `-1`. The graph may be disconnected, so one traversal is not enough.
3. **Traverse:** Push `(node, parent)` pairs onto a stack (DFS) or queue (BFS). For each neighbor:
   - Unvisited → mark it visited and push it with the current node as its parent.
   - Visited and not the parent → cycle found, return True.
4. **Finish:** If no traversal finds a cycle, return False.

### Why It Works

- A tree (no cycle) has exactly one path between any two nodes, so the only visited neighbor
  a node can ever see is its parent.
- A visited non-parent neighbor means the traversal reached it by a second path, which closes a loop.

### Time & Space Complexity

- **Time:** O(V + E) — every node is visited once and every edge is checked twice (once from each end).
- **Space:** O(V) — for `visited` and the stack/queue.

### Quick Example

For `adj = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]`:

- Start at 0: visit 1 and 3 (parent 0).
- From 3: visit 4 (parent 3).
- From 4: neighbor 1 is already visited and is not 4's parent (3) → cycle `0 - 1 - 4 - 3 - 0`.
"""


class Solution:
    def dfs(self, graph, visited, parent, node):
        visited[node] = True
        # Store (node, parent) so each node knows which edge it came from
        stack = [(node, parent)]
        while stack:
            node, parent = stack.pop()
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    # First time seeing neighbor: current node becomes its parent
                    stack.append((neighbor, node))
                    visited[neighbor] = True
                elif neighbor != parent:
                    # Visited but not the edge we came from -> second path -> cycle
                    return True

    # Time complexity: O(V + E) | Space complexity: O(V)
    def isCycleDFS(self, V, adj):
        graph = {}
        for i in range(V):
            graph[i] = adj[i]
        visited = [False] * V
        # Graph may be disconnected, so start a traversal from every unvisited node
        for node in range(V):
            if not visited[node]:
                if self.dfs(graph, visited, -1, node):
                    return True
        return False

    def bfs(self, graph, visited, parent, node):
        # Store (node, parent) so each node knows which edge it came from
        queue = [(node, parent)]
        while queue:
            node, parent = queue.pop(0)
            visited[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    # Unvisited: explore it later with current node as its parent
                    queue.append((neighbor, node))
                elif neighbor != parent:
                    # Visited but not the edge we came from -> second path -> cycle
                    return True
        return False

    # Time complexity: O(V + E) | Space complexity: O(V)
    def isCycleBFS(self, V, adj):
        graph = {}
        for i in range(V):
            graph[i] = adj[i]
        visited = [False] * V
        # Graph may be disconnected, so start a traversal from every unvisited node
        for node in range(V):
            if not visited[node]:
                if self.bfs(graph, visited, -1, node):
                    return True
        return False


from collections import deque
from typing import List


class SolutionLeetcode:
    def isValid(self, row, col, rows, cols):
        return 0 <= row < rows and 0 <= col < cols

    def bfs(self, r, c, rows, cols, grid, value, visitedValue):
        queue = deque()
        grid[r][c] = visitedValue
        queue.append((r, c, (-1, -1)))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            row, col, parent = queue.popleft()
            for dr, dc in directions:
                nr = row + dr
                nc = col + dc
                if self.isValid(nr, nc, rows, cols):
                    if grid[nr][nc] == value:
                        queue.append((nr, nc, (row, col)))
                        grid[nr][nc] = visitedValue
                    elif grid[nr][nc] == visitedValue and (nr, nc) != parent:
                        return True
        return False

    def containsCycle(self, grid: List[List[str]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if "vis-" not in grid[row][col] and self.bfs(
                    row, col, rows, cols, grid, grid[row][col], "vis-" + grid[row][col]
                ):
                    return True
        return False


if __name__ == "__main__":
    sol = Solution()

    # Test 1
    V = 6
    adj = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]
    print(sol.isCycleDFS(V, adj))  # True
    print(sol.isCycleBFS(V, adj))  # True

    # Test 2
    V = 4
    adj = [[1, 2], [0], [0, 3], [2]]
    print(sol.isCycleDFS(V, adj))  # False
    print(sol.isCycleBFS(V, adj))  # False
