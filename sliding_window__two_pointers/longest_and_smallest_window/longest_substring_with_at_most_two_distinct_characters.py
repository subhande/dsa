from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        left, right = 0, 0
        n = len(s)
        freq = defaultdict(int)

        maxLen = 0

        while right < n:
            ch = s[right]

            freq[ch] += 1

            while len(freq) > 2:
                ch = s[left]

                freq[ch] -= 1

                left += 1

                if freq[ch] == 0:
                    del freq[ch]

            maxLen = max(maxLen, right - left + 1)

            right += 1

        return maxLen
