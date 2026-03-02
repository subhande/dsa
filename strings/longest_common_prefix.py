# Longest Common Prefix

from typing import List

"""


Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


"""

# Approach 1: Horizontal Scanning
# Time Complexity: O(n*m) | Space Complexity: O(1)
# Time Complexity: O(s) where s is the sum of all characters in all strings in

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]

        for i in range(1, len(strs)):
            # We check if the current string starts with the prefix. If it does not, we remove the last character from the prefix and check again until we find a common prefix or the prefix becomes empty.
            while not strs[i].startswith(prefix):
                # If the current string does not start with the prefix, we remove the last character from the prefix and check again.
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix


# Approach 2: Vertical Scanning
# Time Complexity: O(n*m) | Space Complexity: O(1)
# Time Complexity: O(s) where s is the sum of all characters in all strings in the array.
# In this approach, we compare characters of the strings one by one. We start with the first character of the first string and compare it with the corresponding character of all other strings. If they match, we move to the next character. If they do not match, we return the common prefix found so far.
# In the worst case scenario is same as 1st one but in practice, it can be faster if the strings have a common prefix that is shorter than the length of the first string, as it will stop checking as soon as a mismatch is found.
class Solution2:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        for i in range(len(strs[0])):
            char = strs[0][i]
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != char:
                    return strs[0][:i]
        return strs[0]
