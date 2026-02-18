# Alien Dictionary
"""
Problem:
Given a sorted list of words from an unknown (alien) language, derive a valid ordering
of the characters in that language (i.e., the alien alphabet). If no valid ordering
exists (due to contradictions / cycles), return an empty string.

Approach:
1. Every unique character appearing in the input must appear in the output (even if it
   has no ordering constraints).
2. For each adjacent pair of words, find the first position where they differ:
      wordA[i] != wordB[i]
   Then we know: wordA[i] must come before wordB[i] in the alien alphabet, so we add a
   directed edge: wordA[i] -> wordB[i].
3. Invalid Case (Prefix Rule):
   If wordA starts with wordB but is longer (e.g., "abc" and "ab"), the ordering is invalid.
4. Perform a topological sort (Kahn's algorithm) over the directed graph constructed
   from these precedence constraints.
5. If we can produce a topological ordering containing all unique characters, return it.
   Otherwise (cycle detected), return "".


Complexity:
Let:
  W = number of words
  C = total number of characters across all words
  U = number of unique characters
  E = number of precedence relations (edges)
Building adjacency:  O(C)
Topological sort:    O(U + E)
Overall:             O(C + U + E)  (Effectively linear in input size)

Return:
- A string representing one valid alien alphabet ordering.
- "" (empty string) if no valid ordering exists.

Example (from the informal sketch below):

w -> r -> t
w -> r -> f
e -> r
e -> t

One valid ordering: e w r t f   (others may also be valid depending on constraints)
"""

from collections import deque, defaultdict
from typing import List


class Solution:
    def topoOrder(self, adj):
        """
        Perform Kahn's algorithm for topological sorting.

        Parameters:
            adj (dict[str, list[str]]): adjacency list mapping each node to its outgoing neighbors.

        Returns:
            str: A string containing a topological ordering of all nodes if possible.
                 Returns "" if a cycle is detected (i.e., not all nodes are processed).
        """
        # inDegree will track the number of incoming edges for each node
        inDegree = defaultdict(int)

        # Total number of unique nodes (characters)
        V = len(adj)

        # Build initial in-degree counts
        for node, edges in adj.items():
            # Ensure every node appears in inDegree even if it has no incoming edges
            if node not in inDegree:
                inDegree[node] = 0
            for edge in edges:
                inDegree[edge] += 1  # Increment incoming edge count for neighbor

        queue = deque()
        order = []

        # Initialize queue with nodes that have in-degree 0 (no prerequisites)
        for node, count in inDegree.items():
            if count == 0:
                queue.append(node)

        # Process nodes in BFS manner
        while queue:
            node = queue.popleft()
            order.append(node)

            # "Remove" edges going out from current node
            for neighbour in adj[node]:
                inDegree[neighbour] -= 1
                # If in-degree becomes zero, it is ready to be processed
                if inDegree[neighbour] == 0:
                    queue.append(neighbour)

        # If we processed exactly V nodes, we have a valid ordering; otherwise there's a cycle
        return "".join(order) if len(order) == V else ""

    def alienOrder(self, words: List[str]) -> str:
        """
        Derive the alien dictionary order from a sorted list of words.

        Parameters:
            words (List[str]): List of words already sorted according to the alien dictionary.

        Returns:
            str: A string representing one valid ordering of the alien alphabet.
                 Returns "" if the ordering cannot be determined (invalid / cyclic).
        """
        adj = defaultdict(list)

        # Step 1: Add all unique characters as nodes in the graph (even with no edges yet)
        for word in words:
            for s in word:
                adj[s] = []

        # Step 2: Build edges based on the first differing character between adjacent words
        for i in range(1, len(words)):
            str1 = words[i - 1]
            str2 = words[i]

            # Index to compare characters positionally
            i = 0
            match_count = 0
            min_length = min(len(str1), len(str2))

            # Find first non-matching character
            while i < min_length:
                if str1[i] != str2[i]:
                    # Precedence: str1[i] must come before str2[i]
                    adj[str1[i]].append(str2[i])
                    break
                else:
                    match_count += 1
                i += 1

            # Edge Case:
            # If all compared chars matched but previous word is longer,
            # then we have an invalid ordering (prefix rule violated).
            # Example: ["abc", "ab"] -> invalid.
            if match_count == min_length and len(str1) > len(str2):
                return ""

        # Step 3: Topologically sort the graph
        return self.topoOrder(adj)
