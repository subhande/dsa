# Find the index of the first occurrence in a string
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description

# Brute Force
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)

        if m == 0:
            return 0

        for i in range(n - m + 1):
            if haystack[i : i + m] == needle:
                return i

        return -1


# Rabin-Karp Algorithm
class Solution1:
    def strStr(self, haystack: str, needle: str) -> int:

        n = len(haystack)
        m = len(needle)
        if n < m:
            return -1

        # Primes for Rabin-Karp algorithm
        p = 7
        mod = 101

        # To store the hash values of pattern and substring of text
        hashPat = 0
        hashText = 0

        pRight = 1
        pLeft = 1

        # Computing the initial hash values
        for i in range(m):
            hashPat = (hashPat + ((ord(needle[i]) - ord("a") + 1) * pRight) % mod) % mod
            hashText = (
                hashText + ((ord(haystack[i]) - ord("a") + 1) * pRight) % mod
            ) % mod

            pRight = (pRight * p) % mod

        for i in range(n - m + 1):
            if hashPat == hashText:
                # Use this to check false positive
                if haystack[i : i + m] == needle:
                    return i

            if i < n - m:
                outgoing = ord(haystack[i]) - ord("a") + 1
                incoming = ord(haystack[i + m]) - ord("a") + 1
                hashText = (hashText - (outgoing * pLeft) % mod + mod) % mod
                hashText = (hashText + (incoming * pRight) % mod) % mod

                hashPat = (hashPat * p) % mod

                pLeft = (pLeft * p) % mod
                pRight = (pRight * p) % mod

        return -1


# KMP Algorithm: Brute Force
class Solution2:
    def computeLPS(self, s: str) -> list[int]:
        n = len(s)  # size of string

        # To store the longest prefix suffix
        LPS = [0] * n

        # Iterate on the string
        for i in range(1, n):
            # For all possible lengths
            for length in range(1, i):
                if s[:length] == s[i - length + 1 : i + 1]:
                    LPS[i] = length

        return LPS  # Return the computed LPS array

    def strStr(self, haystack: str, needle: str) -> int:
        s = needle + "$" + haystack  # Combined string

        # Function call to find the LPS array for the combined string
        LPS = self.computeLPS(s)

        # Length of pattern and text
        n, m = len(haystack), len(needle)

        # Iterate on the combined string after the delimiter
        for i in range(m + 1, len(s)):
            if LPS[i] == m:
                return i - 2 * m  # Return the starting index of the pattern in the text

        return -1


# KMP Algorithm: Optimized
class Solution3:
    def computeLPS(self, s: str) -> list[int]:
        n = len(s)  # size of string

        # To store the longest prefix suffix
        LPS = [0] * n

        i, j = 1, 0

        # Iterate on the string
        while i < n:
            # If the character matches
            if s[i] == s[j]:
                LPS[i] = j + 1
                i += 1
                j += 1

            # Otherwise
            else:
                # Trace back j pointer till it does not match
                while j > 0 and s[i] != s[j]:
                    j = LPS[j - 1]

                # If a match is found
                if s[i] == s[j]:
                    LPS[i] = j + 1
                    j += 1

                i += 1

        return LPS  # Return the computed LPS array

    def strStr(self, haystack: str, needle: str) -> int:
        s = needle + "$" + haystack  # Combined string

        # Function call to find the LPS array for the combined string
        LPS = self.computeLPS(s)

        # Length of pattern and text
        n, m = len(haystack), len(needle)

        # Iterate on the combined string after the delimiter
        for i in range(m + 1, len(s)):
            if LPS[i] == m:
                return i - 2 * m  # Return the starting index of the pattern in the text

        return -1
