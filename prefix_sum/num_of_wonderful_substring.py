# Number of Wonderful Substrings
"""
There are two types of substrings:
    - Substrings with all letters occurring an even number of times. e.g "aa", "bbbb"
    - Substrings with all letters occurring an even number of times, except for one letter that occurs an odd number of times e.g. "d", "bbd", "abb"

"""

from collections import defaultdict


class Solution:
    def wonderfulSubstrings(self, word: str) -> int:

        # Create the frequency map
        # Key = bitmask, Value = frequency of bitmask key
        freq = defaultdict(int)

        # The empty prefix can be the smaller prefix, which is handled like this
        freq[0] = 1

        mask = 0
        res = 0

        for idx, c in enumerate(word):
            bit = ord(c) - 97

            # Flip the parity of the c-th bit in the running prefix mask
            mask ^= 1 << bit

            # Count smaller prefixes that create substrings with no odd occurring letters
            print(["check", word[: idx + 1], mask, freq.get(mask)])
            if mask in freq:
                res += freq[mask]
                freq[mask] += 1
            else:
                freq[mask] = 1

            # Loop through every possible letter that can appear an odd number of times in a substring
            for odd_c in range(0, 10):
                print(
                    [
                        "single-check",
                        mask,
                        odd_c,
                        mask ^ (1 << odd_c),
                        freq.get(mask ^ (1 << odd_c)),
                    ]
                )
                if (mask ^ (1 << odd_c)) in freq:
                    res += freq[mask ^ (1 << odd_c)]

        return res


if __name__ == "__main__":
    word = "abbcc"
    print(Solution().wonderfulSubstrings(word))
