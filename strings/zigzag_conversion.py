# ZigZag Conversion


"""

s = "PAYPALISHIRING", numRows = 4

P       I       N
A    L  S    I  G
Y  A    H  R
P       I

answer = "PINALSIGYAHRPI"

- How many characters in one full zigzag cycle?
    - Down movement → numRows characters
    - Up diagonal → numRows - 2 characters

# Section Size = numRows + (numRows - 2) = 2 * numRows - 2
# Number of sections = ceil(n / (2 * numRows - 2.0))
# Number of columns = sections * (numRows - 1)

Example:
s = "PAYPALISHIRING", numRows = 4
n = 14
Section Size = 2 * numRows - 2 = 6
Number of sections = ceil(14 / 6) = 3
Number of columns = 3 * (4 - 1) = 9

Idellay 7 columns are required why create more ?
Because computing exact columns for the last partial cycle is complex. At max we wil overcompute by numRows - 2 columns which is not a big deal as we will ignore the empty spaces while creating the answer string.
"""
from math import ceil


class Solution:
    def convert(self, s: str, num_rows: int) -> str:
        if num_rows == 1:
            return s

        n = len(s)
        sections = ceil(n / (2 * num_rows - 2.0))
        num_cols = sections * (num_rows - 1)

        matrix = [[" "] * num_cols for _ in range(num_rows)]

        curr_row, curr_col = 0, 0
        curr_string_index = 0

        # Iterate in zig-zag pattern on matrix and fill it with string characters.
        while curr_string_index < n:
            # Move down.
            while curr_row < num_rows and curr_string_index < n:
                matrix[curr_row][curr_col] = s[curr_string_index]
                curr_row += 1
                curr_string_index += 1

            curr_row -= 2
            curr_col += 1

            # Move up (with moving right also).
            while (
                curr_row > 0 and curr_col < num_cols and curr_string_index < n
            ):
                matrix[curr_row][curr_col] = s[curr_string_index]
                curr_row -= 1
                curr_col += 1
                curr_string_index += 1

        answer = ""
        for row in matrix:
            answer += "".join(row)

        return answer.replace(" ", "")
if __name__ == "__main__":
    s = "PAYPALISHIRING"
    numRows = 4
    solution = Solution()
    print(solution.convert(s, numRows))
