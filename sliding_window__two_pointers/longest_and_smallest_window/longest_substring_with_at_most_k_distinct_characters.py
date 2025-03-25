# Longest Substring with At Most K Distinct Characters

from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        left = right = 0
        distinctCharMap = defaultdict(int)
        maxLen = 0
        n = len(s)
        while right < n:
            distinctCharMap[s[right]] += 1
            if len(distinctCharMap) > k:
                ch = s[left]
                left += 1
                distinctCharMap[ch] -= 1
                if distinctCharMap[ch] == 0:
                    distinctCharMap.pop(ch)
            maxLen = max(maxLen, right - left + 1)
            right += 1
        return maxLen
