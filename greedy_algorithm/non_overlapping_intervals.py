# Non Overlapping Intervals

from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        limit = intervals[0][1]

        count = 0

        for i in range(1, len(intervals)):

            if limit > intervals[i][0]:
                count += 1
            else:
                limit = intervals[i][1]

        return count


class Solution2:
    # Function to compare intervals based on ending times
    @staticmethod
    def comp(val1, val2):
        # Compare the ending times of the intervals
        return val1[1] < val2[1]

    def MaximumNonOverlappingIntervals(self, intervals):
        # Sort the intervals based on their ending times
        intervals.sort(key=lambda x: x[1])

        # Get total number of intervals
        n = len(intervals)

        # Initialize counter
        cnt = 1

        # Keep track of the ending time
        last_end_time = intervals[0][1]

        # Iterate through all intervals
        for i in range(1, n):
            # Check if the starting time of the current
            # interval is greater than or equal to the
            # ending time of the last selected interval
            if intervals[i][0] >= last_end_time:
                # Increment counter
                cnt += 1
                # Update the ending time
                last_end_time = intervals[i][1]

        return n-cnt
