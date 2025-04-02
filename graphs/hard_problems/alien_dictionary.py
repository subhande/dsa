# Alien Dictionary
"""

w -> r -> t
w -> r -> f
e -> r
e -> t

w -> r -> t -> f


"""

from collections import deque, defaultdict
from typing import List
class Solution:
    def topoOrder(self, adj):
        inDegree = defaultdict(int)
        V = len(adj)
        for node, edges in adj.items():
            if node not in inDegree:
                inDegree[node] = 0
            for edge in edges:
                inDegree[edge] += 1
        queue = deque()
        order = []
        for node, count in inDegree.items():
            if count == 0:
                queue.append(node)

        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbour in adj[node]:
                inDegree[neighbour] -= 1
                if inDegree[neighbour] == 0:
                    queue.append(neighbour)
        return "".join(order) if len(order) == V else ""

    def alienOrder(self, words: List[str]) -> str:
        adj = defaultdict(list)
        for word in words:
           for s in word:
             adj[s] = []
        for i in range(1, len(words)):
            str1 = words[i-1]
            str2 = words[i]
            i = 0
            match_count = 0
            min_length = min(len(str1), len(str2))
            while i < min(len(str1), len(str2)):
                if str1[i] != str2[i]:
                    adj[str1[i]].append(str2[i])
                    break
                else:
                    match_count += 1
                i += 1

            # if the match count is equal to the min length and the length of str1 is greater than str2
            # e.g. "abc", "ab" -> this order is invalid
            if match_count == min_length and len(str1) > len(str2):
                return ""


        return self.topoOrder(adj)
