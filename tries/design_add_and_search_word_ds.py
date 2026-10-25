# Design Add and Search Word Data Structure
#
# Problem:
#   Support two operations:
#     - addWord(word): store a word (lowercase letters).
#     - search(word):  return True if any stored word matches `word`,
#                      where "." matches any single letter.
#
# Notation used in the complexities below:
#   m = length of the word being added / searched
#   N = number of words stored
#   T = total number of characters across all stored words (upper bound on trie nodes)
#
# Approaches (each class below redefines WordDictionary; the last one wins at import):
#
#   1. Hash map bucketed by length
#        addWord: O(m)            search: O(N_m * m), N_m = words of length m
#        Space:   O(T)
#        Pros: simplest code; add is just a set insert; fine when few words share a length.
#        Cons: search scans every word of the same length; no prefix sharing,
#              so it degrades to O(N * m) when most words have the same length.
#
#   2. Trie with fixed 26-slot array per node + BFS search
#        addWord: O(m)
#        search:  O(m) with no dots; worst case O(min(26^m, T)) with dots,
#                 since each trie node is visited at most once per query.
#        Space:   O(26 * T) for the trie; BFS queue holds up to one trie level.
#        Pros: O(1) child lookup by index; prefix sharing keeps search independent of N
#              for dot-free queries.
#        Cons: 26 pointers per node wastes memory on sparse tries; only supports 'a'-'z';
#              BFS expands every branch level by level instead of stopping on the first
#              full match down one path.
#
#   3. Trie with nested dicts + recursive DFS search  (recommended)
#        addWord: O(m)
#        search:  O(m) with no dots; worst case O(min(26^m, T)) with dots.
#                 The word[i + 1:] slice adds O(m) copying per recursive call.
#        Space:   O(T) for the trie (only existing children stored); O(m) recursion depth.
#        Pros: memory proportional to actual children; works for any character set;
#              DFS returns as soon as one path matches.
#        Cons: dict overhead per node; string slicing costs extra time/memory
#              (passing an index instead would avoid it); recursion depth grows with m.


from collections import defaultdict, deque


# Approach 1: Hash map bucketed by length
# addWord: O(m) | search: O(N_m * m) | Space: O(T)
class WordDictionary:
    def __init__(self):
        # word length -> set of words with that length
        self.d = defaultdict(set)

    def addWord(self, word: str) -> None:
        self.d[len(word)].add(word)

    def search(self, word: str) -> bool:
        m = len(word)

        # Only words of the same length can match
        for dict_word in self.d[m]:
            # Advance while characters match or the pattern has a wildcard
            i = 0
            while i < m and (dict_word[i] == word[i] or word[i] == "."):
                i += 1

            # Reached the end without a mismatch -> full match
            if i == m:
                return True
        return False


class TrieNode:
    def __init__(self):
        # Array to store links to child nodes
        # each index represents a letter of the alphabet
        self.links = [None] * 26
        # Flag indicating if the node
        # marks the end of a word
        self.flag = False

    # Check if the node contains a specific key(letter)
    def containsKey(self, ch):
        return self.links[ord(ch) - ord("a")] is not None

    # Insert a new node with a specific key(letter)
    def put(self, ch, node):
        self.links[ord(ch) - ord("a")] = node

    # Get the node with a specific key(letter)
    def get(self, ch):
        return self.links[ord(ch) - ord("a")]

    # Get all existing children (used when the pattern has a '.')
    def getWildcard(self):
        return [node for node in self.links if node]

    # Set the current node as the end of a word
    def setEnd(self):
        self.flag = True

    # Check if the current node marks the end of a word
    def isEnd(self):
        return self.flag

    def __str__(self):
        return str([self.links, self.flag])


# Approach 2: Array-based trie + BFS search
# addWord: O(m) | search: O(m) without dots, O(min(26^m, T)) with dots | Space: O(26 * T)
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    # Time Complexity O(m), where m is the length of the word
    def addWord(self, word: str) -> None:
        node = self.root

        # Walk down the trie, creating missing nodes along the way
        for ch in word:
            if not node.containsKey(ch):
                node.put(ch, TrieNode())
            node = node.get(ch)
        node.setEnd()

    def search(self, word: str) -> bool:
        node = self.root

        # Each queue entry is (trie node, index of next char in word to match)
        queue = deque()
        queue.append((node, 0))

        n = len(word)

        while queue:
            node, wordIdx = queue.popleft()

            if wordIdx == n:
                # Consumed the whole pattern; match only if a word ends here
                if node.isEnd():
                    return True
                    q
                # Wildcard: branch into every existing child
                nextNodes = node.getWildcard()
                for nextNode in nextNodes:
                    if nextNode is not None:
                        queue.append((nextNode, wordIdx + 1))
            else:
                # Regular letter: follow the single matching child, if any
                nextNode = node.get(word[wordIdx])
                if nextNode is not None:
                    queue.append((nextNode, wordIdx + 1))
        return False


# Approach 3: Dict-based trie + recursive DFS search
# addWord: O(m) | search: O(m) without dots, O(min(26^m, T)) with dots | Space: O(T)
class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Nested dicts: char -> child node; "$" key marks end of a word
        self.trie = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.trie

        for ch in word:
            if not ch in node:
                node[ch] = {}
            node = node[ch]
        node["$"] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any letter.
        """

        def search_in_node(word, node) -> bool:
            for i, ch in enumerate(word):
                if not ch in node:
                    # if the current character is '.'
                    # check all possible nodes at this level
                    if ch == ".":
                        for x in node:
                            # Skip the end-of-word marker; recurse on the rest of the pattern
                            if x != "$" and search_in_node(word[i + 1 :], node[x]):
                                return True

                    # If no nodes lead to an answer
                    # or the current character != '.'
                    return False

                # If the character is found
                # go down to the next level in trie
                else:
                    node = node[ch]

            # Pattern fully consumed; match only if a word ends here
            return "$" in node

        return search_in_node(word, self.trie)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
