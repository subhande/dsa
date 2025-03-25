# Minimum Window Substring



from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        dict_t = Counter(t)

        required = len(dict_t)

        l, r = 0, 0
        formed = 0
        window_counts = {}
        minWindowSize = float("inf")
        windowStartIdx = 0

        while r < len(s):
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1
            if (
                character in dict_t
                and window_counts[character] == dict_t[character]
            ):
                formed += 1

            while l <= r and formed == required:
                character = s[l]
                # Save the smallest window until now.
                if r - l + 1 < minWindowSize:
                    minWindowSize = r - l + 1
                    windowStartIdx = l
                window_counts[character] -= 1

                if (
                    character in dict_t
                    and window_counts[character] < dict_t[character]
                ):
                    formed -= 1
                l += 1
            r += 1
        return "" if minWindowSize == float("inf") else s[windowStartIdx : windowStartIdx+minWindowSize]
