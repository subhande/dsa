"""
Search Suggestions System (LeetCode 1268)

Given `products` and `searchWord`, after typing each character of `searchWord`
return up to 3 products (lexicographically smallest) that start with the
current prefix.

Four approaches are implemented below. Each redefines `Solution`, so only the
LAST definition is live when this module is imported.

    1. Trie + DFS          Build a plain trie; for each prefix walk down and
                           DFS children in sorted order until 3 words are found.
    2. Sort + two pointers Sort products; shrink a [left, right] window that
                           keeps only products matching the prefix so far.
    3. Sort + binary search Sort products; lower_bound(prefix) gives the first
                           candidate, take up to 3 that still match.
    4. Trie w/ cached top-3 Sort products, then insert; every node stores the
                           first 3 words passing through it. Query is a walk.

Notation:
    n = number of products
    m = average product length
    L = total characters across all products (~ n * m)
    w = len(searchWord)

Complexity comparison (output list excluded from space):

    | # | Approach               | Time                          | Extra space |
    |---|------------------------|-------------------------------|-------------|
    | 1 | Trie + DFS             | O(L + w * (w + m))            | O(L)        |
    | 2 | Sort + two pointers    | O(m * n log n + n + w)        | O(1)        |
    | 3 | Sort + binary search   | O(m * n log n + w * m * log n)| O(w)        |
    | 4 | Trie w/ cached top-3   | O(m * n log n + L + w)        | O(L)        |

    - Sorting compares strings, so each comparison costs up to O(m).
    - Sorting is counted as O(1) extra space (generic in-place sort convention).
      Python note: list.sort() is Timsort, which actually uses up to O(n)
      auxiliary memory. Language-specific, so it is left out of the table.
    - #1 per query: O(w) prefix walk + DFS that visits at most 3 root-to-word
      paths (each <= m nodes). Alphabet size (26) and string-copy costs
      from `prefix + ch` are treated as constants.

Which to pick:
    - #2 is the simplest and fastest in practice: no extra structure, and the
      pointers only move inward, so all queries together cost O(n + w).
    - #4 wins when the same product list serves MANY search words: build once,
      then each query is O(w).
    - #3 is a good fit when products are already sorted.
    - #1 is the textbook trie; slowest here because it re-walks the prefix and
      re-runs DFS for every character typed.
"""

from typing import List


# ---------------------------------------------------------------------------
# Approach 1: Trie + DFS
# Time:  O(L + w * (w + m))   Space: O(L)
# ---------------------------------------------------------------------------
class TrieNode:
    """Trie node: `links` maps char -> child, `flag` marks end of a word."""

    def __init__(self):
        self.links = {}
        self.flag = False

    def containsKey(self, ch):
        return ch in self.links

    def put(self, ch, node):
        self.links[ch] = node

    def get(self, ch):
        return self.links.get(ch)

    def setEnd(self):
        self.flag = True

    def isEnd(self):
        return self.flag

    def getAllChildren(self):
        """Child characters in sorted order, so DFS yields words lexicographically."""
        return sorted(self.links.keys())  # Sort children by character


class Trie:
    def __init__(self):
        self.root: TrieNode = TrieNode()

    def insert(self, word):
        """Add `word` to the trie. O(len(word))."""
        node = self.root
        for ch in word:
            if not node.containsKey(ch):
                node.put(ch, TrieNode())
            node = node.get(ch)
        node.setEnd()

    def search(self, word):
        """True if `word` was inserted exactly. O(len(word))."""
        node = self.root
        for ch in word:
            if not node.containsKey(ch):
                return False
            node = node.get(ch)
        return node.isEnd()

    def startsWith(self, prefix):
        """True if any inserted word starts with `prefix`. O(len(prefix))."""
        node = self.root
        for ch in prefix:
            if not node.containsKey(ch):
                return False
            node = node.get(ch)
        return True

    def searchSuggestion(self, prefix):
        """
        Return up to 3 lexicographically smallest words starting with `prefix`.

        Walk to the prefix node, then DFS its subtree visiting children in
        sorted order. A node is reported before its descendants, so shorter
        words come first (e.g. "mo" before "mob"). DFS stops once 3 words
        are collected.
        """
        node = self.root
        for ch in prefix:
            if not node.containsKey(ch):
                return []
            node = node.get(ch)
        words = []

        def dfs(node, prefix):
            nonlocal words
            if len(words) == 3 or node is None:
                return
            if node.isEnd():
                words.append(prefix)
            for ch in node.getAllChildren():
                dfs(node.get(ch), prefix + ch)

        dfs(node, prefix)
        return words


class Solution:
    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:
        # Build trie from all products (no sorting needed; DFS order handles it)
        trie = Trie()

        for product in products:
            trie.insert(product)

        # Query every prefix of searchWord from scratch
        suggestions = []
        for i in range(len(searchWord)):
            suggestions.append(trie.searchSuggestion(searchWord[: i + 1]))

        return suggestions


# ---------------------------------------------------------------------------
# Approach 2: Sort + two pointers
# Time:  O(m * n log n + n + w)
#        Sorting dominates. `left` only moves right and `right` only moves
#        left, so across ALL characters the pointers move at most n times.
# Space: O(1) extra, sort counted as in-place (output excluded).
#        Python note: Timsort uses up to O(n) auxiliary memory.
# ---------------------------------------------------------------------------
class Solution:
    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:
        products.sort()  # Sort products lexicographically

        suggestions = []

        # Invariant: products[left..right] are exactly the products that
        # match searchWord[:i]. Because the list is sorted, matches are contiguous.
        left, right = 0, len(products) - 1

        for i in range(len(searchWord)):
            ch = searchWord[i]

            # Move left pointer to the first product that matches the prefix
            while left <= right and (len(products[left]) <= i or products[left][i] != ch):
                left += 1

            # Move right pointer to the last product that matches the prefix
            while left <= right and (len(products[right]) <= i or products[right][i] != ch):
                right -= 1

            # Collect up to 3 suggestions from the current range
            suggestions.append(products[left : min(left + 3, right + 1)])

        return suggestions


# ---------------------------------------------------------------------------
# Approach 3: Sort + binary search
# Time:  O(m * n log n + w * m * log n)
#        Sorting, then one binary search per character; each string
#        comparison inside the search costs up to O(m).
# Space: O(w) for the growing `prefix` string; sort counted as in-place.
#        Python note: Timsort uses up to O(n) auxiliary memory.
# ---------------------------------------------------------------------------
class Solution:
    def lower_bound(self, arr: List[str], target: str, lo: int) -> int:
        """First index in [lo, len(arr)) with arr[i] >= target."""
        hi = len(arr)
        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        result = []
        bs_start = 0
        n = len(products)
        prefix = ""

        for c in searchWord:
            prefix += c

            # A longer prefix sorts at or after the shorter one, so the next
            # search can start where the previous one landed.
            start = self.lower_bound(products, prefix, bs_start)

            result.append([])

            # Take up to 3 words that still start with prefix
            i = start
            while i < min(start + 3, n) and products[i].startswith(prefix):
                result[-1].append(products[i])
                i += 1

            bs_start = start

        return result


# ---------------------------------------------------------------------------
# Approach 4: Trie with cached top-3 suggestions per node
# Time:  O(m * n log n + L + w)
#        Sort, build trie in O(L), then each query step is O(1).
# Space: O(L) nodes, each holding up to 3 word references.
# ---------------------------------------------------------------------------
class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestions = []  # up to 3 words passing through this node


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # Sorting first means the first 3 words to reach a node are the
        # 3 lexicographically smallest, so each node's cache is final.
        products.sort()
        root = TrieNode()

        # Build trie
        for word in products:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
                if len(node.suggestions) < 3:
                    node.suggestions.append(word)

        # Search: follow searchWord one char at a time. Once a char is
        # missing, every longer prefix has no matches either.
        result = []
        node = root
        for ch in searchWord:
            if node is not None and ch in node.children:
                node = node.children[ch]
                result.append(node.suggestions)
            else:
                node = None
                result.append([])

        return result
