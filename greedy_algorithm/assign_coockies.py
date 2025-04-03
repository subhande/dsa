# Assign Coockies

from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        cookieIdx = 0
        idx = 0
        count = 0
        while idx < len(g) and cookieIdx < len(s):
            if s[cookieIdx] >= g[idx]:
                cookieIdx += 1
                idx += 1
                count += 1
            else:
                cookieIdx += 1
        return count

# Time: O(N logN + M logM + M) | Space: O(1)
class Solution2:
    def findMaximumCookieStudents(self, Student, Cookie):

         # Sorting of lists
        student = sorted(Student)
        cookie = sorted(Cookie)

        # Pointers
        i, j = 0, 0
        n, m = len(student), len(cookie)

        max_student_with_cookies = 0

         # Traverse through both lists
        while i < n and j < m:
            """If the current cookie can satisfy
            the current student, move to the
            next student"""
            if cookie[j] >= student[i]:
                i += 1
                max_student_with_cookies += 1
            # Move to next cookie
            j += 1
        return max_student_with_cookies
