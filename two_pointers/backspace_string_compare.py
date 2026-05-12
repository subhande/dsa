class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        s_ptr = len(s) - 1
        t_ptr = len(t) - 1

        while s_ptr >= 0 or t_ptr >= 0:
            # Find next valid char in s
            skip = 0
            while s_ptr >= 0:
                # If we see a backspace, increment the skip count and move left
                if s[s_ptr] == "#":
                    skip += 1
                    s_ptr -= 1
                # If we see a non-backspace character and we have some backspaces to apply, decrement the skip count and move left
                elif skip > 0:
                    skip -= 1
                    s_ptr -= 1
                else:
                    break

            # Find next valid char in t
            skip = 0
            while t_ptr >= 0:
                # If we see a backspace, increment the skip count and move left
                if t[t_ptr] == "#":
                    skip += 1
                    t_ptr -= 1
                # If we see a non-backspace character and we have some backspaces to apply, decrement the skip count and move left
                elif skip > 0:
                    skip -= 1
                    t_ptr -= 1
                else:
                    break

            # Compare characters
            if s_ptr >= 0 and t_ptr >= 0:
                if s[s_ptr] != t[t_ptr]:
                    return False

            # One string ended earlier
            elif s_ptr >= 0 or t_ptr >= 0:
                return False

            s_ptr -= 1
            t_ptr -= 1

        return True
