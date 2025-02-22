# Number of distinct substrings in a string


class TrieNode:
    def __init__(self):
        self.links = [None] * 26
        self.flag = False

    def containsKey(self, ch):
        return self.links[ord(ch) - ord('a')] is not None

    def get(self, ch):
        return self.links[ord(ch) - ord('a')]

    def put(self, ch, node):
        self.links[ord(ch) - ord('a')] = node

    def setEnd(self):
        self.flag = True

    def isEnd(self):
        return self.flag

class Solution:

    def countDistinctSubstringBruteForce(self, s):
        substrings = set()

        for i in range(len(s)):
            substring = ""
            for j in range(i, len(s)):
                substring += s[j]
                substrings.add(substring)
        substrings.add("")
        return len(substrings)

    def countDistinctSubstring(self, s):
        root = TrieNode()
        distinct_count = 0

        # Generate all substrings starting at each index
        for i in range(len(s)):
            current_node = root
            for j in range(i, len(s)):
                ch = s[j]
                if not current_node.containsKey(ch):
                    # Create a new node if needed and count it as a new substring
                    current_node.put(ch, TrieNode())
                    distinct_count += 1
                current_node = current_node.get(ch)
        return distinct_count + 1

# Example usage:
sol = Solution()
s = "ababa"
print("Number of distinct substrings:", sol.countDistinctSubstring(s))
print("Number of distinct substrings:", sol.countDistinctSubstringBruteForce(s))

s = "aba"
print("Number of distinct substrings:", sol.countDistinctSubstring(s))
print("Number of distinct substrings:", sol.countDistinctSubstringBruteForce(s))
