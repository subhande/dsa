# Max Chunks To Make Sorted

from collections import deque
from typing import List


class Solution1:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        """
        Key insight (pigeonhole argument):
        arr is a permutation of 0..n-1 (all distinct, no gaps).
        Scan left to right tracking maxValueSoFar = max(arr[0..idx]).

        At some index idx, suppose maxValueSoFar == idx.
        - We've seen idx+1 values so far: arr[0], arr[1], ..., arr[idx].
        - The largest among them is exactly idx.
        - Since all values are distinct and the max is idx, none of them
          can exceed idx -> every value in arr[0..idx] lies in {0,...,idx}.
        - That set {0,...,idx} has exactly idx+1 elements, and we have
          exactly idx+1 positions holding distinct values from it.
        - By pigeonhole, arr[0..idx] must contain EXACTLY the values
          {0,1,...,idx} - no more, no less, no value from outside range.
        - So sorting arr[0..idx] in isolation places 0,1,...,idx correctly
          in their final sorted positions, regardless of what's to the
          right. This makes idx a valid chunk boundary.

        Conversely, if maxValueSoFar > idx, some value > idx has appeared
        early (out of place), meaning that value needs to "reach forward"
        past position idx after sorting - so idx can't be a boundary yet.
        maxValueSoFar can never be < idx (pigeonhole again: idx+1 distinct
        non-negative values can't all be <= idx-1, i.e. squeeze into a
        smaller range), so the only two cases are ==idx (boundary) or >idx
        (not yet a boundary).

        Worked trace: arr = [1, 0, 2]
          idx=0, ele=1 -> maxValueSoFar=1 -> 1 == 0? No.   (1 is "ahead of itself")
          idx=1, ele=0 -> maxValueSoFar=1 -> 1 == 1? Yes.  chunk = [1,0], partitions=1
          idx=2, ele=2 -> maxValueSoFar=2 -> 2 == 2? Yes.  chunk = [2],   partitions=2
          -> [1,0] sorts to [0,1], [2] sorts to [2], concatenated = [0,1,2]. Correct.

        Time:  O(n) - single left-to-right pass, O(1) work per index
               (one comparison for max, one comparison for the boundary
               check - no nested loops, no slicing/copying of sub-arrays,
               so no hidden per-element cost like wLen-type factors here).
        Space: O(1) - only two scalar variables (maxValueSoFar, noOfPartitions)
               regardless of n; no auxiliary array is built.
        """
        maxValueSoFar = (
            -1
        )  # safe sentinel since arr[i] >= 0 always (permutation of 0..n-1);
        # int instead of float("-inf") keeps types consistent with arr's ints
        noOfPartitions = 0

        for idx, ele in enumerate(arr):
            maxValueSoFar = max(maxValueSoFar, ele)  # O(1) update

            if maxValueSoFar == idx:
                # pigeonhole condition met: arr[0..idx] is exactly {0,...,idx}
                # -> valid, independent, sortable chunk boundary here
                noOfPartitions += 1

        return noOfPartitions


class Solution2:
    def maxChunksToSorted(self, arr):
        n = len(arr)
        # Deque to store the maximum elements of each chunk
        stack = deque()

        for i in range(n):
            # Case 1: Current element is larger, starts a new chunk
            if not stack or arr[i] > stack[-1]:
                stack.append(arr[i])
            else:
                # Case 2: Merge chunks
                max_element = stack[-1]
                while stack and arr[i] < stack[-1]:
                    stack.pop()
                stack.append(max_element)

        return len(stack)
