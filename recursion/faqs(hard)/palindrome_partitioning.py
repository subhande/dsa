# Palindrome Partitioning


from typing import List
# Time Complexity: O(2^n) | Space Complexity: O(n)
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        self.dfs(s, [], result)
        return result

    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]

    def dfs(self, s: str, path: List[str], result: List[List[str]]):
        if not s:
            result.append(path)
            return
        for i in range(1, len(s) + 1):
            if self.isPalindrome(s[:i]):
                # add current substring in the currentList
                self.dfs(s[i:], path + [s[:i]], result)
                # backtrack and remove the current substring from currentList
