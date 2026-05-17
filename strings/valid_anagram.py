from collections import defaultdict


# Time Complexity: O(n) where n is the length of the string s or t | Space Complexity: O(1) since the frequency map will have at most 26 entries for lowercase English letters
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = defaultdict(int)
        n, m = len(s), len(t)
        if n != m:
            return False

        for i in range(n):
            freq[s[i]] += 1

        for i in range(m):
            if freq[t[i]] == 0:
                return False
            freq[t[i]] -= 1

        return True


# Time Complexity: O(n log n) where n is the length of the string s or t | Space Complexity: O(n) As python strings are immutable, sorting the string will require O(n) space to create a new sorted string
class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
