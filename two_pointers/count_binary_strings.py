# 696. Count Binary Substrings


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        curr = 1
        prev = 0

        result = 0

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curr += 1
            else:
                result += min(prev, curr)
                prev = curr
                curr = 1
        print([result, prev, curr])
        return result + min(prev, curr)
