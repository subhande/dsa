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
        return result + min(prev, curr)


class Solution2:
    def countBinarySubstrings(self, s: str) -> int:
        prev = 0
        curr = 0
        validSubstringCount = 0
        curr = 1
        for i in range(1, len(s)):
            if s[i - 1] == s[i]:
                curr += 1
            else:
                prev = curr
                curr = 1
            validSubstringCount += 1 if prev >= curr else 0
        return validSubstringCount
