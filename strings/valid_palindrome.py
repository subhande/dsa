class Solution1:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([_s for _s in s.lower() if _s.isalnum()])
        return s == s[::-1]


class Solution2:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1

        while i < j:
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True
