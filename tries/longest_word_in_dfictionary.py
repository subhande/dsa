# Longest Word In Dictionary
from collections import deque


# Approach 1: Trie + BFS search | RAW Solution
# Time Complexity: O(S) where S is the total number of characters across all words | Space Complexity: O(S)
# - Insert: O(S), one O(1) step per character
# - BFS: O(26 * S), visits at most S nodes and scans 26 links per node
# - String building (prev + ch): O(S), each visited node is a word of length d built in O(d)
# - Space: trie has at most S nodes with 26 links each -> O(26 * S); queue holds at most one level of strings -> O(S)
class TrieNode:
    def __init__(self):
        # One slot per lowercase letter: links[0] = 'a', links[25] = 'z'
        self.links = [None] * 26
        # True if a word ends at this node
        self.flag = False

    def containsKey(self, ch) -> bool:
        return self.links[ord(ch) - ord("a")] is not None

    def put(self, ch, node):
        self.links[ord(ch) - ord("a")] = node

    def get(self, ch) -> "TrieNode" | None:
        return self.links[ord(ch) - ord("a")]

    def setEnd(self):
        self.flag = True

    def isEnd(self):
        return self.flag

    def getWordEndChildren(self):
        # Return (char, child) for every child that ends a word.
        # Scanning a -> z keeps results in alphabetical order.
        endNodes = []
        for idx, link in enumerate(self.links):
            if link and link.isEnd():
                endNodes.append((chr(idx + ord("a")), link))
        return endNodes


class Solution:
    def __init__(self):
        self.root: TrieNode = TrieNode()

    def insert(self, word):
        # Walk down the trie, creating missing nodes, then mark the last node as a word end
        node = self.root
        for ch in word:
            if not node.containsKey(ch):
                node.put(ch, TrieNode())
            node = node.get(ch)
        node.setEnd()

    def longestWord(self, words: list[str]) -> str:

        # Step 1: Build the trie from all words
        for word in words:
            self.insert(word)

        node = self.root

        # Step 2: Seed BFS with single-letter words (the only valid starting points)
        nodes = self.root.getWordEndChildren()

        # Queue holds (word built so far, trie node at the end of that word)
        queue = deque(nodes)

        maxLengthWord = ""
        maxLength = 0

        # Step 3: BFS level by level; level k holds valid words of length k
        while queue:
            n = len(queue)

            for _ in range(n):
                prev, node = queue.popleft()

                # Strict '<' keeps the first word of a new max length.
                # Each level is in alphabetical order, so that first word is the smallest.
                if maxLength < len(prev):
                    maxLength = len(prev)
                    maxLengthWord = prev

                # Only extend into children that are themselves complete words,
                # so every word reached is built one valid word at a time
                nextNodes = node.getWordEndChildren()

                for node in nextNodes:
                    queue.append((prev + node[0], node[1]))

        return maxLengthWord


# Approach 2: Trie (dict) + DFS | Optimized
# Time Complexity: O(S) | Space Complexity: O(S)
# - Same Big-O as Approach 1, but lower constants:
# - Word stored at end node -> no string building during the search
# - dict children -> each node stores only the letters it uses, not 26 slots
class Solution2:
    def longestWord(self, words: list[str]) -> str:
        # Step 1: Build the trie; each node is a dict of char -> child node
        root = {}
        for word in words:
            node = root
            for ch in word:
                # Move to the child, creating it if it doesn't exist
                node = node.setdefault(ch, {})
            node["$"] = word  # end marker holds the full word

        # Step 2: DFS from the root using an explicit stack
        best = ""
        stack = [root]
        while stack:
            node = stack.pop()
            for ch, child in node.items():
                if ch != "$" and "$" in child:  # only walk through complete words
                    w = child["$"]
                    # Prefer longer words; on equal length, prefer the alphabetically smaller one.
                    # Needed because DFS order doesn't guarantee alphabetical order.
                    if len(w) > len(best) or (len(w) == len(best) and w < best):
                        best = w
                    stack.append(child)
        return best
