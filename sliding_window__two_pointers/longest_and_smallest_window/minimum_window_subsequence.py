# Minimum Window Subsequence

# Approach 1: Brute Force
class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        minWindow = float("inf")
        minWindowStartIdx = None
        minWindowEndIdx = None

        n, m = len(s1), len(s2)

        for idx in range(n):
            i = idx
            j = 0
            formed = 0
            while i < n and j < m:
                if s1[i] == s2[j]:
                    formed += 1
                    j += 1

                if formed == m and minWindow > (i - idx + 1):
                    minWindow = i - idx + 1
                    minWindowStartIdx = idx
                    minWindowEndIdx = i + 1
                i += 1

        return (
            s1[minWindowStartIdx:minWindowEndIdx]
            if minWindowStartIdx is not None
            else ""
        )


class Solution2:
    def minWindow(self, s1: str, s2: str) -> str:
        n, m = len(s1), len(s2)
        minWindow = ""
        i = 0

        while i < n:
            # Forward pass: find end of window
            j = 0
            while i < n and j < m:
                if s1[i] == s2[j]:
                    j += 1
                i += 1

            if j < m:  # s2 not fully matched
                break

            end = i  # exclusive end

            # Backward pass: shrink window from the end
            j = m - 1
            i -= 1
            while i >= 0 and j >= 0:
                if s1[i] == s2[j]:
                    j -= 1
                i -= 1

            start = i + 1  # tightest start

            if not minWindow or (end - start) < len(minWindow):
                minWindow = s1[start:end]

            i = start + 1  # move start forward by 1 and retry

        return minWindow
